from libqtile.config import Key, Screen, Group
from libqtile.command import lazy
from libqtile import layout, bar, widget
from libqtile import hook

mod = "mod4"
alt = "mod1"

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
    Key([mod], "space", lazy.nextlayout()),

    Key([mod], "r", lazy.spawncmd()),
    Key([mod], "x", lazy.spawn("xchat")),
    Key([mod], "w", lazy.spawn("firefox")),
    Key([mod], "Return", lazy.spawn("tilda")),
    Key([mod], "l", lazy.spqwn("libreoffice")),
    Key([mod], "f", lazy.spawn("pcmanfm")),
    Key([mod], "s", lazy.spawn("skype")),
    Key([mod], "e", lazy.spawn("eclipse")),
    Key([mod], "g", lazy.spawn("gimp")),

    # alt
    Key([alt], "t", lazy.window.toggle_floating()),
    Key([alt], "w", lazy.window.kill()),
    Key([alt], "r", lazy.restart()),
    Key([alt], "q", lazy.shutdown()),
    Key([alt], "l", lazy.spawn("i3lock")),
    Key([alt], "F10", lazy.spawn("scrot -b -d 1 '%Y:%m:%d:%H:%M:%S.png' -e 'mv $f ~/Pictures/sshot'")),
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
    Group("9")
]

for i in groups:
    # mod1 + letter of group = switch to group
    keys.append(
        Key([mod], i.name, lazy.group[i.name].toscreen())
    )

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
    )

keys.append(Key([mod, "control"], "Right", lazy.screen.nextgroup()))
keys.append(Key([mod, "control"], "Left", lazy.screen.prevgroup()))


dgroups_key_binder = None
dgroups_app_rules = []

layouts = [
    layout.Max(),
    layout.TreeTab(),
    layout.Stack(num_stacks=2)
]

widget_defaults = dict(
    font='Arial',
    fontsize=16,
    padding=3,
)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                # widget.TextBox("default config", name="default"),
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
wmname = "qtile"


@hook.subscribe.client_new
def dialogs(window):
    if(window.window.get_wm_type() == 'dialog' or window.window.get_wm_transient_for()):
        window.floating = True
