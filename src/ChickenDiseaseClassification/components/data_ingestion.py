import os
import urllib.request as request
import zipfile
from ChickenDiseaseClassification import logger
from ChickenDiseaseClassification.utils.common import get_size
import logging
from ChickenDiseaseClassification.entity.config_entity import *
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        self.logger = logging.getLogger()  # Obtain a logger instance

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file)

            self.logger.info(f"Downloaded {filename} with info: \n{headers}")
        else:
            self.logger.info(f"File {self.config.local_data_file} already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
