"""
License Information
===================
Display the current license state and all license details.
Handles registration if needed.

This is typically the first example to run to ensure the SDK is properly licensed.
No controller connection is needed.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import setup_license, print_title, enum_name

print_title("License Information")

# setup_license() checks the current state:
# - If licensed or in trial: displays the info
# - If expired: asks for credentials or shows the trial request URL
license_info = setup_license()

print("\nDetailed license properties:")
print(f"  State              : {enum_name(license_info.state)}")
print(f"  Licensee           : {license_info.licensee}")
print(f"  Product            : {license_info.product}")
print(f"  License key        : {license_info.license_key}")
print(f"  Evaluation days    : {license_info.evaluation_days_left}")
print(f"  Eval start date    : {license_info.evaluation_start_date}")
print(f"  Trial expiration   : {license_info.trial_period_expiration_date}")
print(f"  Product release    : {license_info.product_release_date}")
print(f"  Maintenance years  : {license_info.maintenance_years}")
print(f"  License issued     : {license_info.license_issued_date}")
print(f"  Maintenance expires: {license_info.maintenance_expiration_date}")

input("\nPress Enter to exit...")
