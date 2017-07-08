Custom Splunk Ansible Modules
=============================

common fields used by all
-----------------------------

### Fields

*   host (optional, defaults to localhost)

    Splunk host to make changes to.  Typically fine to leave as default 'localhost'
    when having Ansible run the script on the Splunk host itself.

*   port (optional, defaults to 8089)

*   auth_user 

    Username to use when authenticating to the Splunk host.

*   auth_password

    Password to use when authenticating to the Splunk host.

*   splunklib (optional, can be left out if python can find splunklib on its own)

    Location (local to the Splunk host) of the splunklib directory.  For this demo
    there is also a splunklib-1.6.2 role will will install the expected version
    on the Splunk host.

splunk_config_stanza
-----------------------------

### Purpose

Add values to configuration files, specified by application, file, stanza, and key.

### Fields

*   app

    The path of the application to which the change should be made.  Used to avoid
    making changes to the system/ configs.

*   file

    The name of the file (sans .conf extension) to which the changes should be made.

*   stanza

    The name of the stanza in which to add values.

*   values

    A dictionary of key/value pairs to add.

splunk_deployment_application
-----------------------------

### Purpose

Configure deployment application's associated serverclasses and restartSplunkd status.

### Fields

*   name

    The name of the application in deployment-apps.

*   serverclass

    The name of the serverclass associated with the application

*   state

    The desired state (present/absent) of the serverclass's association with the application.

*   restartSplunkd

    Boolean value indicating if the application should trigger a splunkd restart upon
    deployment.

splunk_search_peer
-----------------------------

### Purpose

Add search peers (removing not yet supported).

### Fields

*   name

    The name of the search peer (in hostname:port format)

*   state

    Only 'present' is currently supported, as there was no reference to a DELETE method for
    remote search peers.

*   remote_user

    The username to use for authentication to the remote search peer.

*   remote_password

    The password to use for authentication to the remote search peer.

splunk_serverclass
-----------------------------

### Purpose

Add/remove serverclasses, and specify whitelists.

### Fields

*   name

    The name of the serverclass being managed.

*   state

    The desired state of the serverclass (present/absent).

*   whitelists

    Array of whitelists to be configured for this serverclass.  Only the whitelist itself is
    given here, the numbering (whitelist.0, etc) is done based on order supplied.

splunk_user
-----------------------------

### Purpose

Add/remove Splunk users, and change password, name, and roles.

### Fields

* name

    The username being managed.

* password

    The user's password, if being added or changed.

* email

    The user's email address, if being added or changed.

* roles

    Array of roles to associate with the user, if being added or changed.

* state

    The desired state of the user (present/absent).
