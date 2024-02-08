from libqtile.config import Group, Match

_groups = [
    Group(name="term",
          matches=[Match(wm_class="alacritty")],
          spawn=["alacritty"],
          layout="tile"),
    Group(name="web",
          matches=[Match(wm_class="firefox")],
          spawn=["firefox"],
          layout="max",),
    Group(name="messages",
          matches=[Match(wm_class="whatsapp-for-linux")],
          spawn=["whatsapp-for-linux"],
          layout="max",),
    Group(name="media",
          matches=[Match(wm_class="spotify")],
          spawn=["spotify"],
          layout="max"),
    Group("docs"),
    Group("extra"),
]


def set_groups():
    return _groups
