from src.TextSummarizer.config.configuration import ConfigurationManager
from src.TextSummarizer.components.model_trainer import ModelTrainer
from src.TextSummarizer.logging import logger
import transformers, datasets, accelerate, evaluate

print("Transformers:", transformers.__version__)
print("Datasets:", datasets.__version__)
print("Accelerate:", accelerate.__version__)
print("Evaluate:", evaluate.__version__)

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def initiate_model_trainer(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()