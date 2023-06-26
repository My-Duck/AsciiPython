import multiprocessing
import cv2
from multiprocessing import Process
from PIL import Image, ImageDraw, ImageOps

ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


class Ascii:
    """
     method resize_image(image, new_width)
     - takes as parameters the image, and the final width
     - resizes the image into the final width while maintaining aspect ratio
    """

    @staticmethod
    def resize_image(image, new_width):
        width, height = image.size
        ratio = height / width / 1.65
        new_height = int(new_width * ratio)
        resized_image = image.resize((new_width, new_height))
        return resized_image, new_width

    @staticmethod
    def pixels_to_ascii_image(image):
        pixels = image[0].getdata().convert("L")
        new_width = image[1]
        characters = ""
        for pixel in pixels:
            characters += ASCII_CHARS[pixel // 25]
        ascii_image = []
        # Construct the ascii image from the character str
        for i in range(0, len(characters), new_width):
            ascii_image.append(characters[i:i + new_width])
        return ascii_image

    """
        method create_picture(str_list):
            - takes as parameters the list of str ascii image
            - create image 
    """

    @staticmethod
    def create_picture(str_list):

        rows, cols = len(str_list), len(str_list[0])
        scale = 8
        created_image = Image.new("RGB",
                                  (cols * scale, rows * scale))

        draw_image = ImageDraw.Draw(created_image)

        for row in range(rows):
            for col in range(cols):
                draw_image.text(
                    (col * scale, row * scale),
                    str_list[row][col])

        return created_image

    """
       method create_video(file, output, num_cols)
       - takes as parameters the input file,output file name, final width
       - create ascii video
    """

    @staticmethod
    def create_video(file, new_width):
        frames = []
        images = []
        cap = cv2.VideoCapture(file)
        #fps = int(cap.get(cv2.CAP_PROP_FPS))
        while cap.isOpened():
            flag, frame = cap.read()
            if flag:
                frame = Image.fromarray(frame)
            else:
                break
            frames.append(frame)
        cap.release()
        """for im in frames:
            images.append(Ascii.create_picture(Ascii.pixels_to_ascii_image(Ascii.resize_image(im, new_width),
                                                                       ))) """
        a = []
        for im in frames:
            a.append(Ascii.pixels_to_ascii_image(Ascii.resize_image(im, new_width)))
        with multiprocessing.Pool(10) as p:
            images = p.map(Ascii.create_picture, a)
            p.close()
            p.join()
        return images

    """
          method create_gif(file, new_width)
          - takes as parameters the input, final width
          - create ascii gif
    """

    @staticmethod
    def create_gif(file, new_width):
        images = []
        with Image.open(file) as im:
            n_frame = im.n_frames
            for i in range(0, n_frame):
                im.seek(i)
                images.append(Ascii.create_picture(Ascii.pixels_to_ascii_image(Ascii.resize_image(im, new_width))))
        return images
