from libqtile import layout

margin = 2
border_focus = "#ff2121"

_layouts = [
    layout.RatioTile(
        margin=margin,
        border_focus=border_focus,
    ),
    layout.Tile(
        margin=margin,
        border_focus=border_focus,
    ),
    layout.Max(),
]


def set_layouts():
    return _layouts
