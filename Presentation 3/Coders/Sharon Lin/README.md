# Presentation 2 - Sharon's Patching Code

## Instructions

This patching algorithm can be run through using the 'qupath_extraction_code.txt' and 'patching_sharon.ipynb' files. 

First, go to QuPath and manually annotate the epithelium region of a tissue slice of your choice with the labels 'Positive', 'Negative', and 'Ignore*' (analogous to benign/low-grade/high-grade we will use as our actual labels). Then, go to the 'Automate' tab and click 'Script Editor', pasting the code from 'qupath_extraction_code.txt' into the pop-up screen to export your annotations to a png file (note: I then changed this png file to a tif file to match the file type of the original tissue slice). 

Then, open 'patching_sharon.ipynb', replacing the image directory with your own, and run all cells of the file to get resulting patched image. 

## Data

An example annotated tissue slice, along with its original image, is uploaded to https://drive.google.com/drive/folders/12msIkWGyN0iZ_5N_pmF8iFQZIbKXDwF6?usp=sharing.