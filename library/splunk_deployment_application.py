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
            serverclass=dict(type='str', required=True),
            state=dict(type='str', default='present', choices=['present', 'absent']),
            restartSplunkd=dict(type='bool', required=True),
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
        splunk_deployment_application=module.params['name'],
        splunk_serverclass=module.params['serverclass'],
    )

    application_path = "deployment/server/applications/%s" % module.params['name']
    application = client.Endpoint(service, application_path)

    post_params = {
        'serverclass': module.params['serverclass'],
    }

    if module.params['state'] == 'absent':
        post_params['unmap'] = True

    if module.params['restartSplunkd']:
        post_params['restartSplunkd'] = True
    else:
        post_params['restartSplunkd'] = False

    application.post(**post_params)

    module.exit_json(**result)

if __name__ == '__main__':
    main()
