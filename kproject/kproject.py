#!/usr/bin/env python

import os
import sys
import json
import glob
import argparse
import subprocess
from shutil import rmtree

from kproject.dataset import *
from kproject.constant import *
from kproject.utils import *

def _new_cmd(args):
    
    exist_flag = os.path.isdir(args.project_name)
    if args.yes:
        if exist_flag:
            rmtree(args.project_name)
    else:
        if exist_flag:
            print("[ ERROR ] `{}` has already created.".format(args.project_name))
            sys.exit(1)

    os.mkdir(args.project_name)
    print("[ NEW ] `{}/`".format(args.project_name))
    os.chdir(args.project_name)
    os.mkdir(DATASET_DIRNAME)
    print("[ NEW ] `{}/{}/`".format(args.project_name, DATASET_DIRNAME))
    os.mkdir(RESULT_DIRNAME)
    print("[ NEW ] `{}/{}/`".format(args.project_name, RESULT_DIRNAME))
    os.mkdir(MODEL_DIRNAME)
    os.makedirs("{}/{}".format(SRC_DIRNAME, LIB_DIRNAME))
    print("[ NEW ] `{}/{}/{}`".format(args.project_name, SRC_DIRNAME, LIB_DIRNAME))

    with open(README_FILENAME, 'w') as fout:
        fout.write("# {}\n\n".format(args.project_name))
    print("[ NEW ] `{}/{}`".format(args.project_name, README_FILENAME))

    with open(MAIN_FILENAME, 'w') as fout:
        fout.write(TEMPLATE_MAIN)
    print("[ NEW ] `{}/{}`".format(arg.project_name, MAIN_FILENAME))

    os.chmod(MAIN_FILENAME, 0o744)

    with open(ARGS_FILENAME, 'w') as fout:
        fout.write(TEMPLATE_ARGPARSE)
    print("[ NEW ] `{}/{}`".format(args.project_name, ARGS_FILENAME))
    
    with open(CONFIG_FILENAME, 'w') as fout:
        d = {
            "name": args.project_name,
            "experiments": [{ "cmd": ["./{}".format(MAIN_FILENAME), True]}]
        }
        fout.write("{}".format(json.dumps(d, fout, indent=4, sort_keys=True)))
    print("[ NEW ] `{}/{}`".format(args.project_name, CONFIG_FILENAME))

def _run_cmd(args):
    
    print("[ RUN ] `{}`".format(args.conf))
    
    if not os.path.exists(args.conf):
        print("[ Error ] Not found {}".format(args.conf))
        sys.exit(1)

    with open(args.conf, 'r') as fin:
        config = json.load(fin)

    for conf in config['experiments']:

        cmd = []

        if not conf['cmd'][1]:
            break

        cmd.append(conf['cmd'][0])
        del conf["cmd"]
        for k, v in conf.items():
            cmd.append("--{} {}".format(k, v))

        print(cmd)
        
        try:
            result = subprocess.check_output(
                ' '.join(cmd),
                shell=True,
            )
            print(result.decode('hex'))
        
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
        help='[DANGEROUS] Overwrite project directory of same name'
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
