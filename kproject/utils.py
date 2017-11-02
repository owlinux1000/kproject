def colorize(msg, color = 'default'):
    
    d = {
        'default': 0,
        'red': 31,
        'green': 32,
        'yellow': 33,
        'blue': 34,
        'puple': 35,
        'cyan': 36,
    }
    
    return "\033[{}m{}\033[0m".format(d[color], msg)

def error(msg, color = 'red'):
    
    print("[ {} ] {}".format(colorize("ERROR", color), msg))

def info(msg, color = 'blue'):
    print("[ {} ] {}".format(colorize("INFO", color), msg))

def now_str():
    from datetime import datetime
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S")

def h1(msg):
        return "# {}".format(msg)

def h2(msg):
    return "## {}".format(msg)
    
def h3(msg):
    return "### {}".format(msg)
    
def h4(msg):
    return "#### {}".format(msg)
    
def h5(msg):
    return "##### {}".format(msg)
    
def h6(msg):
    return "###### {}".format(msg)
    
def italic(msg):
    return "*{}*".format(msg)

def bold(msg):
    return "**{}**".format(msg)
    
def hr(self):
    return "***"
