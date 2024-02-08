from libqtile.config import Screen
from libqtile import bar, widget


_widgets = [widget.GroupBox(inactive="#808080", highlight_method='line', this_current_screen_border='#ff2121'), 
            widget.Spacer(),
            widget.Clock(),
            widget.Spacer(),
            widget.Volume(),
            widget.Notify(),
            widget.CurrentLayout(),
            widget.KeyboardLayout(configured_keyboards=["us", "br"]),
            widget.GmailChecker(
                username="pedrovinicyus@gmail.com", password="05020501"
            ), 
            widget.Memory(measure_mem='G'),
            widget.Net(format="{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}", 
                       width=90),
            ]

screenQtd = 2
_screens = []

def set_screens():
    for i in range(screenQtd):
        _bar = bar.Bar(widgets = _widgets, size = 30, background='#222222')
        screen = Screen(top = _bar)
        _screens.append(screen)
    return _screens
