# -*- coding: utf-8 -*-
from __init__ import *

setup(
    name=name,
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    license=license,
    entry_points={  
        'console_scripts': 'kproject = bin:main.main'  
    },
)
