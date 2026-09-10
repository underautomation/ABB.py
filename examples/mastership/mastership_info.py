"""
Mastership - Request and Release the Write Access
=================================================
Mastership is what a client has to hold before it is allowed to change anything in a
domain. Only one client at a time holds it. This example lists the domains the
controller exposes, shows who holds each of them, then takes one and releases it.

Most write methods of the SDK take and release the mastership for you. Doing it by
hand is useful when several writes have to happen without another client stepping in.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, pick, enum_name

print_title("Mastership: Request and Release the Write Access")

robot = connect_robot()

try:
    mastership = robot.rws.mastership

    # Domains really exposed by the connected controller
    domains = mastership.get_domains()
    print(f"Domains ({len(domains)})")
    print("-" * 78)
    for domain in domains:
        info = mastership.get_info(domain)
        print(f"  {enum_name(domain):<32} holder: {enum_name(info.holder)}")
        print(f"      Held by me : {info.held_by_me}")
        print(f"      User id    : {info.user_id}")
        print(f"      Alias      : {info.alias}")
        print(f"      Location   : {info.location}")
        print(f"      Application: {info.application}")

    if not domains:
        raise SystemExit(0)

    print("\nPick a domain to take:")
    selected = pick(domains, "Domain", lambda d: enum_name(d))
    if selected is None:
        print("Nothing selected.")
        raise SystemExit(0)

    print(f"\nRequesting the mastership of {enum_name(selected)}...")
    mastership.request(selected)
    try:
        info = mastership.get_info(selected)
        print(f"  Held by me: {info.held_by_me}")
        print(f"  Holder    : {enum_name(info.holder)}")
        print("\n  While the mastership is held, this client can write in that domain.")
        input("  Press Enter to release it...")
    finally:
        mastership.release(selected)
        print(f"  Released. Held by me: {mastership.get_info(selected).held_by_me}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
