import os
import shutil

class FileOrganization:
    def __init__(self, source_dir, target_dir):
        self.source_dir = source_dir
        self.target_dir = target_dir

    def organize_file(self):
        for file_name in os.listdir(self.source_dir):
            source_path = os.path.join(self.source_dir, file_name)

            if os.path.isfile(source_path):
                if ".jpeg" in file_name:
                    target_path = os.path.join(self.target_dir, "jpeg")
                    target_path = os.path.join(target_path, file_name)
                    shutil.move(source_path, target_path)
                    print(f"Moved jpg: {source_path} -> {target_path}")

                elif ".txt" in file_name:
                    target_path = os.path.join(self.target_dir, "txt")
                    target_path = os.path.join(target_path, file_name)
                    shutil.move(source_path, target_path)
                    print(f"Moved jpg: {source_path} -> {target_path}")
                
                else:
                    target_path = os.path.join(self.target_dir, "xlsx")
                    target_path = os.path.join(target_path, file_name)
                    shutil.move(source_path, target_path)
                    print(f"Moved jpg: {source_path} -> {target_path}")
                
            else:
                print(f"Skipping directory: {source_path}")


source_directory = "/home/developer/Documents/Data_Engineering/code_prectice/source_testing_files"
target_directory = "/home/developer/Documents/Data_Engineering/code_prectice/target_testing_files"

file_object = FileOrganization(source_directory, target_directory)
file_object.organize_file()