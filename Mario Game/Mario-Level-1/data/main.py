__author__ = 'justinarmstrong'

from . import setup,tools
from .states import main_menu,load_screen,load_screen2,level1,level2
from . import constants as c


def main():
    """Add states to control here."""
    run_it = tools.Control(setup.ORIGINAL_CAPTION)
    state_dict = {c.MAIN_MENU: main_menu.Menu(),
                  c.LOAD_SCREEN: load_screen.LoadScreen(),
                  c.LOAD_SCREEN2: load_screen2.LoadScreen2(),
                  c.TIME_OUT: load_screen.TimeOut(),
                  c.GAME_OVER: load_screen.GameOver(),
                  c.LEVEL1: level1.Level1(),
                  c.LEVEL2: level2.Level2()}

    run_it.setup_states(state_dict, c.MAIN_MENU)
    run_it.main()



