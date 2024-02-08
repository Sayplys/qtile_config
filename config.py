from configs import set_keys, set_groups, set_screens, set_layouts
from libqtile import hook 
import os, subprocess


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


groups = set_groups()
screens = set_screens()
keys = set_keys()
layouts = set_layouts()

follow_mouse_focus = True
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

wmname = "LG3D"
