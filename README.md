# ABB Robot Communication SDK for Python

[![PyPI](https://img.shields.io/pypi/v/UnderAutomation.ABB?label=PyPI&logo=pypi)](https://pypi.org/project/UnderAutomation.ABB/)
[![PyPI downloads](https://img.shields.io/pypi/dm/UnderAutomation.ABB?label=Downloads&logo=pypi)](https://pypi.org/project/UnderAutomation.ABB/)
[![Python](https://img.shields.io/badge/Python-3.7_to_3.13-blue)](#compatibility)
[![Platforms](https://img.shields.io/badge/OS-Windows_Linux_macOS-informational)](#compatibility)
[![License](https://img.shields.io/badge/license-commercial-blue)](https://underautomation.com/abb/eula)

**UnderAutomation.ABB** is a Python package that talks to ABB industrial robot controllers over
**Robot Web Services (RWS)**. The same code runs on **IRC5** (RobotWare 6) and on **OmniCore**
(RobotWare 7). Nothing is installed on the controller. No RobotStudio, no PC SDK, no ABB runtime.

Use it to read and write RAPID variables, control I/O, read positions, jog the robot, manage programs,
files and backups, and follow the state of the controller, from a Python script. It works with real
controllers and with the virtual controllers of RobotStudio.

- Product page: [underautomation.com/abb](https://underautomation.com/abb)
- Documentation: [underautomation.com/abb/documentation/get-started-python](https://underautomation.com/abb/documentation/get-started-python)
- Also available for .NET: [ABB.NET](https://github.com/underautomation/ABB.NET)

## What you can do

- **RAPID variables and programs:** read and write variables, persistents and constants, start and stop
  tasks, move the program pointer, load and save modules.
- **Inputs / Outputs:** list, read and write digital, analog and group signals, pulse, invert or simulate
  a signal, browse I/O devices and networks.
- **Position and kinematics:** read the current `robtarget` and `jointtarget`, convert between Cartesian
  pose and joint values, jog the robot.
- **Controller and state:** identity, options, operation mode, controller state, speed ratio, clock,
  language and network.
- **Backup and restore:** create a full backup, check it, restore it.
- **File system:** browse the controller file system, download and upload files, create, copy, rename and
  delete files and directories.
- **Event log:** read the event log by domain, in the language you ask, and clear it.
- **System and energy:** system product list, options and energy counters.
- **Mastership:** request and release the edit and motion mastership.
- **Discovery:** find the ABB controllers of the local network and the virtual controllers of this
  machine, without a license and without a known address.
- **One API for both controller generations:** IRC5 (RWS 1.0) and OmniCore (RWS 2.0), only one connection
  parameter changes.

No ABB option is required on the controller. Robot Web Services is part of a standard system.

## How it works

The package wraps the .NET library `UnderAutomation.ABB.dll` with [pythonnet](https://github.com/pythonnet/pythonnet).
The DLL is inside the package: `pip install` installs everything, including pythonnet.

- **Windows:** the DLL runs on the .NET Framework 4.x of Windows. Nothing else to install.
- **Linux and macOS:** install the .NET runtime (for example .NET 8), then tell pythonnet to use it before
  you start Python:

  ```bash
  export PYTHONNET_RUNTIME=coreclr
  ```

  Without this variable, pythonnet uses Mono, its default runtime on Linux and macOS. You can also choose
  the runtime in your code, before the first import of the package:

  ```python
  from pythonnet import load
  load("coreclr")
  ```

## Installation

Python 3.7 to 3.13 is supported (the limit of pythonnet 3.0.5). Install the package in a virtual
environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux and macOS
source .venv/bin/activate

pip install UnderAutomation.ABB
```

Or install it from the sources of this repository:

```bash
git clone https://github.com/underautomation/ABB.py.git
cd ABB.py
pip install -e .
```

## Getting started

```python
from underautomation.abb.abb_controller import AbbController

# The SDK runs in trial mode for 30 days. Register your key to remove the trial limit.
# AbbController.register_license("Your Company", "your-license-key")

robot = AbbController()
robot.connect("192.168.125.1")

identity = robot.rws.controller.get_identity()
print(identity.name)

robot.disconnect()
```

### Choose the controller generation

The default is OmniCore (RWS 2.0). For an IRC5 controller, set the version to `RwsVersion.Irc5_V1_0`.
The rest of your code does not change.

```python
from underautomation.abb.abb_controller import AbbController
from underautomation.abb.connection_parameters import ConnectionParameters
from underautomation.abb.rws.rws_version import RwsVersion

params = ConnectionParameters("192.168.125.1")
params.rws.username = "Default User"
params.rws.password = "robotics"
params.rws.use_https = True                    # OmniCore is reached over HTTPS
params.rws.version = RwsVersion.OmniCore_V2_0  # or RwsVersion.Irc5_V1_0 for IRC5

robot = AbbController()
robot.connect(params)
```

### Without the license layer

`RwsClient` is a standalone RWS client that you can use without `AbbController`:

```python
from underautomation.abb.rws.rws_client import RwsClient
from underautomation.abb.rws.rws_version import RwsVersion

client = RwsClient()
client.connect("192.168.125.1", useHttps=True, version=RwsVersion.OmniCore_V2_0)
print(client.controller.get_identity().name)
```

## From .NET names to Python names

The Python API is the .NET API with Python names. The [.NET documentation](https://underautomation.com/abb/documentation)
applies to Python.

| .NET | Python |
| --- | --- |
| Method `GetIdentity()` | `get_identity()` |
| Property `Rws.Controller` | `rws.controller` |
| Static method `AbbController.RegisterLicense(...)` | `AbbController.register_license(...)` |
| Enum value `RwsVersion.OmniCore_V2_0` | `RwsVersion.OmniCore_V2_0` |
| Array `IoSignalItem[]` | list-like object, use `list(...)` to copy it |
| `Nullable<int>` | `int \| None` |

Each type is in the module named after it, in snake case:
`UnderAutomation.ABB.Rws.Data.MastershipDomain` is `underautomation.abb.rws.data.mastership_domain.MastershipDomain`.

The async methods of the .NET API (`...Async`) have no Python equivalent: use the synchronous methods.

## Features

Everything is reached through `robot.rws`, grouped by service:
`controller`, `io`, `rapid`, `motion_system`, `panel`, `system`, `file`, `elog`, `mastership`.

### RAPID variables and programs

```python
from underautomation.abb.rws.data.mastership_domain import MastershipDomain

# Read a RAPID symbol, the value comes back the way RAPID writes it
reg1 = robot.rws.rapid.get_symbol_value("RAPID/T_ROB1/user/reg1")
print(reg1.value)

# Write a symbol (needs the edit mastership in automatic mode)
robot.rws.mastership.request(MastershipDomain.Edit)
robot.rws.rapid.set_symbol_value("RAPID/T_ROB1/user/reg1", "42")
robot.rws.mastership.release(MastershipDomain.Edit)

# Start and stop the program
robot.rws.rapid.start()
robot.rws.rapid.stop()

# Load a program, list tasks, follow the execution state
robot.rws.rapid.load_program("T_ROB1", "HOME:/myprogram.pgf")
tasks = robot.rws.rapid.get_tasks()
state = robot.rws.rapid.get_execution_state()
```

### Inputs / Outputs

```python
# List every signal
signals = robot.rws.io.get_signals()

# Read one signal
di1 = robot.rws.io.get_signal("EtherNetIP", "d652", "DI_01")
print(di1.logical_value)

# Write, pulse or invert an output
robot.rws.io.set_signal_value("EtherNetIP", "d652", "DO_01", 1)
robot.rws.io.pulse_signal("EtherNetIP", "d652", "DO_01", 1, pulses=3)
robot.rws.io.invert_signal("EtherNetIP", "d652", "DO_01", 1)

# Simulate a signal so a value can be forced without hardware
robot.rws.io.set_signal_state("EtherNetIP", "d652", "DI_01", simulated=True)
```

### Position and kinematics

```python
from underautomation.abb.common.robot_joints import RobotJoints

# Current Cartesian and joint position of a task
rob_target = robot.rws.rapid.get_rob_target("T_ROB1")
joint_target = robot.rws.rapid.get_joint_target("T_ROB1")

print(f"X={rob_target.x} Y={rob_target.y} Z={rob_target.z}")
print(f"J1={joint_target.robot_axes.axis1} J2={joint_target.robot_axes.axis2}")

# Jog the robot
robot.rws.motion_system.set_jogging_mechanical_unit("ROB_1")
robot.rws.motion_system.jog(RobotJoints(5, 0, 0, 0, 0, 0), 0)
```

### Discover controllers

```python
# Finds the controllers of the local network and the virtual controllers of this machine.
# No connection is opened and no license is needed.
found = AbbController.discover()

for controller in found:
    print(f"{controller.system_name} at {controller.address}:{controller.port}")

# to_connection_parameters carries the address, the port, the scheme and the RWS version found
robot = AbbController()
robot.connect(found[0].to_connection_parameters())
```

### Controller and state

```python
from datetime import datetime

identity = robot.rws.controller.get_identity()
info = robot.rws.controller.get_info()

mode = robot.rws.panel.get_operation_mode()
state = robot.rws.panel.get_controller_state()
speed_ratio = robot.rws.panel.get_speed_ratio()

robot.rws.panel.set_speed_ratio(50)
robot.rws.controller.set_clock(datetime.now())

has_option = robot.rws.controller.has_option("RobotWare-OS")
```

### Backup and restore

```python
robot.rws.controller.create_backup("HOME:/backups/2026-01-15")

check = robot.rws.controller.check_restore("HOME:/backups/2026-01-15")
if check.is_accepted:
    robot.rws.controller.restore_backup("HOME:/backups/2026-01-15")
```

### File system

```python
listing = robot.rws.file.list_directory("HOME:/")
for d in listing.directories:
    print(d.name)
for f in listing.files:
    print(f"{f.name} ({f.size} bytes)")

robot.rws.file.upload_file_from_path("HOME:/myprogram.mod", r"C:\rapid\myprogram.mod")
robot.rws.file.get_file_to_destination("HOME:/myprogram.mod", r"C:\backup\myprogram.mod")
robot.rws.file.delete_file("HOME:/old.mod")
```

### Event log

```python
messages = robot.rws.elog.get_messages(domain=0, language="en")
for m in messages:
    print(f"{m.timestamp} {m.title}")

robot.rws.elog.clear_all_messages()
```

### Mastership

```python
from underautomation.abb.rws.data.mastership_domain import MastershipDomain

robot.rws.mastership.request(MastershipDomain.Motion)
# ... jog or move the robot ...
robot.rws.mastership.release(MastershipDomain.Motion)
```

## Examples

The folder [`examples`](examples) contains scripts ready to run, one folder per RWS service.
`examples/__init__.py` holds the shared helpers: Python path, connection settings and license
registration. The first run asks the address of the controller, the RWS credentials and the protocol
version, and saves them in `examples/robot_config.json` (ignored by git). Press Enter to accept the value
between brackets.

Run a script from the root of the repository:

```bash
python examples/system/system_info.py
```

Or choose a script in a menu. The launcher runs it in the same process, so a breakpoint set in an example
file is hit:

```bash
python examples/launcher.py
```

| Script | What it does |
| --- | --- |
| [`license/license_info.py`](examples/license/license_info.py) | License state and every license property, no connection needed. |
| [`controller/controller_identity.py`](examples/controller/controller_identity.py) | Name, serial id, type, MAC address, installed systems, options and network interfaces. |
| [`controller/controller_clock.py`](examples/controller/controller_clock.py) | Reads the controller clock, its time zone and its time server, and sets the clock. |
| [`controller/controller_backup.py`](examples/controller/controller_backup.py) | Reads the backup state and the content of a backup, and creates a new one under `$temp`. |
| [`system/system_info.py`](examples/system/system_info.py) | RobotWare version, options, robot types, installed products and energy counters. |
| [`panel/panel_state.py`](examples/panel/panel_state.py) | Controller state, operation mode, mode selector lock and collision detection. |
| [`panel/panel_speed_ratio.py`](examples/panel/panel_speed_ratio.py) | Reads and writes the speed ratio, switches the motors on and off. |
| [`io/io_list_signals.py`](examples/io/io_list_signals.py) | Lists every signal with its value and its state, and searches signals by name. |
| [`io/io_read_signal.py`](examples/io/io_read_signal.py) | Reads one signal in detail: values, states, quality, timestamps, configuration. |
| [`io/io_write_signal.py`](examples/io/io_write_signal.py) | Writes, inverts, pulses and simulates an output signal, then restores it. |
| [`io/io_networks_devices.py`](examples/io/io_networks_devices.py) | Browses the I/O topology: fieldbus networks, devices and their signals. |
| [`rapid/rapid_tasks.py`](examples/rapid/rapid_tasks.py) | Lists the tasks, reads one in detail, its program, its pointers and the execution state. |
| [`rapid/rapid_read_symbol.py`](examples/rapid/rapid_read_symbol.py) | Searches the RAPID symbols of a task and reads the value and properties of one. |
| [`rapid/rapid_write_symbol.py`](examples/rapid/rapid_write_symbol.py) | Takes the edit mastership, writes a variable, restores it and releases the mastership. |
| [`rapid/rapid_modules.py`](examples/rapid/rapid_modules.py) | Lists the modules of a task, prints the source code and searches a text in it. |
| [`rapid/rapid_start_stop.py`](examples/rapid/rapid_start_stop.py) | Resets the program pointer, starts the execution, follows its state and stops it. |
| [`motion/motion_mechanical_units.py`](examples/motion/motion_mechanical_units.py) | Lists the mechanical units, their axes, their base frame and their calibration. |
| [`motion/motion_current_position.py`](examples/motion/motion_current_position.py) | Reads the current `robtarget` in each coordinate system, the `jointtarget` and the axes. |
| [`motion/motion_kinematics.py`](examples/motion/motion_kinematics.py) | Forward and inverse kinematics on the controller, and every joint solution of a pose. |
| [`file/file_browse.py`](examples/file/file_browse.py) | Walks the controller file system, enters directories and reads the content of a file. |
| [`file/file_transfer.py`](examples/file/file_transfer.py) | Uploads a local file under `$temp`, downloads it back and deletes it. |
| [`elog/elog_messages.py`](examples/elog/elog_messages.py) | Lists the event log domains and reads their messages with causes and actions. |
| [`mastership/mastership_info.py`](examples/mastership/mastership_info.py) | Lists the mastership domains, shows who holds them, takes one and releases it. |

Notes:

- An example that only reads is safe on any controller. The examples that write ask before each change
  and put the original value back.
- A virtual controller does not implement every resource of a real one. When it answers 404, the example
  prints the reason and continues.
- A controller refuses a write when the mode selector is on manual and the FlexPendant keeps the
  ownership. The example prints the 403 answer instead of stopping.
- The certificate of an OmniCore controller is signed by the controller itself. `examples/__init__.py`
  accepts it before the connection, see `allow_self_signed_certificates()`.

## IRC5 and OmniCore, one API

ABB controllers expose Robot Web Services in two versions. This SDK covers both. The same code runs on an
IRC5 and on an OmniCore. Only the connection parameters change.

| Controller | RobotWare | Robot Web Services | `RwsVersion` value |
| --- | --- | --- | --- |
| IRC5 | RobotWare 6 and earlier | RWS 1.0 | `RwsVersion.Irc5_V1_0` |
| OmniCore | RobotWare 7 and later | RWS 2.0 | `RwsVersion.OmniCore_V2_0` |

HTTP or HTTPS is a separate setting (`use_https`), independent of the controller generation.

## Compatibility

- **Python:** 3.7 to 3.13, with pythonnet 3.0.5.
- **Operating systems:** Windows (.NET Framework), Linux and macOS (.NET runtime and `export PYTHONNET_RUNTIME=coreclr`).
- **Controllers:** IRC5, OmniCore, and their virtual controllers in RobotStudio.

## License

This SDK needs a commercial license. A 30-day trial starts at the first use, no key needed. After the
trial, register your key in your code:

```python
from underautomation.abb.abb_controller import AbbController

license_info = AbbController.register_license("Your Company", "your-license-key")
print(license_info.state)
```

- License agreement: [underautomation.com/abb/eula](https://underautomation.com/abb/eula) and [License.md](License.md)
- Trial key: [underautomation.com/license](https://underautomation.com/license?sdk=abb)
- Prices and quote: [underautomation.com/abb](https://underautomation.com/abb)

## Support

- Documentation: [underautomation.com/abb/documentation](https://underautomation.com/abb/documentation)
- Issues: [GitHub Issues](https://github.com/underautomation/ABB.py/issues)
- Contact: [underautomation.com/contact](https://underautomation.com/contact)
