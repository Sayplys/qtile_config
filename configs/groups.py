from libqtile.config import Group, Match

_groups = [
    Group(name="term",
          matches=[Match(wm_class="kitty")],
          spawn=["kitty"],
          layout="tile"),
    Group(name="web",
          matches=[Match(wm_class="firefox")],
          spawn=["firefox"],
          layout="max",),
    Group(name="media",
          matches=[Match(wm_class="spotify-launcher")],
          spawn=["spotify-launcher"],
          layout="max"),
    Group(name="programação",
          matches=[Match(wm_class="kitty")],
          spawn=["kitty"],
          layout="max",),
    Group("docs"),
    Group("extra"),
]


def set_groups():
    return _groups
