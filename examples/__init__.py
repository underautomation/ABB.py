"""
Helper for ABB.py examples
- Automatic sys.path setup
- Persistent controller configuration management
- License management
"""
import sys
import json
from pathlib import Path

# ==============================================================================
# Path setup for imports
# ==============================================================================
def setup_path():
    root = Path(__file__).parent.parent
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

setup_path()

# ==============================================================================
# Configuration file management
# ==============================================================================
_config_file = Path(__file__).parent / "robot_config.json"

def _load_config():
    """Load saved configuration from file."""
    if _config_file.exists():
        try:
            with open(_config_file, 'r') as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def _save_config(config):
    """Save configuration to file."""
    with open(_config_file, 'w') as f:
        json.dump(config, f, indent=2)

def _get_setting(key, prompt, default=None, hide_default=False):
    """
    Generic helper to get a setting from the user.
    If already saved, proposes it as default. Otherwise, asks the user and saves it.

    Args:
        key: Config key to load/save
        prompt: Display prompt for the user
        default: Default value if none saved
        hide_default: If True, shows '****' instead of the saved value (for passwords)

    Returns:
        str: The setting value
    """
    config = _load_config()
    saved = config.get(key, default)

    if saved is not None:
        display = "****" if hide_default and saved else saved
        user_input = input(f"{prompt} [{display}]: ").strip()
        value = user_input if user_input else saved
    else:
        value = input(f"{prompt}: ").strip()

    # Save if value has changed or is new
    if value != config.get(key):
        config[key] = value
        _save_config(config)

    return value

# ==============================================================================
# Controller address and RWS settings
# ==============================================================================
def get_robot_ip():
    """
    Gets the controller IP address or hostname.
    A RobotStudio virtual controller usually answers on 127.0.0.1.

    Returns:
        str: IP address or hostname
    """
    return _get_setting("robot_ip", "Controller IP address or hostname", default="127.0.0.1")

def get_rws_username():
    """
    Gets the RWS username used for Digest Authentication.
    The factory user of an ABB controller is "Default User".

    Returns:
        str: RWS username
    """
    return _get_setting("rws_username", "RWS username", default="Default User")

def get_rws_password():
    """
    Gets the RWS password used for Digest Authentication.
    The factory password of an ABB controller is "robotics".

    Returns:
        str: RWS password
    """
    return _get_setting("rws_password", "RWS password", default="robotics", hide_default=True)

def get_rws_version():
    """
    Gets the RWS protocol version to use.
    Enter 1 for an IRC5 controller (RobotWare 6), 2 for an OmniCore controller (RobotWare 7).

    Returns:
        RwsVersion: The selected protocol version
    """
    from underautomation.abb.rws.rws_version import RwsVersion

    raw = _get_setting("rws_version", "RWS version, 1 = IRC5 / RobotWare 6, 2 = OmniCore / RobotWare 7", default="2")
    return RwsVersion.Irc5_V1_0 if str(raw).strip() == "1" else RwsVersion.OmniCore_V2_0

def get_rws_use_https():
    """
    Gets whether the connection uses HTTPS.
    OmniCore controllers answer on HTTPS, IRC5 controllers on HTTP.

    Returns:
        bool: True to use HTTPS
    """
    raw = _get_setting("rws_use_https", "Use HTTPS (y/n)", default="y")
    return str(raw).strip().lower() in ("y", "yes", "true", "1")

def get_rws_port():
    """
    Gets the RWS port.
    Leave it at 0 to let the SDK use 80 for HTTP and 443 for HTTPS.

    Returns:
        int: The port number, 0 for the default one
    """
    raw = _get_setting("rws_port", "RWS port, 0 for the default one", default="0")
    try:
        return int(str(raw).strip())
    except ValueError:
        return 0

def get_rws_timeout():
    """
    Gets the HTTP request timeout in milliseconds.
    Uploading a file or creating a backup takes longer than a simple read, so the
    default is generous.

    Returns:
        int: Timeout in milliseconds
    """
    raw = _get_setting("rws_timeout", "RWS timeout in milliseconds", default="30000")
    try:
        return int(str(raw).strip())
    except ValueError:
        return 30000

