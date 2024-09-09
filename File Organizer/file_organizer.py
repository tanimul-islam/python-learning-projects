import os
import shutil

def create_subfolder_if_needed(folder_path, subfolder_name):
    """
    Creates a subfolder within the specified folder if it doesn't already exist.

    Parameters:
    folder_path (str): The path of the main folder where the subfolder will be created.
    subfolder_name (str): The name of the subfolder to create.

    Returns:
    str: The full path of the created or existing subfolder.
    """
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path

def sort_folder(folder_path):
    """
    Sorts the files in the specified folder by their file extensions. 
    Moves each file into a corresponding subfolder named after its file type.

    Parameters:
    folder_path (str): The path of the folder to be sorted.

    Returns:
    None
    """
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            # Extract file extension and convert it to lowercase
            file_extension = filename.split('.')[-1].lower()
            if file_extension:
                # Create subfolder name based on file extension
                subfolder_name = f"{file_extension.upper()} Files"
                subfolder_path = create_subfolder_if_needed(folder_path, subfolder_name)
                
                # Full path of the current file
                file_path = os.path.join(folder_path, filename)
                
                # Move the file to the corresponding subfolder
                shutil.move(file_path, subfolder_path)
                print(f"Moved: {filename} -> {subfolder_name}/")

if __name__ == "__main__":
    print("File Organizer Script")
    
    # Specify the folder path to be organized
    folder_path = "C:\\Users\\tanim\\Downloads"
    
    # Check if the provided folder path is valid
    if os.path.isdir(folder_path):
        sort_folder(folder_path)
        print("Everything is Organized!!")
    else:
        print("Invalid folder path. Please ensure the path is correct and try again")
