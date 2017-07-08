DASUG 2017-07-11
================

Deploying Splunk via Ansible
----------------------------

### Demo Components
*   Search Head
*   Cluster Master/Deployment Server/License Master
*   Indexers (2)
*   DMC
*   Heavy Forwarder

### ansible configuration files to configure to be deployment specific
*   hosts
*   files/
    Place Splunk tarball and Splunk Python SDK splunklib/ here
    splunk-6.6.2-4b804538c686-Linux-x86_64.tgz
    splunklib-1.6.2/splunklib
*   group_vars/splunk_servers
    This is where most deployment specific configurations go
    Define splunk installation path, new splunk password, splunk tarball filename, etc

### splunk app default/ configuration files to configure to be deployment specific
*   roles/splunk_cluster_slave/files/cluster_slave_app/default/server.conf
*   roles/splunk_deployment_client_app/files/deployment_client_app/default/deploymentclient.conf
*   roles/splunk_forwarder_outputs_app/files/forwarder_outputs_app/default/outputs.conf
*   roles/splunk_cluster_searchhead_app/files/cluster_searchhead_app/default/server.conf
*   roles/splunk_license_slave_app/files/license_slave_app/default/server.conf
