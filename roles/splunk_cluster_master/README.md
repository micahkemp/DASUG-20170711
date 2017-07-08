Ansible Role
=====================

splunk_cluster_master
---------------------

Configure a Splunk server to be a cluster master.

### Files

*   cluster_master_app

### Dependencies

*   splunk_forwarder_inputs_app

    Installed into master-apps/

*   splunk_license_slave_app

    Installed into master-apps/

    Commented out for demo, due to lack of appropriate license.

### Tasks

*   Install cluster_master_app

*   Restart Splunk

    Necessary before setting a configuration stanza belonging to the above app.

*   Set pass4SymmKey

*   Set indexer discovery pass4SymmKey

*   Restart Splunk
