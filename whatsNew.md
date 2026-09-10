First public release of the ABB SDK for Python.

This is an early version. It is already usable on real controllers, but the API can still
change based on your feedback. All feedback is welcome: missing endpoints, wrong parsing,
naming, documentation, or anything that does not work as you expect. Please open an issue
or contact support@underautomation.com.

## What it does

UnderAutomation.ABB lets you communicate with ABB industrial robot controllers through
Robot Web Services (RWS). The Python package wraps the .NET SDK with pythonnet and exposes
a pythonic API: snake_case methods, for example `robot.rws.controller.get_identity()`.

The same API covers both controller generations:

- IRC5 / RobotWare 6, RWS v1, over HTTP.
- OmniCore / RobotWare 7, RWS v2, over HTTPS.

## Install

```
pip install UnderAutomation.ABB
```

Runs on Python 3.7 to 3.13, on Windows, Linux and macOS. The only dependency is
`pythonnet`.

## Features

- A standalone RWS client, or the licensed controller client that exposes `.rws`.
- Controller: identity, system and RobotWare info, installed options, clock and time zone,
  network interfaces, backup create, restore and check, restart, safety configuration,
  cyclic brake check, virtual time.
- Operator panel: controller state, operation mode, speed ratio, collision detection state,
  operation mode lock.
- I/O: read and write signal values and states, list and search signals, devices and
  networks, pulse, invert, toggle, delayed set, device input and output data.
- RAPID: tasks, modules, programs, symbols and data values, program pointer, execution
  control, breakpoints, service routines, UI instructions, module text editing, pallet.
- Motion system: mechanical units, joint and Cartesian positions, RobTarget and JointTarget,
  forward and inverse kinematics, base frame, jogging, lead-through, revolution counter,
  calibration, motion and path supervision.
- Event log: domains, messages, message titles, read a message by its number, clear, save
  as system dump.
- File system: list, read, write, copy, rename and delete files and directories.
- Mastership: request and release the edit and motion mastership, per domain.
- System: options, products, robot types, license, energy consumption.
- Geometry helpers: `Position`, `Pose`, `Quaternion`, `RobTarget`, `JointTarget`.
- Every RWS failure is reported as `RwsException` and carries the HTTP status code.
- Ready to run examples in the `examples` folder.
