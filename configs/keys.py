from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from .groups import _groups
from .screen import _screens

mod = "mod4"
terminal = "kitty"


_keys = [
    Key([mod], "Return", lazy.spawn(terminal)),

    # system functionalities
    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control", "shift"], "r", lazy.restart()),
    Key([mod, "control", "shift"], "q", lazy.shutdown()),
    Key([mod, "control"], "c", lazy.spawncmd()),
    Key([mod,"control"], "Tab", lazy.widget["keyboardlayout"].next_keyboard()),
    Key([mod, "control"], "d", lazy.widget["volume"].decrease_vol()),
    Key([mod, "control"], "a", lazy.widget["volume"].increase_vol()),
    Key([mod], "p", lazy.spawn("flameshot gui")),

    # screen
    Key([mod, "mod1"], "l", lazy.next_screen()),
    Key([mod, "mod1"], "j", lazy.prev_screen()),

    # group functionalities
    Key([mod, "shift"], "l", lazy.screen.next_group()),
    Key([mod, "shift"], "j", lazy.screen.prev_group()),
    Key([mod, "shift"], "c", lazy.togroup()),

    # layout functionalities
    Key([mod, "mod1"], "n", lazy.next_layout()),
    Key([mod, "mod1"], "p", lazy.prev_layout()),

    # window functionalities
    Key(["mod1"], "F4", lazy.window.kill()),
    Key(["mod1"], "Tab", lazy.layout.next()),
    Key(["mod1", "shift"], "Tab", lazy.layout.previous()),
    Key(["mod1"], "j", lazy.layout.shuffle_up()),
    Key(["mod1"], "l", lazy.layout.shuffle_down()),
]

for i in range(len(_groups)):
    _keys.extend([Key([mod, "mod1"], f"{i + 1}", lazy.group[_groups[i].name].toscreen(screen=k, toggle=True)) for k in _screens])
    _keys.extend(
        [
            Key([mod, "mod1"], f"{i + 1}", lazy.group[_groups[i].name].toscreen(screen=0, toggle=True)),
            Key([mod, "mod1", "shift"], f"{i + 1}", lazy.group[_groups[i].name].toscreen(screen=1, toggle=True)),
            Key(["mod1"], f"{i + 1}", lazy.window.togroup(_groups[i].name, switch_group=True),),
            Key([mod, "shift"], f"{i + 1}", lazy.screen.toggle_group(_groups[i].name))
        ]
    )


def set_keys():
    return _keys
