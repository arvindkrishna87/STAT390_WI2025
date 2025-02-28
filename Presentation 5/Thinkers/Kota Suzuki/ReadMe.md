# Presentation 5 - Kota's patching code modifications
### kotap5_patching_code.ipynb

This week I worked on removing the `smoothing_size` parameter and removing any large/small patches. To remove the `smoothing_size` parameter, I am now taking averages of multiple tangents on the contour, actually implementing a smoothing mechanism. 

To remove any large/small patches without any ad-hoc parameters, I took Ryan's idea of using the area of the epithelium mask to eliminate any patches that fall outside of certain percentages of the area of the mask. 

Implementing these two changes, the performance on the patch increased from roughly 94% -> 97% on case 85. 