import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

@dataclass
class Theme:
    """Base Theme - the default Lucky Theme (My personal color preference)

    Note: All colors are to be privided as strings instandard hex-format (i.e. #FFFFFF)

    Attributes:
        name: Name of the generated theme
        palette: Path of the given color palette file
        foreground: Primary text color
        foreground_darker: Darker primary text color
        background: Primary editor background
        background_darker: Secondary panel background
        accent_primary: Primary UI theme color
        accent_hover: Primary UI theme highlight color
        accent_secondary: Secondary UI theme color
        accent_tertiary: Tertiary UI theme color
        light_one: Lighter base color
        light_two: Darker base color
        primary_one: Primary theme token color
        primary_two: Primary theme token color shade
        secondary_one: Secondary theme token color
        secondary_two: Secondary theme token color shade
        tertiary_one: Tertiary theme token color
        tertiary_two: Tertiary theme token color shade
        issue: Issue/Error/Removed color
        warning: Warning/Changed color
        okay: Okay/Added color
    """

    # Meta
    name: str = "Theme"
    palette: Path = "themes/base_theme.json"

    # Base Colors
    foreground: str = "#F3F3F7"
    foreground_darker: str = "#D2D2E2"
    background: str = "#2F2F37"
    background_darker: str = "#26262C"
    accent_primary: str = "#A967CE"
    accent_hover: str = "#B490E0"
    accent_secondary: str = "#7A6ADD"
    accent_tertiary: str = "#D66FAD"

    # Token Colors
    light_one: str = "#ADB2C2"
    light_two: str = "#9090A0"
    primary_one: str = "#CF81D9"
    primary_two: str = "#B490E0"
    secondary_one: str = "#BBBBFF"
    secondary_two: str = "#A0D0F0"
    tertiary_one: str = "#B0E0FF"
    tertiary_two: str = "#B0D0FF"

    # Important Colors
    issue: str = "#FF7878"
    warning: str = "#FFA878"
    okay: str = "#78FFA8"

    def _load_json(self, json_file: Path) -> None:
        """Load theme palette from a provided JSON file

        Parameters:
            json_file: The chosen color palette JSON file
        """
        with open(json_file, "r") as file:
            values = json.load(file)

        for key, value in values.items():
            setattr(self, key, value)

    def build_theme(
        self, template: Path, file_out: Path, use_palette: Optional[bool] = True
    ) -> None:
        """Build theme from chosen `template` into `file_out`

        Warning: This will OVERWRITE any currently existing `file_out`!

        Parameters:
            template: Chosen JSON template file
            file_out: Output file to write resulting theme to
            use_palette: Whether or not to use a provided
        """
        if use_palette:
            self._load_json(self.palette)

        print(f"Building theme: {self.name}")

        with open(template, "r") as file:
            theme = json.load(file)

        theme["name"] = self.name

        theme["colors"] = {
            "activityBar.activeBorder": self.accent_primary,
            "activityBar.background": self.background_darker,
            "activityBar.border": self.accent_primary,
            "activityBar.foreground": self.foreground,
            "activityBar.inactiveForeground": self.foreground_darker,
            "activityBarBadge.background": self.accent_tertiary,
            "activityBarBadge.foreground": self.foreground,
            "badge.background": self.light_two,
            "badge.foreground": self.light_one,
            "button.background": self.accent_primary,
            "button.border": self.accent_primary,
            "button.foreground": self.foreground,
            "button.hoverBackground": self.accent_hover,
            "button.secondaryBackground": self.light_two,
            "button.secondaryForeground": self.foreground,
            "button.secondaryHoverBackground": self.light_two,
            "checkbox.background": self.background,
            "checkbox.border": self.accent_primary,
            "debugToolBar.background": self.background_darker,
            "debugToolBar.border": self.accent_primary,
            "descriptionForeground": self.foreground_darker,
            "dropdown.background": self.background,
            "dropdown.border": self.accent_primary,
            "dropdown.foreground": self.foreground,
            "dropdown.listBackground": self.background_darker,
            "editor.background": self.background,
            "editor.findMatchBackground": self.accent_tertiary,
            "editor.foreground": self.foreground,
            "editor.inactiveSelectionBackground": self.background,
            "editor.lineHighlightBorder": self.background,
            "editor.selectionHighlightBackground": self.secondary_one,
            "editorGroup.border": self.accent_primary,
            "editorGroupHeader.tabsBackground": self.background_darker,
            "editorGroupHeader.tabsBorder": self.background,
            "editorGutter.addedBackground": self.okay,
            "editorGutter.deletedBackground": self.issue,
            "editorGutter.modifiedBackground": self.warning,
            "editorIndentGuide.activeBackground1": self.foreground_darker,
            "editorIndentGuide.background1": self.background,
            "editorLineNumber.activeForeground": self.foreground,
            "editorLineNumber.foreground": self.foreground,
            "editorOverviewRuler.border": self.background_darker,
            "editorWidget.background": self.background_darker,
            "errorForeground": self.issue,
            "focusBorder": self.accent_primary,
            "foreground": self.foreground,
            "icon.foreground": self.foreground,
            "input.background": self.background,
            "input.border": self.accent_primary,
            "input.foreground": self.foreground,
            "input.placeholderForeground": self.foreground_darker,
            "inputOption.activeBackground": self.accent_secondary,
            "inputOption.activeBorder": self.accent_primary,
            "keybindingLabel.foreground": self.foreground,
            "list.activeSelectionIconForeground": self.foreground,
            "list.dropBackground": self.foreground_darker,
            "menu.background": self.background_darker,
            "menu.border": self.foreground_darker,
            "menu.foreground": self.foreground,
            "menu.separatorBackground": self.foreground_darker,
            "notificationCenterHeader.background": self.background_darker,
            "notificationCenterHeader.foreground": self.foreground,
            "notifications.background": self.background_darker,
            "notifications.border": self.background,
            "notifications.foreground": self.foreground,
            "panel.background": self.background_darker,
            "panel.border": self.accent_primary,
            "panelInput.border": self.background,
            "panelTitle.activeBorder": self.accent_primary,
            "panelTitle.activeForeground": self.foreground,
            "panelTitle.inactiveForeground": self.foreground_darker,
            "peekViewEditor.background": self.background_darker,
            "peekViewEditor.matchHighlightBackground": self.secondary_one,
            "peekViewResult.background": self.background_darker,
            "peekViewResult.matchHighlightBackground": self.secondary_one,
            "pickerGroup.border": self.accent_primary,
            "ports.iconRunningProcessForeground": self.accent_secondary,
            "progressBar.background": self.accent_primary,
            "quickInput.background": self.background_darker,
            "quickInput.foreground": self.foreground,
            "settings.dropdownBackground": self.background,
            "settings.dropdownBorder": self.accent_primary,
            "settings.headerForeground": self.foreground,
            "settings.modifiedItemIndicator": self.accent_tertiary,
            "sideBar.background": self.background_darker,
            "sideBar.border": self.background,
            "sideBar.foreground": self.foreground,
            "sideBarSectionHeader.background": self.background_darker,
            "sideBarSectionHeader.border": self.background,
            "sideBarSectionHeader.foreground": self.foreground,
            "sideBarTitle.foreground": self.foreground_darker,
            "statusBar.background": self.background_darker,
            "statusBar.border": self.accent_primary,
            "statusBar.debuggingBackground": self.accent_primary,
            "statusBar.debuggingForeground": self.foreground,
            "statusBar.focusBorder": self.accent_primary,
            "statusBar.foreground": self.foreground,
            "statusBar.noFolderBackground": self.background_darker,
            "statusBarItem.focusBorder": self.accent_primary,
            "statusBarItem.prominentBackground": self.foreground_darker,
            "statusBarItem.remoteBackground": self.accent_primary,
            "statusBarItem.remoteForeground": self.foreground,
            "tab.activeBackground": self.background,
            "tab.activeBorderTop": self.accent_primary,
            "tab.activeForeground": self.foreground,
            "tab.border": self.background,
            "tab.hoverBackground": self.background,
            "tab.inactiveBackground": self.background_darker,
            "tab.inactiveForeground": self.foreground_darker,
            "tab.lastPinnedBorder": self.accent_primary,
            "tab.unfocusedActiveBorder": self.background_darker,
            "tab.unfocusedActiveBorderTop": self.background,
            "tab.unfocusedHoverBackground": self.background_darker,
            "terminal.background": self.background,
            "terminal.border": self.accent_primary,
            "terminal.foreground": self.foreground,
            "terminal.inactiveSelectionBackground": self.background,
            "terminal.tab.activeBorder": self.accent_primary,
            "textBlockQuote.background": self.background,
            "textBlockQuote.border": self.accent_primary,
            "textCodeBlock.background": self.background,
            "textLink.activeForeground": self.accent_secondary,
            "textLink.foreground": self.accent_secondary,
            "textSeparator.foreground": self.background_darker,
            "titleBar.activeBackground": self.background,
            "titleBar.activeForeground": self.foreground,
            "titleBar.border": self.background,
            "titleBar.inactiveBackground": self.background_darker,
            "titleBar.inactiveForeground": self.foreground_darker,
            "welcomePage.progress.foreground": self.accent_primary,
            "welcomePage.tileBackground": self.background,
            "widget.border": self.accent_primary,
        }

        color_mapping = {
            "foreground": self.foreground,
            "foreground_darker": self.foreground_darker,
            "light_one": self.light_one,
            "light_two": self.light_two,
            "primary_one": self.primary_one,
            "primary_two": self.primary_two,
            "secondary_one": self.secondary_one,
            "secondary_two": self.secondary_two,
            "tertiary_one": self.tertiary_one,
            "tertiary_two": self.tertiary_two,
            "issue": self.issue,
            "warning": self.warning,
            "okay": self.okay,
        }

        for item in theme["tokenColors"]:
            token = item["name"]
            if token in color_mapping:
                item["settings"]["foreground"] = color_mapping[token]

        with open(file_out, "w") as file:
            json.dump(theme, file, indent=4)
