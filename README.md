# i3-workspace-switch

A utility for the [i3](https://i3wm.org) tiling window manager, which assigns each output its own set of 10 workspaces
This effectively allows to switch workspaces on each output as if it was the only connected output

# Installation

```sh
python setup.py install
```

Or if you only want to install this utility to your home folder:
```sh
python setup.py install --user
```
Ensure that `~/.local/bin` is on your `PATH`.

# Configuration

In order to use this utility via shortcuts in i3, use something like this in your `~/.i3/config`:
```
# switch to workspace
bindsym $mod+1 exec i3-workspace-switch 1
bindsym $mod+2 exec i3-workspace-switch 2
bindsym $mod+3 exec i3-workspace-switch 3
bindsym $mod+4 exec i3-workspace-switch 4
bindsym $mod+5 exec i3-workspace-switch 5
bindsym $mod+6 exec i3-workspace-switch 6
bindsym $mod+7 exec i3-workspace-switch 7
bindsym $mod+8 exec i3-workspace-switch 8
bindsym $mod+9 exec i3-workspace-switch 9
bindsym $mod+0 exec i3-workspace-switch 10
```

# Usage

```
usage: i3-workspace-switch [-h] [-w OUTPUT] NUMBER

Utility for switching to unnumbered i3 workspaces using their relative
position.

positional arguments:
  NUMBER                Number of the workspace to focus. Starting with 1.

optional arguments:
  -h, --help            show this help message and exit
  -m, --move            move the current container instead of switching to it
```

# License

This library is [free software](https://en.wikipedia.org/wiki/Free_software); you can redistribute it and/or modify it under the terms of the [GNU Lesser General Public License](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License) as published by the [Free Software Foundation](https://en.wikipedia.org/wiki/Free_Software_Foundation); either version 3 of the License, or any later version. This work is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the [GNU Lesser General Public License](https://www.gnu.org/copyleft/lgpl.html) for more details.
