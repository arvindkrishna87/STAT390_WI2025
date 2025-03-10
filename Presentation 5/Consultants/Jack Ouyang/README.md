# Code Improvements: Summary

## Initially adjusted parameters:
- `smoothing_size` = 25

## Issue
- Tiny patches:
  - There are many patches with a length of 2, which is far too small to provide any real information, and just looks like spots, rather than actual patches. 

## Code updates
- Minimum and maximum patch sizes (Line 20-21, 143)
  - This allows for a minimum and maximum patch size to be set, to eliminate the possibility of the very small or very large patches
- Automated read in of slices (Lines 24-49, 73)
  - This loops through a dictionary of file names of the tif files and the names of the corresponding masks, so instead of changing it for each item, you can run the code once to create patches for all slices.
