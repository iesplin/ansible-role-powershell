ansible-role-powershell
=========

**This role is no longer maintained as Kali now includes PowerShell in its repository.**

Ansible role for installing Powershell in Kali

Role Variables
--------------

powershell_user_profile: /root/.bashrc
powershell_disable_telemetry: true

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: ansible-role-powershell

License
-------

MIT
