#!/usr/bin/env python

import os
import sys
import json
import argparse
import subprocess
from shutil import rmtree

from kproject.dataset import *
from kproject.constant import *
from kproject.utils import *

def _new_cmd(args):
    
    print("[ CREATE ] New project: `{}`".format(args.project_name))
    exist_flag = os.path.isdir(args.project_name)
    if args.yes:
        if exist_flag:
            rmtree(args.project_name)
    else:
        if exist_flag:
            print("[ ERROR ] `{}` has already created.".format(args.project_name))
            sys.exit(1)

    os.mkdir(args.project_name)
    os.chdir(args.project_name)
    os.mkdir(DATASET_DIRNAME)
    os.mkdir(RESULT_DIRNAME)
    os.mkdir(MODEL_DIRNAME)
    os.makedirs("{}/{}".format(SRC_DIRNAME, LIB_DIRNAME))

    with open(MAIN_FILENAME, 'w') as fout:
        fout.write(TEMPLATE_MAIN)

    os.chmod(MAIN_FILENAME, 0o744)

    with open(ARGS_FILENAME, 'w') as fout:
        fout.write(TEMPLATE_ARGPARSE)

    with open(README_FILENAME, 'w') as fout:
        fout.write("# {}\n\n".format(args.project_name))

    with open(CONFIG_FILENAME, 'w') as fout:
        d = {
            "name": args.project_name,
            "experiments": [{ "cmd": "./{}".format(MAIN_FILENAME)}]
        }
        fout.write("{}".format(json.dumps(d, fout, indent=4, sort_keys=True)))
        
def _run_cmd(args):

    with open(args.conf, 'r') as fin:
        config = json.load(fin)

    cmd = []
    for conf in config['experiments']:
        print(conf)

    try:
        result = subprocess.check_output(
            cmd,
            shell=True,
        )
        print(result.decode('hex'))
        sys.exit(0)
        
    except:
        print("[ Error ] Can't run {}".format(args.conf))
        sys.exit(1)

def main():

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    
    parser_new = subparsers.add_parser('new', help='see `new -h`')
    
    parser_new.add_argument(
        'project_name'
    )
    parser_new.add_argument(
        '-y',
        '--yes',
        action='store_true',
        default=False,
        help='[DANGEROUS] Overwrite project directory'
    )
    parser_new.set_defaults(func=_new_cmd)

    parser_run = subparsers.add_parser('run', help='see `run -h`')
    parser_run.add_argument(
        '-c',
        '--conf',
        type=str,
        default='kproject.json',
        help='Set the file of config (Default: kproject.json)'
    )
    
    parser_run.set_defaults(func=_run_cmd)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
        sys.exit(0)

    sys.exit(1)


if __name__ == '__main__':
    
    main()
