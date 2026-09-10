"""
Controller - Backup
===================
List the backup resources, read the state of the last backup operation and read the
information stored in an existing backup. The example can also create a new backup
under $temp, which takes some time on the controller.
"""
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, ask, confirm, enum_name, short_error
from underautomation.abb.rws.data.backup_state import BackupState

print_title("Controller: Backup")

robot = connect_robot()

try:
    controller = robot.rws.controller

    # Resources exposed by the backup service
    resources = controller.get_backup_resources()
    print(f"Backup resources ({len(resources)})")
    print("-" * 60)
    for name in resources:
        print(f"  - {name}")

    # State of the last backup operation
    print("\nBackup state")
    print("-" * 60)
    print(f"  {enum_name(controller.get_backup_state())}")

    # Information stored in an existing backup
    path = ask("\nPath of an existing backup to inspect (Enter to skip)", "")
    if path:
        try:
            info = controller.get_backup_info(path)
            print(f"  {info}")
        except Exception as e:
            print(f"  Could not read the backup: {short_error(e)}")

    # Creating a backup writes on the controller
    print()
    if confirm("Create a new backup under $temp/example_backup?"):
        backup_path = "$temp/example_backup"
        controller.create_backup(backup_path)
        print(f"  Backup requested at {backup_path}")

        # The controller works in the background, so the state is polled
        for _ in range(30):
            state = controller.get_backup_state()
            print(f"  State: {enum_name(state)}")
            if state not in (BackupState.InitState, BackupState.BackupInProgress):
                break
            time.sleep(2)

        # Read back what the new backup contains
        try:
            print(f"  Backup info: {controller.get_backup_info(backup_path)}")
        except Exception as e:
            print(f"  Could not read the new backup: {short_error(e)}")
    else:
        print("  No backup created.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
