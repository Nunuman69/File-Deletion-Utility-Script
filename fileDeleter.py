import os
import re

#Path to the directory containing the files
directory_path = r'd:\TEST FOLDER'  # Adjust this to your actual directory path

#Function to determine the base name of the file including its extension
def get_base_name(filename):
    match = re.match(r"(.+?)(?: \(\d+\))?(\.[^\.]+)$", filename)
    if match:
        return match.group(1)
    return None

file_tracker = {}

#Looping through each file in the directory to categorize them
for filename in os.listdir(directory_path):
    base_name = get_base_name(filename)
    if base_name:
        if base_name not in file_tracker:
            file_tracker[base_name] = []
        file_tracker[base_name].append(filename)

#Identifying and deleting duplicates, keeping the first file
for base_name, files in file_tracker.items():
    if len(files) > 1:  #If condition to only proceed if there's dulicates
        for file in files[1:]:  #Skips the first file by starting from the second
            file_path = os.path.join(directory_path, file)
            try:
                os.remove(file_path)
                print(f'Deleted duplicate file: {file}')
            except Exception as e:
                print(f"Error deleting file {file}: {e}")

#Output statement after operation is complete
print("Duplicate files have been deleted.")
