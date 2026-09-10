"""
Event Log - Read the Controller Messages
========================================
List the event log domains, then read the messages of the one you pick, newest first,
with their title, their description, their causes and the actions they suggest.
Reading the event log does not change anything on the controller.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, ask, ask_int, pick, enum_name
from underautomation.abb.rws.data.elog_message_order import ElogMessageOrder

print_title("Event Log: Read the Controller Messages")

robot = connect_robot()

try:
    elog = robot.rws.elog

    # The language decides in which language the controller writes the texts
    language = ask("Language code, for example en or fr", "en")

    domains = elog.get_domains(language)
    print(f"\nDomains ({len(domains)})")
    print(f"  {'#':>4}  {'Number':<8} {'Name':<24} {'Messages':<10} {'Buffer':<10}")
    print(f"  {'-' * 4}  {'-' * 8} {'-' * 24} {'-' * 10} {'-' * 10}")
    for i, d in enumerate(domains, 1):
        print(f"  {i:>4}. {d.number:<8} {d.name:<24} {d.message_count:<10} {d.buffer_size:<10}")

    if not domains:
        raise SystemExit(0)

    print("\nPick a domain to read:")
    domain = pick(domains, "Domain", lambda d: f"{d.name} ({d.message_count} messages)")
    if domain is None:
        raise SystemExit(0)

    count = ask_int("How many messages at most", 10)

    messages = elog.get_messages(domain.number, ElogMessageOrder.NewestFirst, language, count)
    print(f"\nMessages of {domain.name} ({len(messages)})")

    for message in messages:
        print()
        print("=" * 78)
        print(f"  {message.timestamp}  [{enum_name(message.type)}]  {message.code}")
        print(f"  {message.title}")
        print("-" * 78)
        print(f"  Sequence number : {message.sequence_number}")
        print(f"  Source          : {message.source_name}")
        if message.description:
            print(f"  Description     : {message.description}")
        if message.consequences:
            print(f"  Consequences    : {message.consequences}")
        if message.causes:
            print(f"  Causes          : {message.causes}")
        if message.actions:
            print(f"  Actions         : {message.actions}")
        if message.argument_count:
            print(f"  Arguments       : {', '.join(str(a) for a in message.arguments)}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
