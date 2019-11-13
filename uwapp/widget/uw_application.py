# -*- coding: utf-8 -*
import urwid
from uwapp.widget.uw_menu_button import UWMenuButton
from uwapp.widget.uw_menu_bar import UWMenuBar

import uwapp.util.logging as logging

logger = logging.getLogger(__name__)

class UWApplication(urwid.Frame):

    def __init__(self, menuClass):
        fill = urwid.WidgetPlaceholder(
            #urwid.SolidFill(u' ')
            urwid.AttrMap(
                urwid.SolidFill(u'░'),
                'background'
            )
        )
        super(UWApplication, self).__init__(fill) # u'▒' u'░'
        self.menuInstances = None
        self.menuBar = None
        self.fill = fill
        self.fillOriginalWidget = fill.original_widget
        self.currMenuId = -1
        
        self.register_menu(menuClass)
        self.set_focus_path(['header', 0])

    def clear_popup(self):
        self.fill.original_widget = self.fillOriginalWidget
        self.set_focus_path(['header',0])
        
    def clear_menu(self):
        if self.currMenuId != -1:
            originMenu = self.menuInstances[self.currMenuId]
            #while originMenu.level > 0:
            #    self.fill.original_widget = self.fill.original_widget[0]
            #    originMenu.level -= 1
            self.fill.original_widget = self.fillOriginalWidget
            originMenu.level = 0
            self.currMenuId = -1
        self.set_focus_path(['header',0])
        #.set_focus()

            
    def register_menu(self, menuClass):
        self.menuInstances = []
        self.menuData = menuClass.menus
        self.menuClass = menuClass
        self.currMenuId = -1

        header = []
        startPosition = 0
        for i in range(len(self.menuData)):
            menuBarItem = self.menuData[i]
            mm = self.menuClass(self, menuBarItem)
            self.menuInstances.append(mm)
            
            button = UWMenuButton(menuBarItem["title"])
            
            header.append(button)
            def callback(button, menuId):
                if menuId == self.currMenuId:
                    return
                else:
                    self.clear_menu()
                    size = self.menuInstances[menuId]._get_menu_size(self.menuData[menuId]["subMenu"])
                    self.currMenuId = menuId
                    self.show_menu(self.menuInstances[menuId].instance, size[0], size[1])
            urwid.connect_signal(button, 'click', callback, user_arg = i)
            mm.startPosition = startPosition
            startPosition += 4 + len(menuBarItem["title"])
            
        #@self.menuCallbacks.append(callback)
        self.set_header(urwid.AttrMap(UWMenuBar(header),'menubar'))
            

    def show_menu(self, box, width, height, vertOff=0, horizOff=0):
        #self.set_focus('body')
        self.fill.original_widget = urwid.Overlay(
            urwid.AttrMap(urwid.LineBox(box), 'menu'),
            self.fill.original_widget,
            align='left', width=('relative', width),
            valign='top', height=('relative', height),
            min_width=width,
            min_height=height,
            left=self.menuInstances[self.currMenuId].startPosition+self.menuInstances[self.currMenuId].level*2 +horizOff,
            right = self.menuInstances[self.currMenuId].startPosition+self.menuInstances[self.currMenuId].level*2+horizOff,
            top=self.menuInstances[self.currMenuId].level*1+vertOff, #self.menuInstances.level ,
            bottom = self.menuInstances[self.currMenuId].level*1+height+vertOff # + height
        )
        self.menuInstances[self.currMenuId].level += 1
        self.set_focus_path(['body',1,0])


    def keypress(self, size, key):
        if key == 'esc' and self.menuInstances[self.currMenuId].level > 0:
            self.fill.original_widget = self.fillOriginalWidget
            self.menuInstances[self.currMenuId].level -= 1
            if self.menuInstances[self.currMenuId].level == 0:
                self.set_focus_path(['header',0])
        else:
            return super(UWApplication, self).keypress(size, key)