import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name="dsprojects1"

list_of_files=[
    f"srce/{project_name}/__init__.py",
    f"srce/{project_name}/components/__init__.py",
    f"srce/{project_name}/components/data_ingestion.py",
    f"srce/{project_name}/components/data_transformation.py",
    f"srce/{project_name}/components/model_tranier.py",
    f"srce/{project_name}/components/model_monitoring.py",
    f"srce/{project_name}/pipelines/__init__.py",
    f"srce/{project_name}/pipelines/training_pipeline.py",
    f"srce/{project_name}/pipelines/prediction_pipeline.py",
    f"srce/{project_name}/exception.py",
    f"srce/{project_name}/logger.py",
    f"srce/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")