# Final Patching ALgorithm! 
## final_patching_code.ipynb

The final patching algorithm should run smoothly as long as you have the following folders:
1. A folder named `testing_slices` 
2. A folder within that folder named `patch_outputs`
3. Both your mask (.png) and tissue slice (.tif) in the format: `case_{case_number}_match_{match_number}_{h&e/melan/sox10}`

The final patching algorithm includes the following new features (since presentation 5): 
* Ryan's Gaussian smoothing functionality for more optimal tangents (importantly eliminates `smoothing_size` as a parameter)
* Anna's patch export functionality that allows all masks and tissue slices within the folder to be executed at once 
* Sharon's `patching_export` functionality that outputs the original image + the mask with patches included 
* John's epithelium-within-an-epithelium functionality in `get_contours`
* Jake's mask smoothing to help address the small patch problem

