from libqtile.config import Key, Screen, Group
from libqtile.command import lazy
from libqtile import layout, bar, widget

mod = "mod4"

keys = [
    Key(
        [mod], "k",
        lazy.layout.down()
    ),
    Key(
        [mod], "j",
        lazy.layout.up()
    ),

    Key(
        [mod, "control"], "k",
        lazy.layout.shuffle_down()
    ),
    Key(
        [mod, "control"], "j",
        lazy.layout.shuffle_up()
    ),

    
    Key(
        [mod], "space",
        lazy.layout.next()
    ),


    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate()
    ),


    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split()
    ),
    Key([mod], "Return", lazy.spawn("xterm")),

    Key([mod], "h",      lazy.to_screen(1)),
    Key([mod], "l",      lazy.to_screen(0)),
    Key([mod,"control"], "Tab",    lazy.nextlayout()),
    Key([mod,"control"], "w",      lazy.window.kill()),
    Key([mod,"control"], "q",      lazy.shutdown()),
    Key([mod, "control",], "r", lazy.restart()),

    #programi
    Key([mod], "r"     , lazy.spawncmd()),
    Key([mod], "x"     , lazy.spawn("xchat")),
    Key([mod], "w"     , lazy.spawn("chromium-browser")),
    Key([mod], "Return", lazy.spawn("xfce4-terminal")),
    Key([mod], "f"     , lazy.spawn("pcmanfm")),
]

groups = [
    Group("1"),
    Group("2"),
    Group("3"),
    Group("4"),
    Group("5"),
    Group("6"),
    Group("7"),
    Group("8"),
    Group("9"),
]
for i in groups:
    keys.append(
        Key([mod], i.name, lazy.group[i.name].toscreen())
    )

    keys.append(
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
    )

dgroups_key_binder = None
dgroups_app_rules = []

layouts = [
    layout.Max(),
    layout.Stack(num_stacks=2)
]

widget_defaults = dict(
    font = 'Arial',
    fontsize = 12,
    padding = 3,
)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
            ],
            30,
        ),
    ),
]

main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
mouse = ()
auto_fullscreen = True
