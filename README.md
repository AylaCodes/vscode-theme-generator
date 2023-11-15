# VS Code Theme Generator

A simple theme generator for VS Code using a simple template system with a
JSON-format color palette or optionally a Python class for deeper customization.

## Features
* No requirements (Pure Python 3.10+)
* Simple JSON color palette customization
* Optional in-depth customization via standard VS Code theme.json template + Python classes

## Using your built theme
Follow the steps 2, and 3 from "Create a new Color Theme"
[here](https://code.visualstudio.com/api/extension-guides/color-theme#create-a-new-color-theme),
selecting "Start fresh". Simply replace `<your>-color-theme.json`'s content with the output
from `build.py` which will by default be `output.json` (See `build.py --help`).

Once this is done, follow the instructions from "vsce"
[here](https://code.visualstudio.com/api/working-with-extensions/publishing-extension#vsce)
to install and run `vsce package` to create your .vsix extension. You can then install the
extension directly from VS Code using either the extensions menu
(Extenxions -> Three dots -> Install from VSIX) or using the command palette (CTRL+SHIFT+P)
option `Extensions: Install From VSIX...`

Once installed, you can select your color theme as you would any other, and you are free to
continue following the official guides to create a package and publish your theme on the
marketplace.

## Examples
![](https://i.imgur.com/Y3T9k1x.png)
![](https://i.imgur.com/oTChyyW.png)
