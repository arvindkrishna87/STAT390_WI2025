# Presentation 4 - Modifications to Kota's Kotap4_patching_code.ipynb


## Overview

This folder contains an edited versions of Kota's patching algorithm. His original code is linked here: https://github.com/arvindkrishna87/STAT390_WI2025/blob/54333ec943d45c0bb1d7b5722a818f76a389d449/Presentation%204/Thinkers/Kota%20Suzuki/kotap4_patching_code


### Jake_Kotap4_patching_code

* Added on_upload_change function which allows for multiple masks to be selected at once from the file explorer

* Changed cv2.threshold(image1_gray,1,255,cv2.THRESH_BINARY) => cv2.threshold(image_gray, 240, 255, cv2.THRESH_BINARY_INV) to allow his code to run on epithelium masks

* Added the number of patches in the metrics output
