import os
import shutil

# Path to the 'Train' folder
train_folder = 'Train'

# Iterate over each sub-directory in the 'Test' folder
for subdir in os.listdir(train_folder):
    subdir_path = os.path.join(train_folder, subdir)
    
    # Check if the sub-directory is a directory
    if os.path.isdir(subdir_path):
        # Get the list of all files in the sub-directory
        files = os.listdir(subdir_path)
        
        # Sort the files alphabetically
        files.sort()
        
        # Keep the first 1000 files and delete the rest
        for file in files[110:]:
            file_path = os.path.join(subdir_path, file)
            os.remove(file_path)
