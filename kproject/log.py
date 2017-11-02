import sys
from abc import ABCMeta, abstractmethod
from kproject.utils import *

class KprojectLog(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, fname = None):
        pass

    @abstractmethod
    def start(self, msg = ''):
        pass

    @abstractmethod
    def info(self, msg = ''):
        pass

    @abstractmethod
    def finish(self, msg = ''):
        pass
    
class TxtLog(KprojectLog):
    
    def __init__(self, fname = None):
        if fname is None:
            self.f = sys.stdout
        else:
            self.path = "result/{}.txt".format(fname)
            try:
                self.f = open(self.path, 'w')
            except:
                error("Could not open `{}`".format(self.path))
                sys.exit(1)

        if fname is None:
            print("Result\n", file=self.f)
        else:
            print("{}\n".format(fname), file=self.f)
        
    def start(self, msg = ''):
        print("[ START  ] {} {} {}".format(now_str(), ' '.join(sys.argv), msg), file=self.f)

    def info(self, msg = ''):
        print("[ INFO   ] {} {}".format(now_str(), msg), file=self.f)

    def finish(self, msg = ''):
        print("[ FINISH ] {} {}".format(now_str(), msg), file=self.f)
        self.f.close()

class MDLog(KprojectLog):

    def __init__(self, fname):
        
        self.path = "./result/{}.md".format(fname)
        
        try:
            self.f = open(self.path, 'w')

        except:
            error("Could not open `{}`".format(self.path))
            sys.exit(1)
            
        print(h1(fname+"\n"), file=self.f)
    
    def start(self, msg = ' '):
        _msg = "[ {} ] {} {} {}".format(
            bold("START"),
            now_str(),
            ' '.join(sys.argv),
            msg
        )
        print(_msg, file=self.f)

    def info(self, msg = ' '):
        _msg = "[ {} ] {} {}".format(
            bold("INFO"),
            now_str(),
            msg
        )
        print(_msg, file=self.f)

    def finish(self, msg = ' '):
        _msg = "[ {} ] {} {}".format(
            bold("FINISH"),
            now_str(),
            msg
        )
        print(_msg, file=self.f)
        try:
            self.f.close()
        except:
            error("Could not close `{}`").format(self.path)
