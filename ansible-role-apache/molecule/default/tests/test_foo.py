import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('foo')


def test_listen(host):
    f = host.socket("tcp://0.0.0.0:9999")

    assert f.is_listening
