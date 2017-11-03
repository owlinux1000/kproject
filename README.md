# Kproject

kproject is initializing tool to clean repo and to wirte experiment code quickly.

## Tutorial

```
$ kproject new mnist
[ CREATE ] New project: `mnist`
$ cd mnist; ls -R
.:
README.md  dataset  model  result  src

./dataset:

./model:

./result:

./src:
lib  main.py

./src/lib:
args.py
```

### Useful function

1. `src/lib/args.py`

This script was already written template for argument parser. If you wanna add some opttion, should write this file.

2. `src/main.py`

This is main file for experiment.

3. Logging

	1. kproject.log.KprojectLog
	
	This is abstract class for Logging
	
	2. kproject.log.TxtLog
	
	Basic logging tools
	   
	3. kproject.log.MDLog

	Useful logging tools. You can log as markdown.
	
## Install

```
$ pip install git+https://bitbucket.org/encry1024/kproject
```
