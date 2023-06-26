import multiprocessing
import unittest
from PIL import Image

from ArgParser import ArgParser
from ascii import Ascii


class MyTestCase(unittest.TestCase):
    def test_parser_true(self):
        parser = ArgParser(['--file', 'cat.jpg'])
        self.assertEqual(parser.imgFile, 'cat.jpg')

    def test_value_error(self):
        with self.assertRaises(ValueError):
         Ascii.resize_image(Image.new('RGBA',(10,10),(0,0,0)),-1)

    def test_value_error_Ascii(self):
        self.assertEqual(['$$$', '$$$', '$$$'],Ascii.pixels_to_ascii_image(Image.new('RGBA',(3,3),(0,0,0)),3))

    def test_create_frame_TypeError(self):
        with self.assertRaises(TypeError):
            Ascii.create_picture(1)

    def test_create_gif_AttributeError(self):
        with self.assertRaises(AttributeError):
            Ascii.create_gif(1,1)

    def test_create_video_UnboundLocalError(self):
        self.assertEqual([], Ascii.create_video(1,1,1))

    def test_create_frame_Error(self):
        with self.assertRaises(IndexError):
            Ascii.create_picture(['22221', '2222'])


if __name__ == '__main__':
    unittest.main()

