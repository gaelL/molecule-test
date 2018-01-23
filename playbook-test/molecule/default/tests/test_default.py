import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


# Example of URI curl

# With curl
# def test_curl_homepage(host):
#     f = host.run("curl -s  localhost:9090/graph | grep '<title>Prometheus'")
#
#     assert f.rc == 0

# With ansible
#def test_homepage(host):
#
#    r = host.ansible("uri", "url=http://localhost:9090/graph return_content=yes", check=False)
#
#    assert '<title>Prometheus' in r['content']

