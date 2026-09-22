"""Install the configuration symlinks."""

from __future__ import annotations

import sys

from ._links import destination_exists, managed_links, points_to_source


def main() -> int:
    links = managed_links()

    for link in links:
        if not link.source.exists():
            print(f"Missing source path: {link.source}", file=sys.stderr)
            return 1
        if not points_to_source(link) and destination_exists(link):
            print(
                f"Refusing to replace existing path: {link.destination}",
                file=sys.stderr,
            )
            return 1

    for link in links:
        if points_to_source(link):
            print(
                f"{link.label} is already linked: {link.destination} -> {link.source}"
            )
            continue

        try:
            link.destination.parent.mkdir(parents=True, exist_ok=True)
            link.destination.symlink_to(
                link.source, target_is_directory=link.target_is_directory
            )
        except OSError as error:
            print(f"Could not create {link.destination}: {error}", file=sys.stderr)
            return 1

        print(f"Linked {link.label}: {link.destination} -> {link.source}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
