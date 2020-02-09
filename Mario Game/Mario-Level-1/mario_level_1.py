#!/usr/bin/env python


"""
This is an attempt to recreate the first level of
Super Mario Bros for the with a twist.
"""

import sys
import pygame as pg
from data.main import main
import cProfile


if __name__=='__main__':
    main()
    pg.quit()
    sys.exit()
