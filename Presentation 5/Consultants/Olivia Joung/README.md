# Code Improvements: Summary

## Adjusted parameters:
- `smoothing_size` = 70

## Identified issues after first run:
- Tiny patches:
  - Especially with longer/larger epithelia, there were frequent instances of very small patches (essentially resembling random spots amid the more accurate, normal-sized patches).
  - Not only would these obviously fail to capture the epithelium, but they would also often be inaccurately placed—frequently being located in the stroma or background rather than the actual epithelium itself, for example.
- Wide epithelia and/or large tissues
  - With larger epithelia/tissues, the patches were often less accurately placed. With cases like Match 1 of Case 63, for example, the patches—while accurate placed—were so large that they also captured a fair portion of stroma/background as well.
  - Based on the parameters, it appears that the `extension_factor` should be increased to 1.2 for larger tissues.
