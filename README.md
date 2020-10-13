# Capstone-2

Week 1 to 4
* Download dataset (APKs)
* Data Preprocessing
  * Decompile APKs to java source code, smali files and AndroidManifest.xml file. 
    **Pipeline: Decompile_apk_v5.ipynb**
  * Gather sensor usage info from the dataset. Identify the apps that use sensor data.  (**Pipeline: Gather_Sensor-v4.ipynb**)
  * Calculate Jaccard Similarity and only keep the original-repackaged pairs that use sensor data.  (**Pipeline: Jaccard Similarity.ipynb**)
  * Extract uses-permisson (UP) and uses-features (UF) info from AndroidManifest.xml file.  (**Pipeline: FindUP_UF_v2.ipynb**)
  
  