# ==============================================================================
# License management
# ==============================================================================
def setup_license():
    """
    Checks the current license state and handles registration.

    - If already licensed or in trial: prints license info
    - If expired or invalid: asks user for licensee/key and registers
    - If user has no key: shows URL to request a free trial

    Returns:
        LicenseInfo: The current license information
    """
    from underautomation.abb.abb_controller import AbbController
    from underautomation.abb.license.license_state import LicenseState

    # Try loading saved license credentials
    config = _load_config()
    saved_licensee = config.get("licensee", "")
    saved_key = config.get("license_key", "")

    # Register saved license if available
    if saved_licensee and saved_key:
        license_info = AbbController.register_license(saved_licensee, saved_key)
    else:
        # Create a temporary controller to check the default license state
        robot = AbbController()
        license_info = robot.license_info

    state = license_info.state

    # If license is valid (Licensed, Trial, or ExtraTrial), just display info
    if state == LicenseState.Licensed or state == LicenseState.Trial or state == LicenseState.ExtraTrial:
        print("=" * 60)
        print("LICENSE INFO")
        print("=" * 60)
        print(license_info)
        print("=" * 60)
        return license_info

    # License is invalid, expired, or needs maintenance
    print("=" * 60)
    print("LICENSE REGISTRATION REQUIRED")
    print("=" * 60)
    print(f"Current license state: {license_info}")
    print()
    print("If you don't have a license key, you can request a free")
    print("trial license immediately by email from:")
    print("  https://underautomation.com/license")
    print()

    licensee = input("Enter licensee (company/name) [leave empty to skip]: ").strip()
    if not licensee:
        print("Skipping license registration. Running in current mode.")
        return license_info

    key = input("Enter license key: ").strip()
    if not key:
        print("No key provided. Skipping registration.")
        return license_info

    # Register the license
    license_info = AbbController.register_license(licensee, key)

    # Save credentials
    config["licensee"] = licensee
    config["license_key"] = key
    _save_config(config)

    print()
    print("LICENSE REGISTERED:")
    print(license_info)
    print("=" * 60)

    return license_info

# ==============================================================================
# HTTPS on a robot controller
# ==============================================================================
def allow_self_signed_certificates():
    """
    Prepare the .NET runtime for the HTTPS of a robot controller.

    An OmniCore controller answers on HTTPS with a certificate it signed itself, and
    on Windows the SDK runs on the .NET Framework runtime, which by default only
    offers SSL 3.0 and TLS 1.0 and refuses a certificate it cannot trace back to a
    trusted authority. Both are relaxed here, once for the whole process.

    Call it before connecting when use_https is True. It does nothing on the .NET
    runtimes that already handle this themselves.
    """
    try:
        import clr  # noqa: F401
        from System.Net import ServicePointManager, SecurityProtocolType
        from System.Net.Security import RemoteCertificateValidationCallback
    except Exception:
        return

    try:
        # TLS 1.2, the version an OmniCore controller speaks
        ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12
    except Exception:
        pass

    try:
        # Accept the certificate the controller signed itself
        def _accept_any_certificate(sender, certificate, chain, errors):
            return True

        ServicePointManager.ServerCertificateValidationCallback = \
            RemoteCertificateValidationCallback(_accept_any_certificate)
    except Exception:
        pass

