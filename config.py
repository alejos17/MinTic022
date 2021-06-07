from typing import List  # noqa: F401
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
import os
import subprocess

mod = "mod4"
terminal = "kitty"
terminalapp ="kitty -e "

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/startup_once.sh')
    subprocess.call([home])
@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/startup.sh')
    subprocess.call([home])

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
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
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

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
    #Key([mod], "r", lazy.spawn(terminalapp + "ranger")),
    #Key([mod], "s", lazy.spawn("passmenu")),
    #Key([mod], "n", lazy.spawn(terminalapp + "newsboat")),
    Key([mod], "w", lazy.spawn("google-chrome")),
    #Key([mod, "shift"], "w", lazy.spawn(terminalapp + "amfora")),
    #Key([mod], "m", lazy.spawn(terminalapp + "neomutt")),
    #Key([mod, "shift"], "m", lazy.spawn("thunderbird")),
    # Key([mod], "", lazy.spawn(""), desc=""),
]

group_names = [("✎", {'layout': 'columns'}),
               ("❞", {'layout': 'columns'}),
               ("✺", {'layout': 'columns'}),
               ("✀", {'layout': 'columns'}),
               ("❏", {'layout': 'columns'}),
               ("♫", {'layout': 'floating'}),
               ("⛕", {'layout': 'columns'}),
               ("☎", {'layout': 'columns'}),
               ("☊", {'layout': 'columns'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name, switch_group=True))) # Send current window to another group

colors = [
    "#1E1F29", # darker purple 
    "#bfbfbf", # white
    "#bd93f9", # lighter purple
    "#ff92d0", # pink
    "#50fa7b", # green 
    "#ff6e67", # red
	"#3A2F4D", # grey
]

layouts = [
    layout.Columns(
        border_focus_stack=[1],
        border_focus=colors[2]
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    #layout.Stack(num_stacks=2),
    #layout.Bsp(),
    #layout.Matrix(),
    #layout.MonadTall(),
    #layout.MonadWide(),
    #layout.RatioTile(),
    #layout.Tile(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

widget_defaults = dict(
    font='Ubuntu',
    fontsize=28,
    padding=5,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    font = "Ubuntu",
                    fontsize = 28,
                    margin_y = 3,
                    margin_x = 0,
                    padding_y = 5,
                    padding_x = 3,
                    borderwidth = 3,
                    rounded = False,
                    highlight_method = "line",
                    this_current_screen_border = colors[4],
                    active = colors[3],
                    inactive = colors[2],
                ),
                widget.Spacer(
                    length=15
                ),
		widget.Cmus(
                    font='Ubuntu Mono',
                    play_color=colors[4],
                    noplay_color=colors[2],
                    max_chars=45,
                ),
                widget.Spacer(),
                widget.Clock(
                    format="%H:%M - %a, %d %b",
                    font="Accanthis ADF Std",
                    fontsize="32",
                    foreground=colors[1],
		),
                widget.Spacer(),
                widget.CurrentLayout(
                    fontsize=26,
                    font="Linux Libertine",
                    foreground=colors[3],
		),
		widget.BitcoinTicker(
					fontsize=22,
					font="Mononoki",
					foreground=colors[1],
					currency="EUR"
				),
		widget.Spacer(
                    length=15
                ),
		widget.TextBox(
                    fontsize=28,
                    foreground=colors[2],
                    text = "🎚️",
                    padding = 0
                ),
		widget.PulseVolume(
                    font="Linux Libertine",
                    fontsize=26,
                    foreground=colors[4]
		),
		widget.Spacer(
                    length=15
                ),
		widget.TextBox(
                    fontsize=26,
                    text = "⚡",
                    foreground=colors[2],
                    padding = 0
                ),
		widget.Battery(
                    battery=0+1,
                    discharge_char='...',
                    font="Linux Libertine",
                    fontsize=24,
                    foreground=colors[4],
                    format="{percent:2.0%} {char}",
		),
		widget.Spacer(
                    length=15
                ),
                widget.TextBox(
                    fontsize=28,
                    text = "🕸️",
                    foreground=colors[2],
                    padding = 0
                ),
                widget.Wlan(
                    font="Linux Libertine",
                    fontsize=30,
                    interface="wlp4s0",
                    format="{essid}",
                    foreground=colors[3],
                    disconnected_message="offline"
		),
                widget.Wlan(
                    font="Linux Libertine",
                    interface="wlp4s0",
                    fontsize=26,
                    format="{percent:2.0%}",
                    foreground=colors[4],
		),
		widget.Spacer(
                    length=2
                ),
                widget.Systray(),
		widget.Spacer(
                    length=10
                ),
                widget.QuickExit(
                    fontsize=30,
                    foreground=colors[5],
                    countdown_start=4,
                    countdown_format='{}',
                    default_text="🐧"),
                widget.Spacer(
                    length=2
                ),
            ],
            39,
            background=colors[0],
			opacity=0.75,
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

wmname = "LG3D"

# Qtile startup commands, not repeated at qtile restart
#@hook.subscribe.startup_once
#def autostart():
#    from datetime import datetime
#    try:
#        subprocess.call([home + '/.config/qtile/autostart.sh'])
#    except Exception as e:
#        with open('qtile_log', 'a+') as f:
#            f.write(
#                datetime.now().strftime('%Y-%m-%dT%H:%M') +
#                + ' ' + str(e) + '\n')