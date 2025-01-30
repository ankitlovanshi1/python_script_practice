import os
import pandas as pd

class ToDoList:
    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description
    
    def add(self, file_path):
        """Adds a new project to the Excel file."""
        new_record = pd.DataFrame({
            "Name": [self.name],
            "Description": [self.description]
        })

        try:
            existing_df = pd.read_excel(file_path, engine='openpyxl')
            final_df = pd.concat([existing_df, new_record], ignore_index=True)
        except FileNotFoundError:
            final_df = new_record  # Create new file if it doesn't exist
        
        final_df.to_excel(file_path, index=False, engine='openpyxl')
        print(f"Project '{self.name}' added successfully!")
    
    def remove(self, file_path):
        """Removes a project from the Excel file based on its name."""
        if not os.path.exists(file_path):
            print("File not found!")
            return
        
        try:
            df = pd.read_excel(file_path, engine='openpyxl')
            df = df[df["Name"] != self.name]
            df.to_excel(file_path, index=False, engine='openpyxl')
            print(f"Project '{self.name}' removed successfully!")
        except Exception as e:
            print("Error while removing project:", e)
    
    @staticmethod
    def show(file_path):
        """Displays all projects stored in the Excel file."""
        if not os.path.exists(file_path):
            print("No projects found!")
            return
        
        try:
            df = pd.read_excel(file_path, engine='openpyxl')
            print("Project Details:\n", df)
        except Exception as e:
            print("Error while reading the file:", e)

# File path
file_path = "/home/developer/Downloads/project_details_task.xlsx"

# Example usage
project1 = ToDoList("Intuit", "This is Intuit project")
project2 = ToDoList("AWS", "This is AWS project")
project1.add(file_path)
project2.add(file_path)

# Remove a project
remove_project = ToDoList("AWS")
remove_project.remove(file_path)

# Show all projects
ToDoList.show(file_path)
