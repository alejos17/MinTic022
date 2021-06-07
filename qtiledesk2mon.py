import os

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Screen, Match
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
myTerm = "alacritty"                                    # My terminal of choice
myConfig = "/home/alejos17/.config/qtile/config.py"    # The Qtile config file location
terminal = guess_terminal()
color = "#136334"
color_light = "#20854a"
color_light2 = "#2dba68"
back = "#222222"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(), desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(), desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.run_extension(extension.DmenuRun(
        dmenu_prompt="Ejecuta",
        dmenu_font="Cantarell-18",
        background=back,
        foreground=color_light,
        selected_background=color,
        selected_foregorund="#ddd",
        ))),
    Key([mod], "l", lazy.layout.grow()),
    Key([mod], "h", lazy.layout.shrink()),
    Key([mod], "f", lazy.window.toggle_floating()),

    # Audio
    Key([], "XF86AudioMute", lazy.spawn("amixer -q -D pulse sset Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl -- set-sink-volume 0 -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl -- set-sink-volume 0 +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xrandr --output eDP-1 --brightness 0.4")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("xrandr --output eDP-1 --brightness 0.8")),
    Key([], "XF86AudioMicMute", lazy.spawn("amixer set Capture toggle")),
#	Key([], "0x08f6", lazy.spawn(cmus-remote --pause)),

    Key([mod], "e", lazy.spawn("thunar")),
    Key([mod], "v", lazy.spawn("code")),
    Key([mod], "t", lazy.spawn("telegram-desktop")),
    Key([mod], "w", lazy.spawn("google-chrome")),
    Key([mod], "m", lazy.spawn("mousepad")),

]

__groups = {
    1: Group("TERMINAL", matches=[Match(wm_class=["alacritty"])]),
    2: Group("WWW", matches=[Match(wm_class=["google-chrome"])]),
    3: Group("DEV", matches=[Match(wm_class=["code"])]),
    4: Group("CHAT", matches=[Match(wm_class=["telegram-desktop"])]),
    5: Group("OTROS"),
}
groups = [__groups[i] for i in __groups]


def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1+shift+letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(get_group_key(i.name)),
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    # layout.Max(),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(
        border_normal="#1D2330",
        border_focus="#115E1E",
        border_width=2,
        single_border_width=0,
        margin=4,
        single_margin=0,
    ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Cantarell',
    fontsize=12,
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                # widget.CurrentLayout(),
                widget.GroupBox(
                    highlight_color=[color],
                    highlight_method="line",
                    spacing=0,
                    inactive=color_light2,
                    active=color,
                    block_highlight_text_color="#ffffff",
                    borderwidth=0,
                    padding=10
                ),
                #widget.Prompt(),
                widget.TextBox(text="|", foreground = color_light2),
                widget.WindowName(foreground="#999999"),
                widget.TextBox(text="|", foreground = color_light2),
                widget.CheckUpdates(
                    custom_command="sudo apt update",
                    background="555555",
                    update_interval=1800,
                    distro="LinuxLite",
                    colour_have_updates="00ff00",
                    colour_no_updates="ff5500",
                    display_format='Actualizaciones: {updates}',
                    padding=10,
                    execute="alacritty -e sudo apt upgrade",
                    restart_indicator="Restart!!"
                ),
                widget.TextBox(text="|", foreground = color_light2),
                widget.TextBox(text="Alejandro - Pantalla Ppal"),
                widget.TextBox(text="|", foreground = color_light2),
                widget.TextBox(text=" 🖬"),
                widget.Memory(),
                widget.TextBox(text="|", foreground = color_light2),
                widget.TextBox(text="🔊"),
                widget.Volume(),
                widget.TextBox(text="|", foreground = color_light2),
                widget.Clock(format='%A, %B %d-%m-%Y %H:%M:%S', padding=10),
                widget.TextBox(text="|", foreground = color_light2),
                widget.Systray(),
                widget.Sep(linewidth = 0, padding = 5),
                widget.QuickExit(
                    default_text="Salir",
                    foreground=color_light,
                    countdown_format="[ {} ]"
                ),
            ],
            22,
            background="#222222",
            opacity=1
        ),
    ),

#Segunda pantalla para dos monitores
    Screen(
        top=bar.Bar(
            [
                # widget.CurrentLayout(),
                widget.GroupBox(
                    highlight_color=[color],
                    highlight_method="line",
                    spacing=0,
                    inactive=color_light2,
                    active=color,
                    block_highlight_text_color="#ffffff",
                    borderwidth=0,
                    padding=10
                ),
                #widget.Prompt(),
                widget.WindowName(foreground="#999999"),
                widget.TextBox(text="|", foreground = color_light2),
                widget.TextBox(text="Alejandro - Pantalla 2"),
                widget.TextBox(text="|", foreground = color_light2),
                widget.TextBox(text="🔊"),
                widget.Volume(),
                widget.TextBox(text="|", foreground = color_light2),
                widget.Clock(format='%H:%M:%S', padding=10),
                widget.TextBox(text="|", foreground = color_light2),
                widget.Sep(linewidth = 0, padding = 5),
            ],
            22,
            background="#222222",
            opacity=1
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

autostart = [
	"feh --bg-fill /home/alejos17/Pictures/gato.png",
	"picom -b",
	"nm-applet &",   #comando para mostrar icono de redes en systemtray
]

for x in autostart:
	os.system(x)
