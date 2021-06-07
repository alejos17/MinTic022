import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401

##### DEFINING SOME VARIABLES #####
mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"                                    # My terminal of choice
myConfig = "/home/alejos17/.config/qtile/config.py"    # The Qtile config file location

##### KEYBINDINGS #####
keys = [
    # Cambiar entre Ventanas
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Mover ventanas entre izq / der o mover arriba / abajo en el stack.
    # Se se mueve fuera del rango se crea otra columna
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "a", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Audio
    Key([], "XF86AudioMute", lazy.spawn("amixer -q -D pulse sset Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl -- set-sink-volume 0 -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl -- set-sink-volume 0 +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xrandr --output eDP-1 --brightness 0.4")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("xrandr --output eDP-1 --brightness 0.8")),
    Key([], "XF86AudioMicMute", lazy.spawn("amixer set Capture toggle")),
#	Key([], "0x08f6", lazy.spawn(cmus-remote --pause)),

    # own shortcuts
    Key([mod, "shift"], "z", lazy.spawn("slock")),
    Key([mod, "shift"], "Return", lazy.spawn("rofi -show drun")),
    Key([mod], "Tab", lazy.spawn("rofi -show window -font 'mononoki 30'")),
    Key(["mod1"], "Tab", lazy.spawn("rofi -show windowcd -font 'mononoki 30'")),
    Key([mod, "shift"], "s", lazy.spawn("rofi -show ssh")),
    Key([mod], "d", lazy.spawn("dmenu_run -nb '#1e1f29' -sf '#000000' -sb '#bd93f9' -fn 'Accanthis ADF Std-15'")),

    Key([mod], "e", lazy.spawn("thunar")),
    Key([mod], "v", lazy.spawn("code")),
    Key([mod], "t", lazy.spawn("telegram-desktop")),
    #Key([mod], "r", lazy.spawn(terminalapp + "ranger")),
    Key([mod], "s", lazy.spawn("passmenu")),
    #Key([mod], "n", lazy.spawn(terminalapp + "newsboat")),
    Key([mod], "w", lazy.spawn("google-chrome")),
    #Key([mod, "shift"], "w", lazy.spawn(terminalapp + "amfora")),
    #Key([mod], "m", lazy.spawn(terminalapp + "neomutt")),
    #Key([mod, "shift"], "m", lazy.spawn("thunderbird")),
    # Key([mod], "", lazy.spawn(""), desc=""),
]

##### GROUPS #####
group_names = [("WWW", {'layout': 'monadtall'}),
               ("CONSOLE", {'layout': 'monadtall'}),
               ("RDP", {'layout': 'treetab'}),
               ("CODE", {'layout': 'monadtall'}),
               ("CHAT", {'layout': 'monadtall'}),
               ("MUS", {'layout': 'monadtall'}),
               ("FILES", {'layout': 'monadtall'}),
               ]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group
	

##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {"border_width": 2,
                "margin": 4,
                "border_focus": "AD69AF",
                "border_normal": "1D2330"
                }

##### THE LAYOUTS #####
layouts = [
    layout.Max(),
    layout.Stack(num_stacks=2),
	#layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    #layout.Max(**layout_theme),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND"],
         section_fontsize = 11,
         bg_color = "141414",
         active_bg = "90C435",
         active_fg = "000000",
         inactive_bg = "384323",
         inactive_fg = "a0a0a0",
         padding_y = 5,
         section_top = 10,
         panel_width = 320
         ),
     layout.Floating(**layout_theme)
]

