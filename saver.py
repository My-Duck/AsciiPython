import cv2
import numpy as np
from PIL import ImageOps


class saver:
    @staticmethod
    def save_video(data_2_save,out_file):
        images = data_2_save
        for out_image in images:
            cropped_image = ImageOps.invert(out_image).getbbox()
            out_image = out_image.crop(cropped_image)
            out_image = np.array(out_image)
            try:
                out
            except:
                out = cv2.VideoWriter(out_file, cv2.VideoWriter_fourcc(*"MP4V"), 24,
                                      (out_image.shape[1], out_image.shape[0]))
            out.write(out_image)
        out.release()
        print("saved in: " + out_file)