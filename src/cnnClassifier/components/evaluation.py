from cnnClassifier.config.configuration import EvaluationConfig
import tensorflow as tf
from cnnClassifier.utils.common import save_json
from pathlib import Path

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config 

    def _valid_generator(self):
        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation= "bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            rescale = 1./255,
            validation_split = 0.20
        )
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory = self.config.training_data_dir,
            subset= "validation",
            shuffle = False,
            **dataflow_kwargs
        )
        return self.valid_generator
    
    @staticmethod    
    def load_model(path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    def evaluation(self):
        self.model = self.load_model(self.config.trained_model_path)
        self._valid_generator() 
        self.score = self.model.evaluate(self.valid_generator)

    def save_scores(self):
        scores = {
            "loss": self.score[0],
            "accuracy": self.score[1]
        }
        save_json(path= Path("scores.json"), data=scores)