For Presentations 5 I worked on a number of tasks supporting the other members of the CNN team:
* During the work period on Feb. 26th I attempted to set up a Sharepoint script that would allow others to access the patches without having to manually download each patch when the class finishes patching. This unfortunately did not work out as the data on Sharepoint is not configured as a Sharepoint site, making it impossible to access via Microsoft Azure.

* I spent the rest of the week reading up on the various CNN architectures we are using and understanding how they work to better prepare for finetuning our models next week.

For Presentation 6 I worked on the following:
* Adjusted patch overview image resolution - in `test_export_patches.ipynb` I have modified the `export_patched_slice` function to reduce the resolution of the image which shows where the patches are, so they are easier to evaluate.

* Wrote `preprocess_folder.py` used to filter erroneous uploads into the Patches folder on google drive. This ensures that the patches we get from the rest of the class are all 'good' patches suitable for training.
    * Excludes: 
        * "patched_..." files (images which show the locations of patches on each slice)
        * .tif files
        * subfolders
    * Includes: 
        * patches that are over 2KB (removes any erroneous tiny patches)
        * have "patch###" in their name

* Researched Google Colab credits and QUEST access, with relevant links found on `Presentation 6_CNN Team.pptx`