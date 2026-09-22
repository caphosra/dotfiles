"""Definitions and checks for links managed by this repository."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class ManagedLink:
    label: str
    source: Path
    destination: Path
    target_is_directory: bool = False


def managed_links() -> tuple[ManagedLink, ...]:
    """Return the links managed for the current environment."""
    config_home_value = os.environ.get("XDG_CONFIG_HOME")
    config_home = (
        Path(config_home_value).expanduser()
        if config_home_value
        else Path.home() / ".config"
    )
    if not config_home.is_absolute():
        config_home = Path.home() / ".config"

    return (
        ManagedLink(
            label="Neovim configuration",
            source=REPOSITORY_ROOT / "nvim",
            destination=config_home / "nvim",
            target_is_directory=True,
        ),
        ManagedLink(
            label="tmux configuration",
            source=REPOSITORY_ROOT / "tmux" / ".tmux.conf",
            destination=Path.home() / ".tmux.conf",
        ),
    )


def destination_exists(link: ManagedLink) -> bool:
    """Return whether the destination exists, including as a broken symlink."""
    return link.destination.is_symlink() or link.destination.exists()


def points_to_source(link: ManagedLink) -> bool:
    """Return whether a link destination resolves to its managed source."""
    try:
        return (
            link.destination.is_symlink()
            and link.destination.resolve() == link.source.resolve()
        )
    except (OSError, RuntimeError):
        return False
