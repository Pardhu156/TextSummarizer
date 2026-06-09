import os
import urllib.request as request
import zipfile
from src.TextSummarizer.logging import logger

from datasets import load_dataset
from src.TextSummarizer.logging import logger

from src.TextSummarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_dataset(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info("Downloading SAMSum dataset from Hugging Face")

            dataset = load_dataset("knkarthick/samsum")
            dataset.save_to_disk(self.config.local_data_file)

            logger.info(f"SAMSum dataset saved to {self.config.local_data_file}")

        else:
            logger.info(f"Dataset already exists at {self.config.local_data_file}")