from libqtile.config import Group, Match

_groups = [
    Group(name="term",
          spawn=["kitty"],
          layout="tile"),
    Group(name="web",
          matches=[Match(wm_class="firefox")],
          spawn=["firefox"],
          layout="max",),
    Group(name="media",
          matches=[Match(wm_class="spotify")],
          spawn=["spotify"],
          layout="max"),
    Group(name="programação",
          spawn=["kitty"],
          layout="max",),
    Group(name="comms",
          spawn=["discord"],
          layout="max"),
    Group("docs"),
    Group("extra"),
]


def set_groups():
    return _groups
