# Sensor-Based Repackaged Malware Detection

### Overview
Android is one of the most popular operating systems (OS) for mobile environment in the world. Because of its popularity, Android is also the most targeted mobile OS by malware. Researchers have found that most of the Android malware uses repackaged apps as their preferred means to propagate into users’ devices. Therefore, repackaged apps not only infringe the copyright on the original apps but also threaten the health of the Android ecosystem. Thus, it is imperative to detect repackaged apps in various app markets so as to stop the spread of malware. Since adversaries can easily repackage malicious code into various benign apps, the detection of malware becomes more and more difficult.  

Presently, various approaches have been developed to detect repackaged apps, ranging from similarity computation to runtime monitoring, and to supervised or unsupervised learning. In this project, we want to explore if sensors used by apps can give some insight into malware detection. We study a publicly available dataset of repackaged apps available at [AndroZoo](https://androzoo.uni.lu/api_doc). There are several steps involved in the study, beginning with an exploratory analysis of repackaged apps that utilize innocuous sensors of the phone. Currently, we are working on this step, finding the difference between the sensors used by original apps and repackaged apps, and exploring other potential features that might be useful for the detection of repackaged applications. During the second half of this semester, we will 1) identify if the repackaged app is malware or not; 2)build a classifier to detect the repackaged malware if there is some pattern found during the exploratoryanalysis; 3) achieve other additional goals.

### Contribution
Contribution of our work is three-fold:
* We build a tool to extract the sensors actually used by an app, as opposed to the sensors mentioned in the Android manifest file but never used;
* We find evidence that the repackaged evasive malware utilize more senors than the original application;
* We further investigate the relationship between the repackaged apps using sensors and the authors. In particular, we study the authors’ generated repackaged apps and their sensor usage style

### Workflow
![](https://github.com/Programming-Systems-Lab/Capstone-2/blob/master/HighLevel.png)


### Progress (continuously updating)
**Week 1 to 4**
* Download dataset (APKs)
* Data Preprocessing
![decompilation](https://github.com/Programming-Systems-Lab/Capstone-2/blob/master/Decompilation.png)
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
  * Difference: .. <br/>
  * Uses-features & Uses-permissions: .. <br/>
  * Author: dot plot. <br/>
 
**Week 6**
* Analyze data. <br/>
* Finish first progress report. <br/>
