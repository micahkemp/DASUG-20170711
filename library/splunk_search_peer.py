#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

import sys

def main():
    module = AnsibleModule(
        argument_spec=dict(
            host=dict(type='str', default='localhost'),
            port=dict(type='str', default='8089'),
            auth_user=dict(type='str', required=True),
            auth_password=dict(type='str', required=True, no_log=True),
            name=dict(type='str', required=True),
            # there's no DELETE mothod shown in the API docs, so only 'present' is supported for now
            state=dict(type='str', default='present', choices=['present']),
            remote_user=dict(type='str', required=True),
            remote_password=dict(type='str', required=True, no_log=True),
            splunklib=dict(type='str'),
        ),
        supports_check_mode=True
    )

    if 'splunklib' in module.params:
        sys.path.append(module.params['splunklib'])

    import splunklib.client as client

    service = client.connect(
        host=module.params['host'],
        port=module.params['port'],
        username=module.params['auth_user'],
        password=module.params['auth_password'],
    )

    result = dict(
        splunk_search_peer=module.params['name'],
    )

    search_peers_path = 'search/distributed/peers'
    search_peer_path  = "%s/%s" % (search_peers_path, module.params['name'])

    search_peers = client.Endpoint(service, search_peers_path)

    create_params = {
        'name': module.params['name'],
        'remoteUsername': module.params['remote_user'],
        'remotePassword': module.params['remote_password'],
    }

    update_params = {
        'remoteUsername': module.params['remote_user'],
        'remotePassword': module.params['remote_password'],
    }

    if module.params['state'] == 'present':
        try:
            search_peer = client.Entity(service, search_peer_path)
            search_peer.post(**update_params)
        except:
            # only try to create if fetching it failed
            search_peers.post(**create_params)
    else:
        # not supported, and only 'present' is allowed, so do nothing for now
        pass

    module.exit_json(**result)

if __name__ == '__main__':
    main()
