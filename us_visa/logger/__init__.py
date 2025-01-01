import logging
import os
import sys
from datetime import datetime


file_name=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
file_dir=os.path.join("logs",file_name)
os.makedirs(file_dir,exist_ok=True)

log_file_path=os.path.join(file_dir,file_name)

logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(filename)s - %(levelname)s - %(lineno)d - %(message)s",
    level=logging.INFO
)



