#!/usr/bin/python

import json

RELEASE_URL = "https://api.github.com/repos/%s/%s/releases"

def list_releases(token, owner, repo):
    releases_url = RELEASE_URL % (owner, repo)
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": ("token %s" % (token))
    }
    req = open_url(releases_url, headers=headers)
    return json.loads(req.read())

def main():
    module = AnsibleModule(
        argument_spec=dict(
            owner=dict(required=True),
            repo=dict(required=True),
            token=dict(required=True),
            prefix=dict(required=False, default=''),
        ),
        supports_check_mode=True
    )

    token = module.params['token']
    owner = module.params['owner']
    repo = module.params['repo']
    prefix = module.params['prefix']

    if module.check_mode:
        releases = []
    else:
        try:
            releases = list_releases(token, owner, repo)
        except Exception as err:
            return module.fail_json(msg=str(err))

    if prefix:
        releases = [r for r in releases if r['name'].startswith(prefix)]

    module.exit_json(results=releases)

from ansible.module_utils.basic import *
from ansible.module_utils.urls import *

if __name__ == '__main__':
    main()
