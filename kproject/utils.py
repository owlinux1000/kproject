import os

def get_model(fname):
    path = "model/{}".format(fname)
    if os.path.exists(path):
        return path
    return None

def save_model(fname):
    path = "model/{}".format(fname)
    if os.path.exists(path):
        return None
    return path

def get_dataset(fname):
    path = "dataset/{}".format(fname)
    if os.path.exists(path):
        return path
    return None

def save_dataset(fname):
    path = "dataset/{}".format(fname)
    if os.path.exists(path):
        return None
    return path

def get_result(fname):
    path = "result/{}".format(fname)
    if os.path.exists(path):
        return path
    return None

def save_result(fname):
    path = "result/{}".format(fname)
    if os.path.exists(path):
        return None
    return path
