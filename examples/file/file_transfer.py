"""
File - Upload, Download and Delete
==================================
List a directory of the controller, send a local file into it, download the file back
to check its content, then delete it.
Everything is done under $temp so nothing of the system is touched.

Note: the example reads the directory before uploading. On an OmniCore controller the
first request of a connection has to be a read, otherwise the upload waits for the
authentication challenge until the timeout.
"""
import sys, os, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, ask, confirm, short_error

print_title("File: Upload, Download and Delete")

robot = connect_robot()

try:
    files = robot.rws.file

    remote_directory = ask("Directory on the controller", "$temp")
    remote_name = ask("File name to create", "underautomation_example.txt")
    remote_path = f"{remote_directory.rstrip('/')}/{remote_name}"

    # Read the directory before writing anything in it
    listing = files.list_directory(remote_directory)
    print(f"\n{remote_directory} holds {listing.file_count} files:")
    for item in listing.files:
        print(f"  {item.name:<44} {item.size} bytes")

    # Prepare a small local file, or take the one the user gives
    local_source = ask("\nLocal file to upload (Enter to generate one)", "")
    if not local_source:
        local_source = os.path.join(tempfile.gettempdir(), remote_name)
        with open(local_source, "w", encoding="utf-8") as f:
            f.write("Hello from the UnderAutomation ABB SDK for Python.\n")
            f.write("This file was uploaded by the file_transfer example.\n")
        print(f"  Generated {local_source}")

    # Upload
    print(f"\nUploading {local_source} to {remote_path}")
    try:
        files.upload_file_from_path(remote_path, local_source)
        print("  Uploaded.")
    except Exception as e:
        print(f"  Upload failed: {short_error(e)}")
        raise SystemExit(1)

    # The file now shows up in the listing
    listing = files.list_directory(remote_directory)
    print(f"\n{remote_directory} now holds {listing.file_count} files:")
    for item in listing.files:
        marker = "  <- the new one" if item.name == remote_name else ""
        print(f"  {item.name:<44} {item.size} bytes{marker}")

    # Download it back as bytes
    content = files.get_file_as_bytes(remote_path)
    print(f"\nDownloaded {len(content)} bytes:")
    print("-" * 60)
    print(bytes(content).decode("utf-8", errors="replace"))

    # And also straight to a local file
    local_copy = os.path.join(tempfile.gettempdir(), f"downloaded_{remote_name}")
    files.get_file_to_destination(remote_path, local_copy)
    print(f"Saved a copy to {local_copy}")

    # Clean up
    print()
    if confirm(f"Delete {remote_path} from the controller?"):
        files.delete_file(remote_path)
        print("  Deleted.")
    else:
        print("  File left on the controller.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
