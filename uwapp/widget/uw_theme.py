class UWTheme:
    turboVision = [
        ('dialog', 'white', 'light gray'),
        ('dialog.content', 'white', 'dark blue'),
        
        ('menubar', 'black', 'light gray'),
        ('menu', 'black', 'light gray'),
        ('button', 'black', 'light green'),
        ('background', 'dark blue', 'light gray'),
        ('reversed', 'standout', '')
    ]
    redHat = [
        ('dialog', 'black', 'light gray'),
        ('dialog.content', 'black', 'light gray'),
        
        ('menubar', 'black', 'light gray'),
        ('menu', 'black', 'light gray'),
        ('button', 'black', 'dark red'),
        ('background', 'dark blue', 'dark blue'),
        ('reversed', 'standout', '')
    ]
    console = [
        ('reversed', 'standout', '')
    ]
    @staticmethod
    def get_theme(themeName):
        if themeName == "turboVision":
            return UWTheme.turboVision
        elif themeName == "redHat":
            return UWTheme.redHat
        elif themeName == "console":
            return UWTheme.console
            