# Sensor-Based Repackaged Malware Detection
![visual](https://github.com/Programming-Systems-Lab/Capstone-2/blob/master/visual2.png)

### Overview
Android is one of the most popular operating systems (OS) for mobile environment in the world. Because of its popularity, Android is also the most targeted mobile OS by malware. Researchers have found that most of the Android malware uses repackaged apps as their preferred means to propagate into users’ devices. Therefore, repackaged apps not only infringe the copyright on the original apps but also threaten the health of the Android ecosystem. Thus, it is imperative to detect repackaged apps in various app markets so as to stop the spread of malware. Since adversaries can easily repackage malicious code into various benign apps, the detection of malware becomes more and more difficult.  

Presently, various approaches have been developed to detect repackaged apps, ranging from similarity computation to runtime monitoring, and to supervised or unsupervised learning. In this project, we want to explore if sensors used by apps can give some insight into malware detection. We study a publicly available dataset of repackaged apps available at [AndroZoo](https://androzoo.uni.lu/api_doc). There are several steps involved in the study, beginning with an exploratory analysis of repackaged apps that utilize innocuous sensors of the phone. Currently, we are working on this step, finding the difference between the sensors used by original apps and repackaged apps, and exploring other potential features that might be useful for the detection of repackaged applications. During the second half of this semester, we will 1) identify if the repackaged app is malware or not; 2)build a classifier to detect the repackaged malware if there is some pattern found during the exploratoryanalysis; 3) achieve other additional goals.

### Contribution
Contribution of our work is three-fold:
* We build a tool to extract the sensors actually used by an app, as opposed to the sensors mentioned in the Android manifest file but never used;
* We find evidence that the repackaged evasive malware utilize more senors than the original application;
* We further investigate the relationship between the repackaged apps using sensors and the authors. In particular, we study the authors’ generated repackaged apps and their sensor usage style


### Required packages
The following packages are required to decompile APKs and extract Java source code and xml files: <br/>
* [dex2jar](https://github.com/pxb1988/dex2jar): download and extract dex2jar to the root folder where the folder of APKs is stored. <br/>
* [jd-cli](https://github.com/kwart/jd-cli): download the command line Java decompiler jd-cli to the root folder. <br/>
* [apktool](https://github.com/kwart/jd-cli): download and install the latest version of apktool. <br/>

Now you are good to go! The decompilation pipeline is in [Decompile_apk_v5.ipynb](https://github.com/Programming-Systems-Lab/Capstone-2/blob/master/Data%20Preprocessing/Decompile_apk_v5.ipynb)


### Progress (continuously updating)

**Week 1 to 4**
* Download dataset (APKs)
* Data Preprocessing
  * Decompile APKs to java source code, smali files and AndroidManifest.xml file. <br/>
    **Pipeline: [Decompile_apk_v5.ipynb](https://github.com/Programming-Systems-Lab/Capstone-2/blob/master/Data%20Preprocessing/Decompile_apk_v5.ipynb)**
  * Gather sensor usage info from the dataset. Identify the apps that use sensor data. <br/> 
    **Pipeline: [Gather_Sensor-v4.ipynb](https://github.com/Programming-Systems-Lab/Capstone-2/blob/master/Data%20Preprocessing/Gather_Sensor-v4.ipynb)**
  * Calculate Jaccard Similarity and only keep the original-repackaged pairs that use sensor data. <br/> 
    **Pipeline: [Jaccard Similarity.ipynb](https://github.com/Programming-Systems-Lab/Capstone-2/blob/master/Data%20Preprocessing/Jaccard%20Similarity.ipynb)**
  * Extract uses-permisson (UP) and uses-features (UF) info from AndroidManifest.xml file. <br/> 
    **Pipeline: [FindUP_UF_v4.ipynb](https://github.com/Programming-Systems-Lab/Capstone-2/blob/master/Data%20Preprocessing/FindUP_UF_v4.ipynb)**
  
**Week 5**
* Get authors of the apps. <br/>
  **Pipeline: [get_author_v1.ipynb](https://github.com/Programming-Systems-Lab/Capstone-2/blob/master/Data%20Preprocessing/get_author_v1.ipynb)**
* Obtain all parts of data from each team member and combine separate files into one csv file. <br/>
  **Data: ["data" folder](https://github.com/Programming-Systems-Lab/Capstone-2/tree/master/data)**
* Data Visualization. <br/>
  * Sensor Usage: pie chart, stacked bar chart, 100% stacked bar chart, histogram. <br/>
  * Jaccard Similarity: histogram. <br/>
  * Difference: visna <br/>
  * Uses-features & Uses-permissions: stacked bar chart <br/>
  * Author: dot plot. <br/>
 
**Week 6**
* Analyze data. <br/>
* Finish first progress report. <br/>

**Week 7**
* EDA on AndroZoo dataset (malware & benign apps). <br/>
* Do feature exploration. <br/>
* Model tuning, training and testing (LR, SVM, KNN, XGBoost, DNN). <br/>
  * Features <br/>
    * With sensor features <br/>
    * Without sensor features <br/>
  * Test set <br/>
    * The test set splitted from Training_Dataset.csv <br/>
    * The test set only containing repackaged benign apps <br/>
    * COVID dataset <br/>
* Experiments on the threshold (currently, 0: benign, >=2: malware) <br/>
* Finish BigData2020 Poster <br/>

**Week 8**
* Finish BigData2020 1-page paper <br/>
* EDA on AndroZoo dataset (malware & benign apps) <br/>
* Feature exploration <br/>

**Week 9**
* Finish BigData2020 3-page paper <br/>

**Week 10**
* Extract the hashes of the libraries used by benign apps and save them in a list; Extract the hashes of the libraries used by malware; Check if the hashes of a malware are all in the list. If yes, then the feature `if_the_app_using_suspicious_libs` should be 0; if not, the feature should be 1  <br/>


**Week 11**
* Run models for different thresholds  <br/>
* Finish the second progress report  <br/>

**Week 12**
* Build code2vec pipeline <br/>
  * Put all the decompiled file at the same level as this project, inside a folder named *decompile*
  * Generate a JSON file containing the java file paths of interest for apps: [Get Java Files.ipynb](https://github.com/Programming-Systems-Lab/Capstone-2/blob/master/Data%20Preprocessing/Get%20Java%20Files.ipynb)<br /> This file can be downlaoded from our google drive and stored in [Capstone-2/Data Preprocessing](https://github.com/Programming-Systems-Lab/Capstone-2/tree/master/Data%20Preprocessing)
  * Go to the directory of [Capstone-2/Data Preprocessing/code2vec](https://github.com/Programming-Systems-Lab/Capstone-2/tree/master/Data%20Preprocessing/code2vec), follow the instructions to get the vector representations.