# ==============================================================================
# Helper: Connect to the controller
# ==============================================================================
def connect_robot():
    """
    Creates an AbbController, sets up the license, asks for the connection
    settings and opens the RWS connection.

    Returns:
        AbbController: Connected controller instance
    """
    from underautomation.abb.abb_controller import AbbController
    from underautomation.abb.connection_parameters import ConnectionParameters

    # Setup license first
    setup_license()

    # Ask for the connection settings, saved values are proposed as defaults
    address = get_robot_ip()

    robot = AbbController()
    params = ConnectionParameters(address)

    # A virtual controller does not always answer to a ping
    params.ping_before_connect = False

    params.rws.enable = True
    params.rws.username = get_rws_username()
    params.rws.password = get_rws_password()
    params.rws.version = get_rws_version()
    params.rws.use_https = get_rws_use_https()
    params.rws.port = get_rws_port()
    params.rws.timeout = get_rws_timeout()

    # An OmniCore controller signs its own certificate, so the runtime is told to
    # accept it and to speak TLS 1.2
    if params.rws.use_https:
        allow_self_signed_certificates()

    scheme = "https" if params.rws.use_https else "http"
    print(f"\nConnecting to {scheme}://{address} (RWS {'1.0' if int(params.rws.version) == 10 else '2.0'})...")

    try:
        robot.connect(params)
    except Exception as e:
        error_msg = str(e)
        lowered = error_msg.lower()
        if "license" in lowered or "trial" in lowered or "expired" in lowered or "InvalidLicenseException" in type(e).__name__:
            # Keep only the human readable part, before the .NET stack trace
            readable = error_msg.split("\n")[0].strip()
            # Some .NET exceptions carry characters the Windows console cannot print
            safe_msg = readable.encode("ascii", errors="replace").decode("ascii")
            print(f"\nLicense error: {safe_msg}")
            print("\nPlease register a valid license first.")
            print("Get a free trial at: https://underautomation.com/license")
            raise SystemExit(1)
        raise

    print("Connected successfully!\n")

    return robot

# ==============================================================================
# Small console helpers used by the examples
# ==============================================================================
def print_title(title):
    """Print the header of an example."""
    print("=" * 60)
    print(f"  ABB SDK - {title}")
    print("=" * 60)

def ask(prompt, default=None):
    """Ask the user for a string, press Enter to accept the default."""
    if default is not None:
        raw = input(f"{prompt} [{default}]: ").strip()
        return raw if raw else default
    return input(f"{prompt}: ").strip()

def ask_int(prompt, default=None):
    """Ask the user for an integer, press Enter to accept the default."""
    while True:
        raw = ask(prompt, None if default is None else str(default))
        try:
            return int(raw)
        except (TypeError, ValueError):
            print("  Please enter a whole number.")

def ask_float(prompt, default=None):
    """Ask the user for a number, press Enter to accept the default."""
    while True:
        raw = ask(prompt, None if default is None else f"{default:.4f}")
        try:
            return float(raw)
        except (TypeError, ValueError):
            print("  Please enter a number.")

def short_error(exception):
    """
    Return a short printable message for an exception.

    A .NET exception carries its whole nested stack trace in its text, and that trace
    can hold characters the Windows console cannot print, so only the first line is
    kept and it is made safe for the console.
    """
    message = str(exception).split("\n")[0].strip()

    # The SDK appends the diagnostics of the request after the readable sentence
    for separator in (" Original error:", " See the inner exception", " --->"):
        if separator in message:
            message = message.split(separator)[0].strip()

    if not message:
        message = exception.__class__.__name__
    if len(message) > 200:
        message = message[:200] + " ..."
    return message.encode("ascii", errors="replace").decode("ascii")

def enum_name(value):
    """
    Return the readable name of an enum value.
    The enums of the SDK derive from IntEnum, so printing one directly shows the
    number behind it rather than its name.
    """
    return getattr(value, "name", str(value))

def default_task(tasks):
    """
    Return the task an example should work on by default.
    A controller also carries semi static tasks such as SC_CBC, which hold no program
    and no position, so the first motion task is preferred.
    """
    for task in tasks:
        if task.motion_task:
            return task
    return tasks[0] if tasks else None

def confirm(prompt):
    """Ask a yes / no question. Returns True only on an explicit yes."""
    return input(f"{prompt} (y/N): ").strip().lower() in ("y", "yes")

def pick(items, prompt, formatter=None):
    """
    Show a numbered list and let the user pick one item.
    Returns the selected item, or None when the list is empty or the user skips.
    """
    if not items:
        print("  (nothing to select)")
        return None

    for i, item in enumerate(items, 1):
        label = formatter(item) if formatter else str(item)
        print(f"  {i:>3}. {label}")

    raw = input(f"{prompt} [1-{len(items)}, Enter to skip]: ").strip()
    if not raw:
        return None
    try:
        index = int(raw)
    except ValueError:
        return None
    if 1 <= index <= len(items):
        return items[index - 1]
    return None
