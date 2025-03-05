# Optimization of Codes

## Issues Identified 

1. Patches are sensitive to factor smoothing_size, which is just making tangents on two points as mentioned in the codes.
2. It require manual input and adjustment every single time, making the process exhaustive.
3. Making smoothing based on two points and not average of multiple also make it harder to precisely capture patches

## Issues I fixed
1. I defined a new function called calculate_tangents, which is able to compute local tangent by averaging a window of nearby points around the specific countor and thus calculate tangent vectors between multiple neighborhood points and average them(default to 5 but able to change)
2. This eliminates the smoothing_size adjustment and generalize to all tangent calculations by computing tangents using local window points around each point in vector
3. It significantly improved the epithelium coverage for almost all matches, the code just didn't work once, which I opt going back to original method.
## Update I made
1. The update I made is removing smooth size, create new function, and adjust contour codes as needed. It can be seen in the following changed code chunks.
# Function to calculate tangent for each point base on surrounding points
def calculate_tangents(contour_points, window_size=5):
    number_contour_points = len(contour_points)
    tangents = np.zeros_like(contour_points, dtype=float)
    
    for i in range(number_contour_points):
        start = max(i - window_size // 2, 0)
        end = min(i + window_size // 2 + 1, number_contour_points)
        window_points = contour_points[start:end]
        vectors = np.diff(window_points, axis=0)
        tangent = np.mean(vectors, axis=0)
        tangent = tangent / (np.linalg.norm(tangent) + 1e-8)  
        tangents[i] = tangent
    
    return tangents

for contour in contours:
    contour_points = contour.reshape(-1, 2)
    tangents = calculate_tangents(contour_points, window_size=5)
    
    normals = np.zeros_like(tangents)
    normals[:, 0] = -tangents[:, 1]
    normals[:, 1] = tangents[:, 0]
    
    all_normals.append(normals)
    all_tangents.append(tangents)
    
all_patches = []
all_patch_lengths = []
height, width = epithelium_mask_2D.shape
