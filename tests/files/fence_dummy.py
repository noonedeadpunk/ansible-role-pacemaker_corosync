#!/usr/bin/env python3
import sys

METADATA = """<?xml version="1.0" ?>
<resource-agent name="fence_dummy" shortdesc="Dummy fence agent">
<longdesc>Dummy fence agent for molecule testing</longdesc>
<parameters>
    <parameter name="action" required="0">
        <getopt mixed="-o, --action=[action]" />
        <content type="string" default="metadata" />
        <shortdesc lang="en">Fencing Action</shortdesc>
    </parameter>
    <parameter name="nodename" required="0">
        <getopt mixed="-N, --nodename" />
        <content type="string" />
        <shortdesc lang="en">Node name</shortdesc>
    </parameter>
    <parameter name="plug" required="0">
        <getopt mixed="-n, --plug" />
        <content type="string" />
        <shortdesc lang="en">Physical plug number</shortdesc>
    </parameter>
    <parameter name="pcmk_host_list" required="0">
        <getopt mixed="-s" />
        <content type="string" />
        <shortdesc lang="en">Host list</shortdesc>
    </parameter>
</parameters>
<actions>
    <action name="on" />
    <action name="off" />
    <action name="reboot" />
    <action name="status" />
    <action name="list" />
    <action name="monitor" />
    <action name="metadata" />
</actions>
</resource-agent>
"""

is_metadata = ("-o" in sys.argv and "metadata" in sys.argv) or ("--action=metadata" in sys.argv)
if not is_metadata and not sys.stdin.isatty():
    stdin_content = sys.stdin.read()
    if "action=metadata" in stdin_content:
        is_metadata = True

if is_metadata:
    print(METADATA)
    sys.exit(0)

sys.exit(0)
