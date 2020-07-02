ansible-pacemaker-corosync role
===============================

Deploys corosync/pacemaker

# Variables

- `pacemaker_corosync_group`: Ansible group name for corosync cluster (default: false, *mandatory*)
- `pacemaker_corosync_ring_interface`: Interface to use for ring0 communications (default: false, *mandatory*)
- `pacemaker_corosync_fqdn`: Whether use inventory_hostname or ansible_fqdn as node name for corosync (default: false)

