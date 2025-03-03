Generalized Smoothing Improvement
Identified Issues:
- The original implementation used a parameter smoothing_size to compute tangents.
- This approach determined tangents based on only two contour points, making it sensitive to noise and local variations.
- The smoothing_size parameter was not performing true smoothing. This may have led to inefficient patch placements.
Issue Fixed:
- Replaced the smoothing_size approach with a Gaussian filter-based smoothing of contour tangents.
- This ensures tangents are computed more reliably by averaging local gradients. This helps reduce the sensitivity to noise.
- The update generalizes smoothing, eliminating the need for the smoothing_size parameter.
Updates Made:
- Implemented gaussian_filter1d from scipy.ndimage to smooth gradients before computing tangents.
- Removed the previous approach using smoothing_size for tangent calculations.
- Normalized the filtered tangents to ensure consistency in vector direction.
- Also removed any use or mention of smoothing size in setting of parameters or the results metrics
Where to See the Update in Code:
- The update is in the section where tangents and normals are computed:
- Before: Tangents were computed using a fixed smoothing_size index-based approach.
- After: Gradients (dx, dy) are now smoothed using gaussian_filter1d(dx, sigma=2) and gaussian_filter1d(dy, sigma=2) before normalizing.
- The update is located in the loop processing each contour, under the comment # Getting tangents and normals on contour points.
- The other update is the removal of smoothing size in the metrics = section of the code at the end of the code and the removal of smoothing size as a parameter at the start of the code
