# README: Enhancements to Epithelium Patching Code

## Before Improvement
In the original code, I found that the best epithelium coverage was achieved using a `smoothing_size` of 15 to help reduce noise. Tuning this parameter demonstrated the impact that generalizing and reducing noise could have, as it dramatically changed my coverage scores.

## Improvements
- **Patch Length Averaging:**  
  The `contour_patch_lengths` are now updated to use the average patch length of adjacent neighbors. The number of adjacent neighbors it looks to can be tuned by the parameter `adj_neighbor_span` but I found best coverage when it was set to 4. This change smooths out the patch boundaries by reducing local noise in the patch size estimates.

- **Increased Overlap Threshold:**  
  As a result of the averaging, there was sometimes a slight reduction in overlap. I achieved better coverage by increasing the `overlap_threshold` from 0.3 to 0.5, ensuring more robust overall epithelium coverage.

## Impact
Overall, the improvements led to an enhancement in performance.


