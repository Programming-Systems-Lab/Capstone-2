# Capstone-2

Week 1 to 4
* Download dataset (APKs)
* Data Preprocessing
  * Decompile APKs to java source code, smali files and AndroidManifest.xml file. <br/>
    **Pipeline: Decompile_apk_v5.ipynb** [link](https://github.com/Programming-Systems-Lab/Capstone-2/blob/master/Data%20Preprocessing/Decompile_apk_v5.ipynb)
  * Gather sensor usage info from the dataset. Identify the apps that use sensor data. <br/> 
    **Pipeline: Gather_Sensor-v4.ipynb**
  * Calculate Jaccard Similarity and only keep the original-repackaged pairs that use sensor data. <br/> 
    **Pipeline: Jaccard Similarity.ipynb**
  * Extract uses-permisson (UP) and uses-features (UF) info from AndroidManifest.xml file. <br/> 
    **Pipeline: FindUP_UF_v2.ipynb**
  
  
