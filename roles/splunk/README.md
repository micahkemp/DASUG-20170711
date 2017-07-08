Ansible Role
============

Splunk
------------

Basic installation of Splunk

### Dependencies

*   splunklib-1.6.2

    Required for the custom Ansible modules to manage Splunk.

### Tasks

*   Set hostname

    Do this before starting Splunk so that serverName is set correctly.

*   Add Splunk user

*   Unpack Splunk tarball into Splunk Home

*   Start Splunk and Accept License

*   Enable boot-start

*   Change default password
