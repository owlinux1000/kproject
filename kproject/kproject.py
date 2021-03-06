#!/usr/bin/env python

import os
import sys
import json
import glob
import argparse
import subprocess
from shutil import rmtree

from kproject.constant import *
from kproject.utils import *

def _new_cmd(args):

    name = args.project_name
    
    info("Create new `{}`".format(name))

    exist_flag = os.path.isdir(name)

    if args.yes:
        if exist_flag:
            rmtree(name)
    else:
        if exist_flag:
            error("`{}` has already created.".format(name))
            sys.exit(1)

    os.mkdir(name)
    os.chdir(name)
    os.mkdir(DATASET_DIRNAME)
    os.mkdir(RESULTS_DIRNAME)
    os.mkdir(MODELS_DIRNAME)
    os.makedirs("{}/{}".format(SRC_DIRNAME, LIB_DIRNAME))

    with open(README_FILENAME, 'w') as fout:
        fout.write("# {}\n\n".format(name))

    with open(MAIN_FILENAME, 'w') as fout:
        fout.write(TEMPLATE_MAIN)

    os.chmod(MAIN_FILENAME, 0o744)

    with open(ARGS_FILENAME, 'w') as fout:
        fout.write(TEMPLATE_ARGPARSE)

    # TODO Implemented by OrderDict and modify run command
    with open(CONFIG_FILENAME, 'w') as fout:
        d = {
            "experiments": [
                {
                    CMD_KEY: MAIN_FILENAME,
                    EXEC_FLAG_KEY: True,
                    ARGS_KEY: {
                        
                    }
                }
            ]
        }
        fout.write("{}".format(json.dumps(d, fout, indent=4, sort_keys=True)))

def _run_cmd(args):

    info("Run in `{}`".format(args.conf))
    
    if not os.path.exists(CONFIG_FILENAME):
        error("Could not find `{}` in `{}`".format(CONFIG_FILENAME, os.getcwd()))
        sys.exit(1)
        
    if not os.path.exists(args.conf):
        error("Could not find `{}` in `{}`".format(args.conf, os.getcwd()))
        sys.exit(1)
        
    with open(args.conf, 'r') as fin:
        config = json.load(fin)

    for conf in config[TOP_KEY]:

        cmd = ['python', '-u']

        if not conf[EXEC_FLAG_KEY]:
            continue

        cmd.append(conf[CMD_KEY])
        del conf[CMD_KEY]
        del conf[EXEC_FLAG_KEY]

        for k, v in conf[ARGS_KEY].items():
            cmd.append("--{}".format(k))
            if not v is None:
                cmd.append(v)

        for i, c in enumerate(cmd):
            if type(c) != str:
                cmd[i] = str(c)
        try:
            p = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            
            for line in iter(p.stdout.readline, b''):
                print(line.rstrip().decode('utf-8'))
        
        except:
            error("Coudl not run `{}`".format(args.conf))
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
        help='[DANGEROUS] Overwrite directory of the same name'
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

    parser.print_help()
    sys.exit(1)


if __name__ == '__main__':
    
    main()
