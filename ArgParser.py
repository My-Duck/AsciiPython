import os
import argparse


class ArgParser:
    def __init__(self, args):
        self.args_parser = argparse.ArgumentParser()

        self.args_parser.add_argument('--file', dest='imgFile', required=True,
                                      help='sample: --file cat.jpg')
        self.args_parser.add_argument('--out', dest='outFile', default='out', required=False,
                                      help='default: out.jpg, sample: --out cat')
        self.args_parser.add_argument('--width', dest='width', type=int, default=250,  required=False,
                                      help='default: 250 , sample: --width 100')

        self._args = self.args_parser.parse_args(args)

        self.outFile = self._args.outFile
        self.imgFile = self._args.imgFile
        self.width = self._args.width
