# Default filename or dirname
MAIN_FILENAME='src/main.py'
ARGS_FILENAME='src/lib/args.py'
HISTORY_FILENAME='.history'
README_FILENAME='README.md'
DATASET_DIRNAME='dataset'
RESULT_DIRNAME='result'
MODEL_DIRNAME='model'
SRC_DIRNAME='src'
LIB_DIRNAME='lib'

# Default program
TEMPLATE_MAIN = '''#!/usr/bin/env python
from lib.args import CONFIG

if __name__ == '__main__':
    pass
    # Write here'''

TEMPLATE_ARGPARSE = '''import argparse

_parser = argparse.ArgumentParser()
_parser.add_argument('--dataset', type=str, help='Set dataset path')
_parser.add_argument('--title', type=str, help='Set experiment title')
_parser.add_argument('--debug', action='store_true', default=False, help='Run in debug mode')

# Write here some option you wanna add

CONFIG = vars(_parser.parse_args())'''
