
* Put the [code2vec](https://github.com/tech-srl/code2vec) project here, and replace the interactive_predict.py with our file.

* Create a folder called [models](https://github.com/Programming-Systems-Lab/Capstone-2/tree/master/Data%20Preprocessing/code2vec/models).

* Run the following command to generate vectors:
```
python3 code2vec.py --load models/random/saved_model_iter2 --export_code_vectors --predict
```

A folder called csv will be created and the vectors will be inside.
