# Firefox Context Menu Customizer

A Python script to automatically install Firefox context menu customizations that hide unwanted menu items.

Reference: [stonecrusher/simpleMenuWizard: Hide contextmenu items in Firefox Photon](https://github.com/stonecrusher/simpleMenuWizard)

## Installation

### Prerequisites

- **Python 3.13+**
- **Firefox** (must be installed and run at least once to create a profile)

### Setup

If using Poetry:

```bash
poetry install
```

## Usage

### Automatic Installation (Recommended)

Run the Python script to automatically find your Firefox profile and install the customizations:

```bash
python src/firefox_menu/main.py
```

The script will:

- Automatically detect your OS and find the Firefox profile directory
- Create the `chrome` directory if it doesn't exist
- Copy the `userChrome.css` file to your Firefox profile
- Provide clear feedback and next steps

### Manual Installation

If you prefer to install manually:

1. **Find your Firefox profile directory**:
   - **macOS**: `~/Library/Application Support/Firefox/Profiles/`
   - **Windows**: `~/AppData/Roaming/Mozilla/Firefox/Profiles/`
   - **Linux**: `~/.mozilla/firefox/`

2. **Locate your default profile** (usually ends with `.default-release`).

3. **Create a `chrome` directory** in your profile folder.

4. **Copy `src/firefox_menu/userChrome.css`** to `chrome/userChrome.css` in your profile.

## Configuration

You need to set the following configuration values in `about:config` in order for the changes to work:

- `toolkit.legacyUserProfileCustomizations.stylesheets` = `true`
- `widget.macos.native-context-menus` = `false` (only needed on macOS)

Then restart Firefox after running the script.

## What It Does

The script removes clutter from Firefox's context menus, including:

- Tab management options (close, move, select all, etc. - meant to be used with extensions like [Close Tabs to the Right](https://addons.mozilla.org/en-US/firefox/addon/close-tabs-right/))
- Bookmark options
- Accessibility inspection
- Link preview
- Image sharing
- Background setting
- Translation options

## Cross-Platform Support

The script automatically detects your operating system and finds the correct Firefox profile location:

- **macOS**: `~/Library/Application Support/Firefox/Profiles/`
- **Windows**: `~/AppData/Roaming/Mozilla/Firefox/Profiles/`
- **Linux**: `~/.mozilla/firefox/`

## Troubleshooting

- **"Firefox profiles directory not found"**: Ensure Firefox is installed and has been run at least once.
- **"No default Firefox profile found"**: Check `about:profiles` in Firefox to see your profile directory.
- **Changes not taking effect**: Make sure you've set the `about:config` preferences and restarted Firefox.
