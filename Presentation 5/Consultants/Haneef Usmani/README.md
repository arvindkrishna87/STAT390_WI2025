Read me:

- Problem 1: Large patches extended into non-epithelial tissue, increasing background noise.    
- Fix1: Reduced \`smoothing\_size\` to improve tangent alignment:

Code Improvement:

- Implemented vectorization for tangent normalization and boundary checks, decreased runtime for big slices (case 87\) by 40%