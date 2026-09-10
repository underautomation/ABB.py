"""
System - Version, Options and Energy
====================================
Read the RobotWare version of the system, the list of options, the installed products,
the robot types and the energy counters.
Everything here is read only.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, enum_name, short_error

print_title("System: Version, Options and Energy")

robot = connect_robot()

try:
    system = robot.rws.system

    # RobotWare version and system identity
    info = system.get_info()
    print("System info")
    print("-" * 60)
    print(f"  Name         : {info.name}")
    print(f"  Version      : {info.version} ({info.version_name})")
    print(f"  Major.Minor  : {info.major}.{info.minor}.{info.build}.{info.revision}")
    print(f"  Build tag    : {info.build_tag}")
    print(f"  System id    : {info.system_id}")
    print(f"  Type         : {info.type}")
    print(f"  Title        : {info.title}")
    print(f"  Description  : {info.description}")
    print(f"  Date         : {info.date}")
    print(f"  Start time   : {info.start_time}")
    print(f"  Options      : {info.option_count}")

    # RobotWare options of the system
    options = system.get_options()
    print(f"\nOptions ({len(options)})")
    print("-" * 60)
    for name in options:
        print(f"  - {name}")

    # Robot types the system knows
    types = system.get_robot_types()
    print(f"\nRobot types ({len(types)})")
    print("-" * 60)
    for name in types:
        print(f"  - {name}")

    # Installed products with their version
    products = system.get_products()
    print(f"\nProducts ({len(products)})")
    print("-" * 60)
    for product in products:
        print(f"  - {product.name} {product.version} ({product.version_name})")

    # License string of the system
    try:
        print(f"\nSystem license: {system.get_license()}")
    except Exception as e:
        print(f"\nSystem license: not available ({short_error(e)})")

    # Energy counters, only available when the option is installed
    try:
        energy = system.get_energy()
        print("\nEnergy")
        print("-" * 60)
        print(f"  Measurement valid  : {energy.is_measurement_valid}")
        print(f"  State              : {enum_name(energy.state)}")
        print(f"  Time stamp         : {energy.time_stamp}")
        print(f"  Reset time         : {energy.reset_time}")
        print(f"  Interval energy    : {energy.interval_energy}")
        print(f"  Accumulated energy : {energy.accumulated_energy}")
        print(f"  Average power      : {energy.average_power}")
        for unit in energy.mechanical_units:
            print(f"  Mechanical unit    : {unit}")
    except Exception as e:
        print(f"\nEnergy: not available ({short_error(e)})")

finally:
    robot.disconnect()
    print("\nDisconnected.")
