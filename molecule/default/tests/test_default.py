import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pwsh_lnk(host):
    f = host.file('/usr/bin/pwsh')
    assert f.exists
    assert f.is_symlink
