#!/usr/bin/env python3

"""This script finds the Firefox default profile and installs/updates the userChrome.css file to
the version included alongside this script, to customize the context menu by hiding unwanted items.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

from polykit import PolyLog

logger = PolyLog.get_logger(level="debug", simple=True)


def find_firefox_profile() -> Path | None:
    """Find the Firefox default profile directory.

    Returns:
        The path to the default profile directory, or None if not found.
    """
    # Firefox profiles are stored in different locations based on OS
    if sys.platform == "darwin":  # macOS
        profiles_dir = Path.home() / "Library/Application Support/Firefox/Profiles"
    elif sys.platform == "win32":  # Windows
        profiles_dir = Path.home() / "AppData/Roaming/Mozilla/Firefox/Profiles"
    else:  # Linux and others
        profiles_dir = Path.home() / ".mozilla/firefox"

    if not profiles_dir.exists():
        logger.error("Firefox profiles directory not found: %s", profiles_dir)
        return None

    # Look for the default profile (usually ends with .default-release)
    for profile_dir in profiles_dir.iterdir():
        if profile_dir.is_dir() and profile_dir.name.endswith(".default-release"):
            return profile_dir

    logger.error("No default Firefox profile found in: %s", profiles_dir)
    return None


def install_css(profile_dir: Path, source_css: Path) -> bool:
    """Install or update the userChrome.css file in the Firefox profile.

    Args:
        profile_dir: The path to the Firefox profile directory.
        source_css: The path to the source userChrome.css file.

    Returns:
        True if successful, False otherwise.
    """
    # Create chrome directory if it doesn't exist
    chrome_dir = profile_dir / "chrome"
    chrome_dir.mkdir(exist_ok=True)

    # Path for the target userChrome.css file
    target_css = chrome_dir / "userChrome.css"

    try:  # Copy the source file to the target location
        shutil.copy2(source_css, target_css)
        logger.debug("Successfully installed to: %s", target_css)
        return True
    except Exception as e:
        logger.error("Error installing userChrome.css: %s", e)
        return False


def main() -> None:
    """Main function to install the Firefox context menu customizations."""
    # Find the source userChrome.css file relative to the script
    script_dir = Path(__file__).parent
    source_css = script_dir / "userChrome.css"

    if not source_css.exists():
        logger.error("Error: userChrome.css not found at: %s", source_css)
        return

    # Find the Firefox profile
    profile_dir = find_firefox_profile()
    if not profile_dir:
        logger.error("Please ensure Firefox is installed and has been run at least once.")
        return

    logger.debug("Found Firefox profile: %s", profile_dir)

    # Install the userChrome.css file
    if install_css(profile_dir, source_css):
        logger.info("\nInstallation completed successfully!")
        logger.debug("\nMake sure you also set the necessary about:config values:")
        logger.debug("  - toolkit.legacyUserProfileCustomizations.stylesheets = true")
        logger.debug("  - widget.macos.native-context-menus = false")
        return

    logger.error("Installation failed!")


if __name__ == "__main__":
    main()
