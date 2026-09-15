## Discover ABB controllers on the network

`AbbController.discover` looks for ABB controllers without opening a connection and without a license.
Two ways run together: listening for the announcements a controller sends on the network, and testing
the ports of the local machine, which finds a virtual controller of RobotStudio whatever port it was
given.

Each result is a `DiscoveredController`, with the address, the port, the RobotWare version when known,
and a `to_connection_parameters` method that builds parameters ready for `connect`.

```python
found = AbbController.discover()

for controller in found:
    print(f"{controller.system_name} at {controller.address}:{controller.port}")

robot = AbbController()
robot.connect(found[0].to_connection_parameters())
```

## Breaking change: removed `RwsConnectParametersBase.ip`

This property had no effect, the controller address was always taken from `ConnectionParameters.address`.
Remove any code that sets `params.rws.ip`, it was never read.
