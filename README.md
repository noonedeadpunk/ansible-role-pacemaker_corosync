Ansible Role pacemaker_corosync ![Build Status](https://github.com/noonedeadpunk/ansible-pacemaker-corosync/actions/workflows/main.yml/badge.svg?branch=master)
===============================

Deploys and configures Corosync, Pacemaker, and Pacemaker Remote nodes.

See [CHANGELOG.md](CHANGELOG.md) for version history, upgrade notes, and breaking changes.

# Variables

## Core & Network

- `pacemaker_corosync_group`: Ansible group name for corosync cluster nodes (default: `false`, *mandatory*).
- `pacemaker_corosync_ring_interface`: Interface to use for ring0 communications on cluster nodes (default: `false`, *mandatory*).
- `pacemaker_corosync_bootstrap_node`: Host in `pacemaker_corosync_group` used to run bootstrap and cluster configuration commands (default: `{{ groups[pacemaker_corosync_group] | first }}`).
- `pacemaker_corosync_fqdn`: Whether to use `inventory_hostname` or `ansible_fqdn` as the node name in Corosync (default: `false`).
- `pacemaker_corosync_use_syslog`: Enable logging to syslog (default: `true`).
- `pacemaker_corosync_use_logfile`: Enable logging to logfile (default: `false`).

## Pacemaker Remote

- `pacemaker_remote_group`: Ansible group name for pacemaker-remote nodes (default: `false`).
- `pacemaker_remote_ring_interface`: Interface to use for communications on remote hosts (default: `{{ pacemaker_corosync_ring_interface }}`).
- `pacemaker_remote_register_resource`: Whether to register remote nodes as `ocf:pacemaker:remote` resources in the Pacemaker cluster (default: `true`).
- `pacemaker_remote_reconnect_interval`: Reconnect interval in seconds for `ocf:pacemaker:remote` resources. Set to `0` to omit (default: `15`).

## Cluster Properties & STONITH

- `pacemaker_cluster_properties`: Mapping of Pacemaker cluster properties to configure. Setting any property value to `null` or `""` will explicitly unset it from the cluster (reverting to Pacemaker default) (default: `{}`).
  > **Note**: When using Pacemaker Remote nodes, it is recommended to set `cluster-recheck-interval` (e.g. `10s` or `1m`). Pacemaker's default is `15min`, which can delay autonomous reconnection evaluations if no other cluster events trigger the scheduler.
- `pacemaker_stonith_devices`: List of STONITH fencing devices to configure with optional location constraints (default: `[]`).

# Configuration Examples

### Cluster Properties

```yaml
pacemaker_cluster_properties:
  stonith-enabled: true
  stonith-action: reboot
  no-quorum-policy: stop
  cluster-recheck-interval: 60s
  # Set a property to null or "" to unset it and restore Pacemaker default:
  batch-limit: null
```

### STONITH Devices

```yaml
pacemaker_stonith_devices:
  - name: "ipmi-node01"
    agent: "fence_ipmilan"
    params:
      ip: "10.0.1.101"
      username: "admin"
      password: "secretpassword"
      lanplus: "1"
      pcmk_host_list: "node01"
    avoid_node: "node01"  # Creates location constraint: pcs constraint location ipmi-node01 avoids node01
  - name: "ipmi-node02"
    agent: "fence_ipmilan"
    params:
      ip: "10.0.1.102"
      username: "admin"
      password: "secretpassword"
      lanplus: "1"
      pcmk_host_list: "node02"
    avoid_node: "node02"
```

# Example Playbook

```yaml
- name: Deploy Corosync and Pacemaker Cluster
  hosts: all
  roles:
    - role: pacemaker_corosync
      vars:
        pacemaker_corosync_group: pacemaker_cluster
        pacemaker_remote_group: pacemaker_remote_nodes
        pacemaker_corosync_ring_interface: eth1
        pacemaker_remote_ring_interface: eth2
        pacemaker_remote_reconnect_interval: 15
        pacemaker_cluster_properties:
          stonith-enabled: false
          cluster-recheck-interval: 10s
```
