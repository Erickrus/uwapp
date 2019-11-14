# -*- coding: utf-8 -*
import urwid
from uwapp.my_menu import MyMenu
from uwapp.widget.uw_application import UWApplication
from uwapp.widget.uw_theme import UWTheme
from uwapp.preference_dialog import PreferenceDialog

import uwapp.util.logging as logging

logger = logging.getLogger(__name__)

class Application(UWApplication):
    def __init__(self, menuClass):
        super(Application, self).__init__(menuClass)


if __name__ == "__main__":
    while True:
        try:
            preference = PreferenceDialog.load_preference()
            app = Application(MyMenu)
            urwid.MainLoop(app, palette=UWTheme.get_theme(preference["theme"])).run()
            break
        except Exception as e:
            logger.info(str(e.args))
            if str(e.args).find("restart") > 0:
                continue
            else:
                raise Exception(e)
        


