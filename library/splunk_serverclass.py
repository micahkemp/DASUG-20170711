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
            state=dict(type='str', default='present', choices=['present', 'absent']),
            whitelists=dict(type='list'),
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
        splunk_serverclass=module.params['name'],
    )

    serverclasses_path = 'deployment/server/serverclasses'
    serverclass_path   = "%s/%s" % (serverclasses_path, module.params['name'])

    serverclasses = client.Endpoint(service, serverclasses_path)

    create_params = {
        'name': module.params['name'],
    }
    update_params = { }

    if 'whitelists' in module.params and module.params['whitelists']:
        i = 0
        for whitelist in module.params['whitelists']:
            whitelist_name = "whitelist.%s" % i
            create_params[whitelist_name] = whitelist
            update_params[whitelist_name] = whitelist
            i = i+1

    if module.params['state'] == 'present':
        try:
            serverclass = client.Entity(service, serverclass_path)
            serverclass.post(**update_params)
        except:
            # only try to create if fetching it failed
            serverclasses.post(**create_params)
    else:
        try:
            serverclass = client.Entity(service, serverclass_path)
            serverclass.delete()
            result['changed'] = True
        except:
            result['changed'] = False

    module.exit_json(**result)

if __name__ == '__main__':
    main()
