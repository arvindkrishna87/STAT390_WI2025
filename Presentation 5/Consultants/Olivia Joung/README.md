# Code Improvements: Summary

## Initially adjusted parameters:
- `smoothing_size` = 70

## Identified issues after first run:
- Tiny patches:
  - Especially with longer/larger epithelia, there were frequent instances of very small patches (essentially resembling random spots amid the more accurate, normal-sized patches).
  - Not only would these obviously fail to capture the epithelium, but they would also often be inaccurately placed—frequently being located in the stroma or background rather than the actual epithelium itself, for example.
- Wide epithelia and/or large tissues
  - With larger epithelia/tissues, the patches were often less accurately placed. With cases like Match 1 of Case 63, for example, the patches—while accurate placed—were so large that they also captured a fair portion of stroma/background as well.
  - Based on the parameters, it appears that the `extension_factor` should be increased to 1.2 for larger tissues.

## Code updates to `patch_corners` function (2)
- Adjusted `extension_factor` to 1.2 for large enough tissues (Lines 89-97)
  - As an initial test, I tried increasing the `extension_factor` only for tissues with an `epithelium_width` greater than `max_width/2`.
  - I noticed the epithelium coverage across multiple tissues significantly improved and therefore decided to leave the threshold as is. In the future, I may continue to test thresholds either higher or lower than `max_width/2` and see if other values yield even more accurate results.
  - Given the new `adjusted_extension_factor`, I also adjusted `patch_length` and `half_patch_length`
- Skipped tiny patches (Lines 99-102)
  - I added code that automatically skips over any patch with less than a `patch_length` of 20.
  - Similarly to my previous change, this value of 20 came from testing with multiple values across different patches. This appeared to be the smallest possible value for effectively eliminating small, unnecessary patches, however further testing may also prove a different value to be more efficient at this task.
