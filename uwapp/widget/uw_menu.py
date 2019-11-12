# -*- coding: utf-8 -*
import urwid

from uwapp.widget.uw_menu_button import UWMenuButton
import uwapp.util.logging as logging

logger = logging.getLogger(__name__)

class UWMenu:

    def __init__(self, app, menuData):
        self.app = app
        self.instance = eval(self._parse_children(menuData))
        self.level = 0
        self.data = menuData




    def _get_menu_size(self, subMenu):
        width, height = 0, 0
        for subMenuItem in subMenu:
            height += 1
            currWidth = len(subMenuItem["title"])
            if "subMenu" in subMenuItem:
                currWidth += 4
            if  currWidth > width:
                width = currWidth
        return max(width+6, 10), max(height+2, 3)
    
    def _parse_children(self, menu, vertOff=1, horizOff=0):
        res = ""
        if menu["type"] == "menu":
            children = []
            if "subMenu" in menu:
                for i in range(len(menu["subMenu"])):
                    children.append(self._parse_children(menu["subMenu"][i], vertOff+i-1, 5+horizOff+len(menu["subMenu"][i]["title"])))
                size = self._get_menu_size(menu["subMenu"])
            children = "[%s]" % ",".join(children)
            res = "self.menu(\"%s\", %s, %d, %d)" % (menu["title"], children, size[0], size[1]) 
        elif menu["type"] == "subMenu":
            children = []
            if "subMenu" in menu:
                for i in range(len(menu["subMenu"])):
                    children.append(self._parse_children(menu["subMenu"][i], vertOff+i-1, 5+horizOff+len(menu["subMenu"][i]["title"])))
                size = self._get_menu_size(menu["subMenu"])
            children = "[%s]" % ",".join(children)
            res = "self.sub_menu(\"%s\", %s, %d, %d, %d, %d)" % (menu["title"], children, size[0], size[1], vertOff, horizOff)
            
        elif menu["type"] == "menuItem":
            res = "self.menu_button(\"%s\", %s)" % (menu["title"], menu["callback"])
        
        logger.info(str(res))
        return res


    def menu_button(self, caption, callback):
        button = UWMenuButton(caption)

        if callback != None:
            urwid.connect_signal(button, 'click', callback)
        return urwid.AttrMap(button, None, focus_map='reversed')

    def sub_menu(self, title, choices, width, height, vertOff, horizOff):
        # contents = self.menu(caption, choices)
        contents = self.menu("", choices, width, height)

        def open_menu(button):
            return self.app.show_menu(contents, width, height, vertOff, horizOff)

        return self.menu_button([title, u' ...'], open_menu)

    def menu(self, title, choices, width, height):
        #body = [urwid.Divider("-")]
        body = []
        body.extend(choices)
        return urwid.ListBox(urwid.SimpleFocusListWalker(body))
