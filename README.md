# Capstone-2

Week 1 to 4
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
  
Week 5
* Get authors of the apps. <br/>
  **Pipeline: [get_author_v1.ipynb](https://github.com/Programming-Systems-Lab/Capstone-2/blob/master/Data%20Preprocessing/get_author_v1.ipynb)**
* Obtain all parts of data from each team member and combine separate files into one csv file.
  **Data: ["data" folder](https://github.com/Programming-Systems-Lab/Capstone-2/tree/master/data)
* Data Visualization
  * Sensor Usage: pie chart, stacked bar chart, 100% stacked bar chart, histogram
  * Jaccard Similarity: histogram
  * Difference: ..
  * Uses-features & Uses-permissions: ..
  * Author: dot plot
