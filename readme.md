# ansible-github-releases

An ansible module for listing github releases (and maybe more, soon).

## example usage

```yml
#!/usr/bin/env ansible-playbook
---
- hosts: localhost
  name: list github releases
  vars:
    owner: 'chesles'
    repo: 'ansible-github-releases'
    token: 'your-oauth-token'

  tasks:
    - name: List GitHub releases
      github_release_find:
        owner: "{{ owner }}"
        repo: "{{ repo }}"
        token: "{{ token }}"
      register: release

    - debug: msg="Release {{ release }}"
```
