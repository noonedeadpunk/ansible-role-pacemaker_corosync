# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - Unreleased

### Upgrade Notes

* **Decoupled Architecture**: Corosync configuration and cluster formation tasks now execute exclusively on nodes belonging to `pacemaker_corosync_group`. Remote nodes (`pacemaker_remote_group`) run only the lightweight `pacemaker-remote` daemon without Corosync.
* **Automatic Node Cleanup on Role Transition**: If a host that previously belonged to `pacemaker_corosync_group` is migrated to `pacemaker_remote_group`, the role automatically cleans up leftover Corosync configuration files, services, and packages to prevent lingering or conflicting cluster daemons.
* **Centralized Authkey Distribution**: The authentication key (`/etc/pacemaker/authkey`) is generated on the bootstrap node and distributed across nodes with `0640` permissions (`root:haclient`).
* **Explicit Bootstrap Node**: Introduced `pacemaker_corosync_bootstrap_node` (defaults to `{{ groups[pacemaker_corosync_group] | first }}`). Cluster-wide commands (`pcs` property setup, STONITH device configuration, authkey generation, and remote node registration) run deterministically via this designated bootstrap host.

### Added

* **Declarative Cluster Properties**: Introduced `pacemaker_cluster_properties` dictionary to configure Pacemaker cluster properties. Setting any property value to `null` or `""` explicitly unsets it in the CIB, restoring Pacemaker's default value.
* **Declarative STONITH & Location Constraints**: Introduced `pacemaker_stonith_devices` to define fencing devices with agents and parameters. Each device supports `avoid_node` to automatically set location constraints preventing fencing agents from running on the node they protect. Stale location constraints for managed devices are automatically cleaned up.
* **Remote Resource Tuning**: Introduced `pacemaker_remote_register_resource` to toggle automatic `ocf:pacemaker:remote` resource registration, and `pacemaker_remote_reconnect_interval` (default: `15`) to configure the reconnection retry interval for remote nodes.
* **Modernized Molecule Testing**: Added full 3-node cluster and remote node test coverage with side-effect and verification testing.
* **CentOS Stream 10 Support**: Added support for CentOS Stream 10.

### Changed

* Refactored task structure into modular files (`tasks/install.yml`, `tasks/configure.yml`, `tasks/install_pacemaker.yml`, `tasks/install_pacemaker_remote.yml`, `tasks/configure_cluster.yml`, `tasks/configure_remote_resource.yml`, `tasks/cleanup_remote_node.yml`).
* Replaced `fetch` module with `slurp` for delegating authkey transfers.
* Modernized CI workflows and Molecule testing stack.

### Deprecated

* Role no longer manages or installs `haveged` on EL-like systems. Respective variables `pacemaker_corosync_haveged_enabled`, `pacemaker_corosync_centos_epel_key`, and `pacemaker_corosync_centos_epel_mirror` have been removed and have no effect.

## [1.1.0]

### Added
* Support for CentOS Stream 9.
* GitHub Actions CI workflow.

### Changed
* Updated testing stack for Ansible 2.17+.
* Refactored fact variable usage and removed deprecated command arguments.

## [1.0.0]

### Added
* Optional `pacemaker-remote` integration.
* Logging configuration variables (`pacemaker_corosync_use_syslog`, `pacemaker_corosync_use_logfile`).
* Option to use FQDN as node name (`pacemaker_corosync_fqdn`).
* Option to disable `haveged` installation.

## [0.9.1]

### Fixed
* Fixed linting issues and prevented unintended package upgrades.

## [0.9.0]

### Added
* Initial release providing Corosync and Pacemaker cluster deployment.