##### COLORS #####
colors = [["#282a36", "#282a36"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # background color for layout widget
          ["#A77AC4", "#A77AC4"], # dark green gradiant for other screen tabs
          ["#7197E7", "#7197E7"]] # background color for pacman widget

##### PROMPT #####
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
	
##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize = 12,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

##### WIDGETS #####

def init_widgets_list():
    widgets_list = [
               widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.GroupBox(font="Ubuntu Bold",
                        fontsize = 9,
                        margin_y = 0,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 1,
                        active = colors[2],
                        inactive = colors[2],
                        rounded = False,
                        highlight_method = "block",
                        this_current_screen_border = colors[4],
                        this_screen_border = colors [1],
                        other_current_screen_border = colors[0],
                        other_screen_border = colors[0],
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.Prompt(
                        prompt=prompt,
                        font="Ubuntu Mono",
                        padding=10,
                        foreground = colors[3],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.WindowName(
                        foreground = colors[4],
                        background = colors[0],
                        padding = 5
                        ),
               widget.TextBox(
                        text=" 🖬",
                        foreground=colors[2],
                        background=colors[5],
                        padding = 0,
                        fontsize=14
                        ),
               widget.Memory(
                        foreground = colors[2],
                        background = colors[5],
                        padding = 5
                        ),
               widget.TextBox(
                        text='|',
                        background = colors[2],
                        foreground = colors[5],
                        padding=0,
                        fontsize=14
                        ),
               widget.TextBox(
                        text=" ↯",
                        foreground=colors[2],
                        background=colors[5],
                        padding = 0,
                        fontsize=14
                        ),
               widget.Net(
                        interface = "enp1s0",
                        foreground = colors[2],
                        background = colors[5],
                        padding = 5
                        ),
               widget.TextBox(
                        text='|',
                        background = colors[2],
                        foreground = colors[5],
                        padding=0,
                        fontsize=14
                        ),
               widget.TextBox(
                        text=" 🔊",
                        foreground=colors[2],
                        background=colors[5],
                        padding = 0,
                        fontsize=14
                        ),
               widget.Volume(
                        foreground = colors[2],
                        background = colors[5],
                        padding = 5
                        ),
		       widget.TextBox(
                        text='|',
                        background = colors[2],
                        foreground = colors[5],
                        padding=0,
                        fontsize=14
                        ),
               widget.TextBox(
                        fontsize=14,
                        text = "⚡",
                        foreground=colors[5],
                        padding = 0
                        ),
               widget.Battery(
                        battery=0+1,
                        discharge_char='...',
                        fontsize=14,
                        foreground=colors[5],
                        format="{percent:2.0%} {char}",
		                ),
               widget.TextBox(
                        text='|',
                        background = colors[2],
                        foreground = colors[5],
                        padding=0,
                        fontsize=14
                        ),
               widget.TextBox(
                        text='|',
                        background = colors[2],
                        foreground = colors[5],
                        padding=0,
                        fontsize=14
                        ),
               widget.TextBox(
                        fontsize=14,
                        text = "🕸️",
                        foreground=colors[5],
                        padding = 0
                        ),
                widget.Wlan(
                        fontsize=14,
                        interface="wlp4s0",
                        format="{essid}",
                        foreground=colors[5],
                        disconnected_message="offline"
		                ),
                widget.Wlan(
                        interface="wlp4s0",
                        fontsize=14,
                        format="{percent:2.0%}",
                        foreground=colors[5],
		                ),
               widget.TextBox(
                        text='|',
                        background = colors[2],
                        foreground = colors[5],
                        padding=0,
                        fontsize=14
                        ),
               widget.TextBox(
                        text=" ☵",
                        padding = 5,
                        foreground=colors[2],
                        background=colors[5],
                        fontsize=14
                        ),
               widget.CurrentLayout(
                        foreground = colors[2],
                        background = colors[5],
                        padding = 5
                        ),
               widget.TextBox(
                        text='|',
                        background = colors[2],
                        foreground = colors[5],
                        padding=0,
                        fontsize=14
                        ),
               widget.TextBox(
                        text=" 🕒",
                        foreground=colors[2],
                        background=colors[5],
                        padding = 5,
                        fontsize=14
                        ),
               widget.Clock(
                        foreground = colors[2],
                        background = colors[5],
                        format="%A, %B %d - %H:%M:%S"
                        ),
               widget.TextBox(
                        text='|',
                        background = colors[2],
                        foreground = colors[5],
                        padding=0,
                        fontsize=14
                        ),
               widget.QuickExit(
                        fontsize=14,
                        foreground=colors[5],
                        countdown_start=4,
                        countdown_format='{}',
                        default_text="🐧"
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 5,
                        foreground = colors[2],
                        background = colors[5]
                        ),
               widget.Systray(
                        background=colors[5],
                        padding = 5
                        ),
              ]
    return widgets_list

##### SCREENS ##### (TRIPLE MONITOR SETUP)

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1                       # Slicing removes unwanted widgets on Monitors 1,3

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                       # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.95, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=0.95, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.95, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

##### DRAG FLOATING WINDOWS #####
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

##### FLOATING WINDOWS #####
floating_layout = layout.Floating(float_rules=[
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

##### STARTUP APPLICATIONS #####
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"