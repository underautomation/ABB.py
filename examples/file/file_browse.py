"""
File - Browse the Controller File System
========================================
Walk the file system of the controller: list a directory, enter a sub directory,
go back up and read the content of a file.
Listing and reading do not change anything on the controller.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, ask, short_error

print_title("File: Browse the Controller File System")

robot = connect_robot()

try:
    files = robot.rws.file

    # $home is the user directory of the controller, a good place to start
    current_path = ask("Directory to start from", "$home")

    while True:
        print(f"\nListing {current_path}")
        print("-" * 78)

        try:
            listing = files.list_directory(current_path)
        except Exception as e:
            print(f"  Could not list this directory: {short_error(e)}")
            current_path = ask("Directory to list", "$home")
            continue

        entries = []

        for device in listing.devices:
            entries.append(("DEV ", device.name, ""))
        for directory in listing.directories:
            entries.append(("DIR ", directory.name, ""))
        for file_item in listing.files:
            entries.append(("    ", file_item.name, f"{file_item.size} bytes"))

        print(f"  {'#':>4}  {'Type':<5} {'Name':<40} {'Size':<15}")
        print(f"  {'-' * 4}  {'-' * 5} {'-' * 40} {'-' * 15}")
        for i, (kind, name, size) in enumerate(entries, 1):
            print(f"  {i:>4}. {kind:<5} {name:<40} {size:<15}")
        print(f"\n  {listing.directory_count} directories, {listing.file_count} files, "
              f"{listing.device_count} devices")

        choice = input("\nNumber to enter a directory or read a file, '..' to go up, 'q' to quit: ").strip()

        if choice.lower() == "q":
            break

        if choice == "..":
            parts = current_path.rstrip("/").rsplit("/", 1)
            current_path = parts[0] if len(parts) > 1 and parts[0] else current_path
            continue

        try:
            index = int(choice)
        except ValueError:
            continue

        if not 1 <= index <= len(entries):
            continue

        kind, name, _size = entries[index - 1]
        target = f"{current_path.rstrip('/')}/{name}"

        if kind.strip() in ("DIR", "DEV"):
            current_path = target
            continue

        # A file was picked, download it as bytes and print what it holds
        try:
            content = files.get_file_as_bytes(target)
            print(f"\nContent of {target} ({len(content)} bytes)")
            print("-" * 78)
            try:
                print(bytes(content).decode("utf-8", errors="replace")[:4000])
            except Exception:
                print(bytes(content)[:400])
        except Exception as e:
            print(f"  Could not read the file: {short_error(e)}")

        # And it can also be saved directly on the PC
        local = ask("\nLocal path to save it to (Enter to skip)", "")
        if local:
            files.get_file_to_destination(target, local)
            print(f"  Saved to {local}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
