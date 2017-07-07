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
            app=dict(type='str', required=True),
            file=dict(type='str', required=True),
            stanza=dict(type='str', required=True),
            values=dict(type='dict', required=True),
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
        app=module.params['app'],
    )

    result = dict(
        splunk_app=module.params['app'],
        splunk_file=module.params['file'],
        splunk_stanza=module.params['stanza'],
        splunk_values={},
    )

    conf_file_path = "configs/conf-%s" % (module.params['file'])
    conf_stanza_path = "%s/%s" % (conf_file_path, module.params['stanza'])

    try:
        conf_file = client.Endpoint(service, conf_file_path)
        conf_file.post(name=module.params['stanza'])
        result['splunk_stanza_created'] = True
    except:
        result['splunk_stanza_created'] = False

    conf_stanza = client.Endpoint(service, conf_stanza_path)
    for key in module.params['values']:
        key_value = {key: module.params['values'][key]}
        conf_stanza.post(**key_value)
        result['splunk_values'][key] = module.params['values'][key]

    module.exit_json(**result)


if __name__ == '__main__':
    main()
