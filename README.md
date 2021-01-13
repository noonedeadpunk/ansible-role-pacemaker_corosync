ansible-role-pacemaker_corosync [![Build Status](https://travis-ci.org/noonedeadpunk/ansible-role-pacemaker_corosync.svg?branch=master)](https://travis-ci.org/noonedeadpunk/ansible-role-pacemaker_corosync)
===============================

Deploys corosync/pacemaker

# Variables

- `pacemaker_corosync_group`: Ansible group name for corosync cluster (default: false, *mandatory*)
- `pacemaker_remote_group`: Ansible group name for pacemaker-remote cluster (default: false, *mandatory*)
- `pacemaker_corosync_ring_interface`: Interface to use for ring0 communications (default: false, *mandatory*)
- `pacemaker_remote_ring_interface`: Interface to use for ring0 communications on remote hosts (default: pacemaker_corosync_ring_interface)
- `pacemaker_corosync_fqdn`: Whether use inventory_hostname or ansible_fqdn as node name for corosync (default: false)
