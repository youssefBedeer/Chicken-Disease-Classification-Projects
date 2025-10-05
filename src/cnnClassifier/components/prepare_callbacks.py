import tensorflow as tf
import time 
from cnnClassifier import logging
from cnnClassifier.config.configuration import PrepareCallbacksConfig
import os

class PrepareCallbacks: 
    def __init__(self, config:PrepareCallbacksConfig):
        self.config = config

    @property
    def _create_tb_callbaks(self):
        time_stamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(self.config.tensorboard_root_log, f'tb_log_at_{time_stamp}')
        logging.info(tb_running_log_dir)
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    
    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath = self.config.checkpoint_model_filepath,
            save_best_only = True
        )

    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbaks,
            self._create_ckpt_callbacks
        ]