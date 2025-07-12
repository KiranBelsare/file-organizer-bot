import os
import shutil

folder_path = "/Users/kiranbelsare/Desktop/organizer_test"

for file in os.listdir(folder_path):
    full_path = os.path.join(folder_path, file)

    # Ignore folders, only touch files
    if os.path.isdir(full_path):
        continue

    # Split filename and extension
    filename, extension = os.path.splitext(file)

    # Decide destination folder
    if extension.lower() in [".png", ".jpg", ".jpeg"]:
        folder_name = "Images"
    elif extension.lower() in [".pdf", ".txt", ".docx"]:
        folder_name = "Documents"
    elif extension.lower() in [".py"]:
        folder_name = "Python Files"
    else:
        folder_name = "Others"

    # Build destination folder path
    dest_folder = os.path.join(folder_path, folder_name)
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Move the file
    shutil.move(full_path, os.path.join(dest_folder, file))