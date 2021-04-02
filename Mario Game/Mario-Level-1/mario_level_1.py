#!/usr/bin/env python


"""
This is an attempt to recreate the first level of
Super Mario Bros for the with a twist.
To run in Linux right click and choose run in terminal
Another way to run is using this file in python and clicking run module: f5 key
"""

import sys
import pygame as pg
from data.main import main
import cProfile


if __name__=='__main__':
    main()
    pg.quit()
    sys.exit()
