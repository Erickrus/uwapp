import urwid
from uwapp.widget.uw_menu import UWMenu
from uwapp.widget.uw_menu_button import UWMenuButton
from uwapp.widget.uw_menu_bar import UWMenuBar
import uwapp.util.logging as logging

logger = logging.getLogger(__name__)

menus = [{
    "title": u"File",
    "type": "menu",
    "subMenu": [
        {
            "title": u"Open",
            "type": "menuItem",
            "callback": None
        }, {
            "title": u"Save",
            "type": "menuItem",
            "callback": None
        }, {
            "title": u"Save As",
            "type": "menuItem",
            "callback": None
        },
        {
            "title": u"Recent",
            "type": "subMenu",
            "subMenu": [{
                    "title": u"uwapp.py",
                    "type": "menuItem",
                    "callback": None
                }, {
                    "title": u"uw_menu.py",
                    "type": "menuItem",
                    "callback": None
                },
            ]
        },
        {
            "title": "Exit",
            "type": "menuItem",
            "callback": "self.exit_program"
        }
    ]
}, {
    "title": u"Help",
    "type": "menu",
    "subMenu": [{
        "title": u"About",
        "type": "menuItem",
        "callback": "self.about"
    }]
    
}]


class MyMenu(UWMenu):
    def __init__(self, app, menuData):
        super(MyMenu, self).__init__(app, menuData)

    def exit_program(self, button):
        raise urwid.ExitMainLoop()

    def about(self, button):
        self.app.clear_menu()
        


        close_button = urwid.Button("      OK      ")
        urwid.connect_signal(close_button, 'click',
            lambda button: self.app.clear_popup())
        pile = urwid.Pile([
            urwid.Text("About"),
            urwid.Divider(u'─'),
            urwid.Text(
            "UWMenu 0.1\n"), close_button])
        fill = urwid.Filler(pile)
        
        

        self.app.fill.original_widget = urwid.Overlay(
            urwid.LineBox(
                urwid.Pile([
                    fill
                    #
                    ])
                
            ),
            self.app.fill.original_widget,
            align='center', width=('relative', 0),
            valign='middle', height=('relative', 0),
            min_width=20,
            min_height=8,
            left=0,
            right = 20,
            #right=(self.menuInstances.self.maxLevels - self.menuInstances.level - 1) * 3,
            top=5, #self.menuInstances.level ,
            #bottom=(self.maxLevels - self.menuInstances.level - 1) * 2
            bottom = 10 # + height
        )


class Application(urwid.Frame):

    def __init__(self):
        fill = urwid.WidgetPlaceholder(urwid.SolidFill(u' '))
        super(Application, self).__init__(fill) # u'▒'
        self.menuInstances = None
        self.menuBar = None
        self.fill = fill
        self.currMenuId = -1

    def clear_popup(self):
        self.fill.original_widget= self.fill.original_widget[0]
        
    def clear_menu(self):
        if self.currMenuId != -1:
            originMenu = self.menuInstances[self.currMenuId]
            while originMenu.level > 0:
                self.fill.original_widget = self.fill.original_widget[0]
                originMenu.level -= 1
            originMenu.level = 0
            self.currMenuId = -1
    def register_menu(self, menu):
        self.menuInstances = []
        self.menuData = menu
        self.currMenuId = -1

        header = []
        startPosition = 0
        for i in range(len(menu)):
            menuBarItem = menu[i]
            mm = MyMenu(self, menuBarItem)
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
        self.set_header(UWMenuBar(header))
            

    def show_menu(self, box, width, height, vertOff=0, horizOff=0):
        self.fill.original_widget = urwid.Overlay(
            urwid.LineBox(box),
            self.fill.original_widget,
            align='left', width=('relative', width),
            valign='top', height=('relative', height),
            min_width=width,
            min_height=height,
            left=self.menuInstances[self.currMenuId].startPosition+self.menuInstances[self.currMenuId].level*2 +horizOff,
            right = self.menuInstances[self.currMenuId].startPosition+self.menuInstances[self.currMenuId].level*2+horizOff,
            #right=(self.menuInstances.self.maxLevels - self.menuInstances.level - 1) * 3,
            top=self.menuInstances[self.currMenuId].level*1+vertOff, #self.menuInstances.level ,
            #bottom=(self.maxLevels - self.menuInstances.level - 1) * 2
            bottom = self.menuInstances[self.currMenuId].level*1+height+vertOff # + height
        )
        self.menuInstances[self.currMenuId].level += 1


    def keypress(self, size, key):
        if key == 'esc' and self.menuInstances[self.currMenuId].level > 0:
            self.fill.original_widget = self.fill.original_widget[0]
            self.menuInstances[self.currMenuId].level -= 1
        else:
            return super(Application, self).keypress(size, key)










app = Application()


app.register_menu(menus)


#size = fileMenu._get_menu_size(menus[0]["subMenu"])
#app.show_menu(fileMenu.instance, size[0], size[1])
urwid.MainLoop(app, palette=[
    ('reversed', 'standout', ''),
    ]).run()



