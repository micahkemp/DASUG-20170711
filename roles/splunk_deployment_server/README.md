Ansible Role
========================

splunk_deployment_server
------------------------

### Dependencies

*   splunk_deployment_client_app

    Installed to deployment-apps/deployment_client_app

    The app folder name has to be defined for deployment_client_app, as it gets
    a different folder name when installed to deployment clients directly.

*   splunk_cluster_searchhead_app

    Installed to etc/deployment-apps

*   splunk_forwarder_outputs_app

    Installed to etc/deployment-apps

*   splunk_license_slave_app

    Installed to etc/deployment-apps

### Tasks

*   Create License Slaves serverclass

    Whitelist search heads, forwarders, cluster master, dmc.

    Don't add whitelists for the demo, due to lack of appropriate license.

*   Add license_slave_app to License Slaves serverclass

*   Create Cluster Search Head serverclass

    Whitelist search heads, dmc

*   Add cluster_searchhead_app to Cluster Search Head serverclass

*   Create Deployment Clients serverclass

    Whitelist everything.

*   Add deployment_client_app to Deployment Clients serverclass

*   Create Forwarders serverclass

    Whitelist everything.

*   Add forwarder_outputs_app to Forwarders serverclass
