"""Uninstall the configuration symlinks."""

from __future__ import annotations

import sys

from ._links import destination_exists, managed_links, points_to_source


def main() -> int:
    links = managed_links()

    for link in links:
        if destination_exists(link) and not points_to_source(link):
            print(
                f"Refusing to remove unmanaged path: {link.destination}",
                file=sys.stderr,
            )
            return 1

    for link in links:
        if not destination_exists(link):
            print(f"{link.label} is not installed: {link.destination}")
            continue

        try:
            link.destination.unlink()
        except OSError as error:
            print(f"Could not remove {link.destination}: {error}", file=sys.stderr)
            return 1

        print(f"Removed {link.label} link: {link.destination}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
