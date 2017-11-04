# Kproject

kproject is initializing tool to clean repo and to wirte experiment code quickly.

## Tutorial

First, you use ```new``` command of kproject and create new some directories and files such.

```
$ kproject new mnist
$ cd mnist; ls -R
README.md     dataset       kproject.json model         result        src

./dataset:

./model:

./result:

./src:
lib     main.py

./src/lib:
args.py
```

Here is recommend usage of these directories.

|name|recommend way to use|
|:--:|:--:|
|dataset|Save some dataset you use.|
|models|Save your models here.|
|results|Save your experiment results.|
|src|Save your codes.|
|src/lib|Save your codes of library.|

Here is description some files created automatically.

|name|description|
|:---:|:---:|
|README.md|You should know.|
|kproject.json|Automatically use with ```run``` command|
|src/main.py|You should write main codes here.|
|src/lib/args.py|This file says code of argument parser.|

Next, you use ```run``` command. Automatically run ```src/main.py``` with configuration of ```kproject.json```. Now, you implicitly used ```kprojec.json```, so let's see more in detail. Here is content of initial ```krpoject.json```. You can easy to see some keys.

```
{
    "experiments": [
        {
            "cmd": "./src/main.py",
            "exec?": true
        }
    ]
}	
```

### Useful kproject library

kproject has some useful library. Here is useful library I think.

#### About argument parser

Already template argument parser has implemented by ```argparse``` in ```src/lib/args.py```. So you can easy to add some options. Then this file defined ```CONFIG```.

```
from lib.args import CONFIG
print(CONFIG['title'])
```

#### About logging

Some logging class has already defined.

```
from kproject.log import MDLog
from kproject.utils import *
log = MDLog("experiment1") #=> create /result/experiment1.md
log.start()
log.info("some information")
log.info(h2("experiment 1-1")) #=> ## experiment 1-1
log.finish()
```

## Install

```
$ pip install git+https://bitbucket.org/encry1024/kproject
```
