# ABB Robot Communication SDK for Python

[![PyPI](https://img.shields.io/pypi/v/UnderAutomation.ABB?label=PyPI&logo=pypi)](https://pypi.org/project/UnderAutomation.ABB/)
[![Python](https://img.shields.io/badge/Python-3.7_|_3.8_|_3.9_|_3.10_|_3.11_|_3.12_|_3.13-blue?logo=python)](#-compatibility)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-blue)](#-compatibility)
[![License](https://img.shields.io/badge/License-Commercial-red)](https://underautomation.com/abb/eula)

### 🤖 Talk to ABB robots from Python

**UnderAutomation.ABB** is a fully managed SDK that talks to ABB industrial robot controllers over
**Robot Web Services (RWS)**. The same code runs on **IRC5** (RobotWare 6) and on **OmniCore**
(RobotWare 7). Nothing is installed on the controller. No RobotStudio, no PC SDK, no ABB runtime.

Use it to read and write RAPID variables, control I/O, read positions, jog the robot, manage programs,
files and backups, and follow the state of the controller, from a normal Python application.

It works with **real controllers** and with the **virtual controllers** of RobotStudio.

🔗 **More information:** [https://underautomation.com/abb](https://underautomation.com/abb)

🔗 Also available in **[🟦 .NET](https://github.com/underautomation/ABB.NET)**

---

[⭐ Star this repo if it is useful to you](https://github.com/underautomation/ABB.py/stargazers)
[👁️ Watch it to follow new releases](https://github.com/underautomation/ABB.py/watchers)

---

## 🚀 TL;DR

- ✔️ **No RobotStudio, no PC SDK** - RWS is part of a standard controller system
- 🧾 **RAPID variables and programs** - read and write variables, persistents and constants, start and stop tasks, move the program pointer, load and save modules
- ⚡ **Inputs / Outputs** - list, read and write digital, analog and group signals, pulse, invert or simulate a signal, browse I/O devices and networks
- 📐 **Position and kinematics** - read the current `robtarget` and `jointtarget`, convert between Cartesian pose and joint values, jog the robot
- 🎛️ **Controller and state** - identity, options, operation mode, controller state, speed ratio, clock, language and network
- 💾 **Backup and restore** - create a full backup, check it, restore it
- 📂 **File system** - browse the controller file system, download and upload files, create, copy, rename and delete files and directories
- 📜 **Event log** - read the event log by domain, in the language you ask, and clear it
- 🔋 **System and energy** - system product list, options and energy counters
- 🔑 **Mastership** - request and release the edit and motion mastership
- 🔁 **One API for both controller generations** - IRC5 (RWS 1.0) and OmniCore (RWS 2.0), only one connection parameter changes

---

## 🛠 Installation & Getting Started

### Prerequisites

- **Python 3.7** or higher
- An ABB robot controller, or a virtual controller in RobotStudio

### Step 1 - Create a virtual environment

We recommend a virtual environment to keep your project dependencies isolated.

```bash
# Create a project folder
mkdir my-abb-project
cd my-abb-project

# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### Step 2 - Install the SDK

The SDK is published on PyPI:

```bash
pip install UnderAutomation.ABB
```

All dependencies (including `pythonnet`) are installed automatically.

On **Linux**, also install the .NET runtime and set `PYTHONNET_RUNTIME` to `coreclr`:

```bash
sudo apt-get install -y dotnet-runtime-8.0
export PYTHONNET_RUNTIME=coreclr
```

> **Alternative: install from source**
>
> ```bash
> git clone https://github.com/underautomation/ABB.py.git
> cd ABB.py
> pip install -e .
> ```

### Step 3 - Connect to your controller

Create a Python file (for example `main.py`):

```python
from underautomation.abb.abb_controller import AbbController

# The SDK runs in trial mode for 30 days. Register your key to remove the trial limit.
# If you get a license exception, ask a trial key at https://underautomation.com/license
# AbbController.register_license("Your Company", "your-license-key")

robot = AbbController()

# Connect (replace with your controller IP address)
robot.connect("192.168.125.1")

identity = robot.rws.controller.get_identity()
print(identity.name)

robot.disconnect()
```

Run it:

```bash
python main.py
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
params.rws.use_https = True                        # OmniCore is reached over HTTPS
params.rws.version = RwsVersion.OmniCore_V2_0      # or RwsVersion.Irc5_V1_0 for IRC5

robot = AbbController()
robot.connect(params)
```

> **Without the licensed controller class**
>
> `RwsClient` is a standalone RWS client you can use without the `AbbController` licensing layer:
>
> ```python
> from underautomation.abb.rws.rws_client import RwsClient
> from underautomation.abb.rws.rws_version import RwsVersion
>
> client = RwsClient()
> client.connect("192.168.125.1", useHttps=True, version=RwsVersion.OmniCore_V2_0)
> print(client.controller.get_identity().name)
> ```

---

## 🔑 Licensing

The SDK works out of the box for **30 days** (trial period), no registration needed.

After the trial, you can:

- **Buy a license** at [underautomation.com/order](https://underautomation.com/order?sdk=abb)
- **Get a new trial period immediately by email** at [underautomation.com/license](https://underautomation.com/license?sdk=abb)

To register a license in code:

```python
from underautomation.abb.abb_controller import AbbController

license_info = AbbController.register_license("your-licensee", "your-license-key")
print(license_info)
```

---

## 📌 Features

Everything is reached through `robot.rws`, grouped by service:
`controller`, `io`, `rapid`, `motion_system`, `panel`, `system`, `file`, `elog`, `mastership`.

### 🧾 RAPID variables and programs

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

### ⚡ Inputs / Outputs

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

### 📐 Position and kinematics

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

### 🎛️ Controller and state

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

### 💾 Backup and restore

```python
robot.rws.controller.create_backup("HOME:/backups/2026-01-15")

check = robot.rws.controller.check_restore("HOME:/backups/2026-01-15")
if check.is_accepted:
    robot.rws.controller.restore_backup("HOME:/backups/2026-01-15")
```

### 📂 File system

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

### 📜 Event log

```python
messages = robot.rws.elog.get_messages(domain=0, language="en")
for m in messages:
    print(f"{m.timestamp} {m.title}")

robot.rws.elog.clear_all_messages()
```

### 🔑 Mastership

```python
from underautomation.abb.rws.data.mastership_domain import MastershipDomain

robot.rws.mastership.request(MastershipDomain.Motion)
# ... jog or move the robot ...
robot.rws.mastership.release(MastershipDomain.Motion)
```

---

## 📂 Examples

The repository ships a set of ready to run examples in the [`examples/`](https://github.com/underautomation/ABB.py/tree/main/examples) folder, one subfolder per RWS service.

### How the Examples Work

| File                                                                                                | Role                                                                                                                    |
| --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| [`examples/launcher.py`](https://github.com/underautomation/ABB.py/blob/main/examples/launcher.py)  | **Interactive menu** - browse and run any example from a single launcher                                                |
| [`examples/__init__.py`](https://github.com/underautomation/ABB.py/blob/main/examples/__init__.py)  | **Shared helpers** - sets up the Python path, manages the connection settings and handles the license registration      |
| `examples/robot_config.json`                                                                        | **Saved settings** (git-ignored) - remembers the controller address, the credentials and the license key                |

**Run an example directly**

> The first time you run an example, it asks for the controller address, the RWS credentials and the protocol version. The answers are saved in `robot_config.json`, so they are only typed once. Press Enter to accept the value between brackets.

```bash
python examples/system/system_info.py
```

**Or browse the examples with the launcher**

```bash
python examples/launcher.py
```

The launcher discovers the examples on its own and runs the one you pick in the same process, so a breakpoint set in an example file is hit:

```
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║                             █████╗  ██████╗ ██████╗                            ║
║                             ██╔══██╗██╔══██╗██╔══██╗                           ║
║                             ███████║██████╔╝██████╔╝                           ║
║                             ██╔══██║██╔══██╗██╔══██╗                           ║
║                             ██║  ██║██████╔╝██████╔╝                           ║
║                             ╚═╝  ╚═╝╚═════╝ ╚═════╝                            ║
║                                                                                ║
║                    Python SDK - Interactive Example Launcher                   ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════════════════════╗
║                                SELECT A CATEGORY                               ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║  🤖   1. CONTROLLER   (3 examples)                                             ║
║         Controller - identity, clock, options, backups                         ║
║                                                                                ║
║  📜   2. ELOG         (1 example)                                              ║
║         Event log - read and filter controller messages                        ║
║                                                                                ║
║  📂   3. FILE         (2 examples)                                             ║
║         File system - browse, download and upload files                        ║
║                                                                                ║
║  ⚡   4. IO           (4 examples)                                             ║
║         I/O system - networks, devices, read and write signals                 ║
║                                                                                ║
║  🔑   5. LICENSE      (1 example)                                              ║
║         License management - activation & status                               ║
║                                                                                ║
║  🔒   6. MASTERSHIP   (1 example)                                              ║
║         Mastership - request and release the write access                      ║
║                                                                                ║
║  🦾   7. MOTION       (3 examples)                                             ║
║         Motion system - mechanical units, positions, kinematics                ║
║                                                                                ║
║  🚦   8. PANEL        (2 examples)                                             ║
║         Control panel - controller state, operation mode, speed ratio          ║
║                                                                                ║
║  🧾   9. RAPID        (5 examples)                                             ║
║         RAPID - tasks, modules, symbols, program execution                     ║
║                                                                                ║
║  🧩  10. SYSTEM       (1 example)                                              ║
║         System - RobotWare version, options, products, energy                  ║
║                                                                                ║
╠════════════════════════════════════════════════════════════════════════════════╣
║  0. Exit                                                                       ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝

  Enter category number [0-10]:
```

---

### 📋 Complete Example List

#### 🔑 License

| #   | Example                                                                                                       | Description                                                        |
| --- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| 1   | [license_info.py](https://github.com/underautomation/ABB.py/blob/main/examples/license/license_info.py)       | Show the license state and every license property, no connection needed |

#### 🤖 Controller

| #   | Example                                                                                                                   | Description                                                                       |
| --- | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| 2   | [controller_identity.py](https://github.com/underautomation/ABB.py/blob/main/examples/controller/controller_identity.py)  | Name, serial id, type, MAC address, installed systems, options and network interfaces |
| 3   | [controller_clock.py](https://github.com/underautomation/ABB.py/blob/main/examples/controller/controller_clock.py)        | Read the controller clock, its time zone and its time server, and set the clock     |
| 4   | [controller_backup.py](https://github.com/underautomation/ABB.py/blob/main/examples/controller/controller_backup.py)      | Read the backup state and the content of a backup, and create a new one under `$temp` |

#### 🧩 System

| #   | Example                                                                                                 | Description                                                                     |
| --- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| 5   | [system_info.py](https://github.com/underautomation/ABB.py/blob/main/examples/system/system_info.py)    | RobotWare version, options, robot types, installed products and energy counters |

#### 🚦 Panel

| #   | Example                                                                                                             | Description                                                              |
| --- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| 6   | [panel_state.py](https://github.com/underautomation/ABB.py/blob/main/examples/panel/panel_state.py)                 | Controller state, operation mode, mode selector lock and collision detection |
| 7   | [panel_speed_ratio.py](https://github.com/underautomation/ABB.py/blob/main/examples/panel/panel_speed_ratio.py)     | Read and write the speed ratio, switch the motors on and off             |

#### ⚡ I/O

| #   | Example                                                                                                                 | Description                                                                  |
| --- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| 8   | [io_list_signals.py](https://github.com/underautomation/ABB.py/blob/main/examples/io/io_list_signals.py)                | List every signal with its value and its state, and search signals by name   |
| 9   | [io_read_signal.py](https://github.com/underautomation/ABB.py/blob/main/examples/io/io_read_signal.py)                  | Read one signal in detail: values, states, quality, timestamps, configuration |
| 10  | [io_write_signal.py](https://github.com/underautomation/ABB.py/blob/main/examples/io/io_write_signal.py)                | Write, invert, pulse and simulate an output signal, then restore it          |
| 11  | [io_networks_devices.py](https://github.com/underautomation/ABB.py/blob/main/examples/io/io_networks_devices.py)        | Browse the I/O topology: fieldbus networks, devices and their signals        |

#### 🧾 RAPID

| #   | Example                                                                                                                   | Description                                                                    |
| --- | --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| 12  | [rapid_tasks.py](https://github.com/underautomation/ABB.py/blob/main/examples/rapid/rapid_tasks.py)                       | List the tasks, read one in detail, its program, its pointers and the execution state |
| 13  | [rapid_read_symbol.py](https://github.com/underautomation/ABB.py/blob/main/examples/rapid/rapid_read_symbol.py)           | Search the RAPID symbols of a task and read the value and properties of one    |
| 14  | [rapid_write_symbol.py](https://github.com/underautomation/ABB.py/blob/main/examples/rapid/rapid_write_symbol.py)         | Take the edit mastership, write a variable, restore it and release the mastership |
| 15  | [rapid_modules.py](https://github.com/underautomation/ABB.py/blob/main/examples/rapid/rapid_modules.py)                   | List the modules of a task, print the source code and search a text in it      |
| 16  | [rapid_start_stop.py](https://github.com/underautomation/ABB.py/blob/main/examples/rapid/rapid_start_stop.py)             | Reset the program pointer, start the execution, follow its state and stop it   |

#### 🦾 Motion

| #   | Example                                                                                                                            | Description                                                                        |
| --- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| 17  | [motion_mechanical_units.py](https://github.com/underautomation/ABB.py/blob/main/examples/motion/motion_mechanical_units.py)       | List the mechanical units, their axes, their base frame and their calibration       |
| 18  | [motion_current_position.py](https://github.com/underautomation/ABB.py/blob/main/examples/motion/motion_current_position.py)       | Read the current `robtarget` in each coordinate system, the `jointtarget` and the axes |
| 19  | [motion_kinematics.py](https://github.com/underautomation/ABB.py/blob/main/examples/motion/motion_kinematics.py)                   | Forward and inverse kinematics on the controller, and every joint solution of a pose |

#### 📂 File

| #   | Example                                                                                                     | Description                                                                |
| --- | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 20  | [file_browse.py](https://github.com/underautomation/ABB.py/blob/main/examples/file/file_browse.py)          | Walk the controller file system, enter directories and read a file content  |
| 21  | [file_transfer.py](https://github.com/underautomation/ABB.py/blob/main/examples/file/file_transfer.py)      | Upload a local file under `$temp`, download it back and delete it           |

#### 📜 Event Log

| #   | Example                                                                                                           | Description                                                              |
| --- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| 22  | [elog_messages.py](https://github.com/underautomation/ABB.py/blob/main/examples/elog/elog_messages.py)            | List the event log domains and read their messages with causes and actions |

#### 🔒 Mastership

| #   | Example                                                                                                                     | Description                                                          |
| --- | ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 23  | [mastership_info.py](https://github.com/underautomation/ABB.py/blob/main/examples/mastership/mastership_info.py)            | List the mastership domains, see who holds them, take one and release it |

### Notes on the examples

- An example that only reads is safe on any controller. The ones that write ask before each change and put the original value back.
- A virtual controller does not implement every resource of a real one. When it answers 404, the example prints the reason and carries on.
- A controller refuses a write when the mode selector is on manual and the FlexPendant keeps the ownership. The example prints the 403 answer instead of stopping.
- On an OmniCore controller the certificate is signed by the controller itself. `examples/__init__.py` relaxes the .NET runtime for it before connecting, see `allow_self_signed_certificates()`.

---

## 🔁 IRC5 and OmniCore, one API

ABB controllers expose Robot Web Services in two versions. This SDK covers both. The same code runs on
an old IRC5 and on a new OmniCore. Only the connection parameters change.

| Controller | RobotWare               | Robot Web Services | `RwsVersion` value         |
| ---------- | ----------------------- | ------------------ | -------------------------- |
| IRC5       | RobotWare 6 and earlier | RWS 1.0            | `RwsVersion.Irc5_V1_0`     |
| OmniCore   | RobotWare 7 and later   | RWS 2.0            | `RwsVersion.OmniCore_V2_0` |

HTTP or HTTPS is a separate setting (`use_https`), independent of the controller generation.

---

## 🔍 Compatibility

|                       | Supported                                     |
| --------------------- | --------------------------------------------- |
| **Robot Controllers** | IRC5, OmniCore, and their virtual controllers |
| **OS**                | Windows, Linux, macOS                         |
| **Python**            | 3.7+                                          |
| **Dependency**        | `pythonnet 3.0.5` (installed automatically)   |

The controller needs no ABB option. Robot Web Services is part of a standard system.

---

## 📢 Contributing

We welcome your feedback and contributions.

- Report issues via [GitHub Issues](https://github.com/underautomation/ABB.py/issues)
- Submit pull requests with enhancements
- Suggest features and improvements

---

## 📜 License

**⚠️ This SDK requires a commercial license.**

- 🆓 **30-day free trial** included out of the box
- 🔄 **Get a new trial immediately** at [underautomation.com/license](https://underautomation.com/license?sdk=abb)
- 🛒 **Buy a license** at [underautomation.com/abb](https://underautomation.com/abb)
- 📄 **EULA**: [underautomation.com/abb/eula](https://underautomation.com/abb/eula)

---

## 📬 Need Help?

- 📖 **Documentation**: [underautomation.com/abb/documentation](https://underautomation.com/abb/documentation)
- 🐍 **Python Get Started Guide**: [underautomation.com/abb/documentation/get-started-python](https://underautomation.com/abb/documentation/get-started-python)
- 📦 **PyPI Package**: [pypi.org/project/UnderAutomation.ABB](https://pypi.org/project/UnderAutomation.ABB/)
- 📩 **Contact Us**: [underautomation.com/contact](https://underautomation.com/contact)
