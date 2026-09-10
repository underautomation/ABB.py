"""
Controller - Clock and Time Server
==================================
Read the controller clock, its time zone and its time server.
The example can also set the clock to the time of the PC, which a real controller
accepts but a virtual controller usually refuses.
"""
import sys, os
from datetime import datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, confirm, short_error

print_title("Controller: Clock and Time Server")

robot = connect_robot()

try:
    controller = robot.rws.controller

    # Current controller clock
    clock = controller.get_clock()
    print("Clock")
    print("-" * 60)
    print(f"  Controller time : {clock}")
    print(f"  PC time         : {datetime.now()}")

    # Time zone
    try:
        print(f"  Time zone       : {controller.get_time_zone()}")
    except Exception as e:
        print(f"  Time zone       : not available ({short_error(e)})")

    # Time server, if one is configured
    try:
        server = controller.get_time_server()
        print(f"  Time server     : {server.address}")
        print(f"  Server time     : {server.time}")
    except Exception as e:
        print(f"  Time server     : not configured ({short_error(e)})")

    # Writing the clock changes the controller, so it is asked first
    print()
    if confirm("Set the controller clock to the PC time?"):
        try:
            controller.set_clock(datetime.now())
            print(f"  New controller time: {controller.get_clock()}")
        except Exception as e:
            print(f"  The controller refused to set the clock: {short_error(e)}")
    else:
        print("  Clock left unchanged.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
