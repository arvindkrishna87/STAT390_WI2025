# Presentation 5 - Kota's patching code modifications
### kotap5_patching_code.ipynb

This week I worked on removing the `smoothing_size` parameter and removing any large/small patches. To remove the `smoothing_size` parameter, I am now taking averages of multiple tangents on the contour, actually implementing a smoothing mechanism. 

To remove any large/small patches without any ad-hoc parameters, I took Ryan's idea of using the area of the epithelium mask to eliminate any patches that fall outside of certain percentages of the area of the mask. 

STILL WORK-IN-PROGRESS: trying to figure out how to handle patches that straddle two distinct regions of the epithelium. To get around this, I introduce two new functions: `sample_line_pixels` and `epithelium_to_background`. `sample_line_pixel` gets the pixel values along a start and end point. It is used to find the pixel values along the four sides of each patch. `eptihelium_to_background` checks to see whether these sides of the patches flag a pattern that reveals that a patch is straddling two distinct regions. This pattern is epithelium -> non-epithelium -> epithelium. 

If this pattern is flagged, that patch is removed 