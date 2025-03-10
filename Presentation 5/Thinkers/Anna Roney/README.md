# Presentation 5 - Putting Everything Together


## Overview

This folder contains two final versions of the patching algorithm and the patch exporting code. The patch export code is explained in the pdf titled 'Patch Extraction Code Logif'. This export code relies on the slice images (tifs) and masks (pngs) being in a folder called `testing_slices`. Inside that folder, create a folder called `patch_outputs` for the patches to be exported into. In the 'testing_slices' folder, all image files (tifs AND pngs) must start with `case_{case_number}_match_{match_number}`. See the patchers presentation 5 slides for a screenshot of what a correct 'testing_slices' folder looks like.

During presentation 5 both Kota and Ryan worked on modifying the patching code to remove the smoothing_size parameter. 

### final_kota

This file combines kotap5_patching_code.ipynb with my patch export code.

 - this code takes averages of multiple tangents on the contour, actually implementing a smoothing mechanism, in order to eliminate the smoothing_size parameter
- uses the area of the epithelium mask to eliminate any patches that fall outside of certain percentages of the area of the mask
- still trying to figure out how to handle patches that straddle two distinct regions of the epithelium. 
    - two new functions: sample_line_pixels and epithelium_to_background
    - sample_line_pixel gets the pixel values along a start and end point. 
    - used to find the pixel values along the four sides of each patch - eptihelium_to_background checks to see whether these sides of the patches flag a pattern that reveals that a patch is straddling two distinct regions
    - pattern is epithelium -> non-epithelium -> epithelium
    - If this pattern is flagged, that patch is removed and replaced with a smaller patch
    - still figuring out how to cover the rest of the region with more patches to cover for the large, removed patch
    - This means the performance is slightly worse with this functionality


### final_ryan

This is a combined version of Ryan's patching code and my patch export code.

- This code creates a series of squares around the all exterior contours of a cell, normal to its outline, that can then be extracted into images
- The only paramters passed into the function is overlap_threshold
- This approach has the benefit of automatically adjusting the rotation of the squares over the cell
- This approach uses gradient calculation and gaussian smoothing for accurate tangents at all contour points
