import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')

project_name = "red_wine_quality_prediction"


# List of file paths to be created
list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml", 
    "main.yaml",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
    "templates/index.html"
]
        

for filepath in list_of_files:
    filepath = Path(filepath)  # Convert string path to a Path object for cleaner handling

    # Split the path into directory and filename parts
    filedir, filename = os.path.split(filepath)

    # If the path includes directories, ensure they exist
    if filedir != "":
        # Create directories if they don't already exist
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for file: {filename}")

    # If the file does not exist OR is empty (size == 0)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # check if its empty, if its not then the existing content will get overwritten
        # Create an empty file (open in write mode and close immediately)
        with open(filepath, "w") as f:
            pass  # No content written, just ensures the file exists
        logging.info(f"Created empty file: {filepath}")
    
    else:
        # Log that the file already exists and is not empty
        logging.info(f"{filename} already exists and is not empty.")