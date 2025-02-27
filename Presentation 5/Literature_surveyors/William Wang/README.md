
# Adaptive Smoothing and Triple Stain Processing

## Issues
• It is quite inefficient to relabel hardcode
• The model uses fixed Smoothing

## Fix and Code

### A way to label variables automatically was inserted at the start of a code block:

patient_number = "h2114171" 
case_match = "highgrade_case18_match1"  

stain_roi_map = {
    "h&e": "3",
    "melan": "2",
    "sox10": "1"
}
Iterate through each stain type and its respective ROI number
for stain, roi_number in stain_roi_map.items():

### Adaptive Smoothing and a Contour Counter was loosely inserted in function definition code block and the start of the countour for loop

def adaptive_smoothing_size(num_contour_points):
    return max(100, int(num_contour_points * 0.05))



smoothing_size = adaptive_smoothing_size(num_contour_points)  # Dynamic smoothing size

