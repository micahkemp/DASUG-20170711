#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

import sys
#sys.path.append('/tmp/splunklib-1.6.2')
#import splunklib.client as client

def main():
    module = AnsibleModule(
        argument_spec=dict(
            host=dict(type='str', default='localhost'),
            port=dict(type='str', default='8089'),
            auth_user=dict(type='str', required=True),
            auth_password=dict(type='str', required=True, no_log=True),
            name=dict(type='str', required=True),
            password=dict(type='str', no_log=True),
            realname=dict(type='str'),
            email=dict(type='str'),
            roles=dict(type='list'),
            state=dict(type='str', default='present', choices=['present', 'absent']),
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
        password=module.params['auth_password'])

    result = dict(
        splunk_user=module.params['name'],
    )

    if module.params['state']=='present':
        try:
            user = service.users[module.params['name']]
            created = False
        except:
            user = service.users.create(
                module.params['name'],
                module.params['password'],
                module.params['roles'],
            )
            created = True

        if created == False:
            if 'password' in module.params and module.params['password']:
                user.update(password=module.params['password'])
                result['password']='changed'

        if 'realname' in module.params and module.params['realname']:
            user.update(realname=module.params['realname'])
            result['realname']=module.params['realname']
        if 'email' in module.params and module.params['email']:
            user.update(email=module.params['email'])
            result['email']=module.params['email']
    else:
        service.users.delete(module.params['name'])

    module.exit_json(**result)


if __name__ == '__main__':
    main()
