# Capstone-2

Week 1 to 4
* Download Dataset (APKs)
* Data Preprocessing
  * Decompile APKs to java source code, smali files and AndroidManifest.xml file.
  * Gather sensor usage info from the dataset. Identify the apps that use sensor data.
  * Calculate Jaccard Similarity and only keep the original-repackaged pairs that use sensor data.
  * Extract uses-permisson (UP) and uses-features (UF) info from AndroidManifest.xml file.
