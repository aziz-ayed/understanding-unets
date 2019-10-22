"""Inspired by https://github.com/sicara/tf-explain/blob/master/tf_explain/callbacks/grad_cam.py"""
import tensorflow as tf
from tensorflow.keras.callbacks import Callback


class TensorBoardImage(Callback):
    def __init__(self, log_dir, image, noisy_image):
        super().__init__()
        self.log_dir = log_dir
        self.image = image
        self.noisy_image = noisy_image

    def set_model(self, model):
        self.model = model
        self.writer = tf.summary.create_file_writer(self.log_dir, filename_suffix='images')

    def on_train_begin(self, _):
        self.write_image(self.image, 'Original Image', 0)

    def on_train_end(self, _):
        self.writer.close()

    def write_image(self, image, tag, epoch):
        with self.writer.as_default():
            tf.summary.image(tag, image, step=epoch)

    def on_epoch_end(self, epoch, logs={}):
        denoised_image = self.model.predict_on_batch(self.noisy_image)
        self.write_image(denoised_image, 'Denoised Image', epoch)
