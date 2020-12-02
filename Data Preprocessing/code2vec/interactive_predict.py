import traceback
import json
import os
import pandas as pd
import time

from common import common
from extractor import Extractor

SHOW_TOP_CONTEXTS = 10
MAX_PATH_LENGTH = 8
MAX_PATH_WIDTH = 2
JAR_PATH = 'JavaExtractor/JPredict/target/JavaExtractor-0.0.1-SNAPSHOT.jar'


class InteractivePredictor:
    exit_keywords = ['exit', 'quit', 'q']

    def __init__(self, config, model):
        model.predict([])
        self.model = model
        self.config = config
        self.path_extractor = Extractor(config,
                                        jar_path=JAR_PATH,
                                        max_path_length=MAX_PATH_LENGTH,
                                        max_path_width=MAX_PATH_WIDTH)

    def read_file(self, input_filename):
        with open(input_filename, 'r') as file:
            return file.readlines()

    def predict(self):
        try:
            os.mkdir('csv/')
        except FileExistsError:
            pass

        with open('../javaPahts.json') as f:
            data = json.load(f)
        print('Starting interactive prediction...')
        counter = 0
        start_time = time.time()
        for app in data:
            appVectors = []
            if counter>1:
                break
            counter +=1
            for javaPath in data[app]:
                #print(
                #    'Modify the file: "%s" and press any key when ready, or "q" / "quit" / "exit" to exit' % input_filename)
                #user_input = input()
                #if user_input.lower() in self.exit_keywords:
                #    print('Exiting...')
                #    return
                inputfile = 'input.java'
                input_filename = os.path.join("..",javaPath)
                print(input_filename)
                try:
                    predict_lines, hash_to_string_dict = self.path_extractor.extract_paths(inputfile)
                except ValueError as e:
                    print('bad bad')
                    print(e)
                    continue
                raw_prediction_results = self.model.predict(predict_lines)
                method_prediction_results = common.parse_prediction_results(
                    raw_prediction_results, hash_to_string_dict,
                    self.model.vocabs.target_vocab.special_words, topk=SHOW_TOP_CONTEXTS)
                #count = 0
                for raw_prediction, method_prediction in zip(raw_prediction_results, method_prediction_results):
                    #if count >0:
                        #print("too many vectors!")
                    #count +=1
                    #print('Original name:\t' + method_prediction.original_name)
                    #for name_prob_pair in method_prediction.predictions:
                        #print('\t(%f) predicted: %s' % (name_prob_pair['probability'], name_prob_pair['name']))
                    #print('Attention:')
                    #for attention_obj in method_prediction.attention_paths:
                        #print('%f\tcontext: %s,%s,%s' % (
                        #attention_obj['score'], attention_obj['token1'], attention_obj['path'], attention_obj['token2']))
                    if self.config.EXPORT_CODE_VECTORS:
                        appVectors.append( raw_prediction.code_vector)
                        print('Code vector:')
                        print(' '.join(map(str, raw_prediction.code_vector)))
                        #print(type(raw_prediction.code_vector))
                #if count ==1:
                    #print("perfect!")
            pd.DataFrame(appVectors).to_csv('csv/'+app+'.csv',index=False)
        print("--- %s seconds ---" % (time.time() - start_time))
