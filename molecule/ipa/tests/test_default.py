"""Role testing files using testinfra."""


def test_user_exists(host):
    command = r"""set -o pipefail && echo '123123123'| \
    kinit cmordant > /dev/null && \
    ipa user-find cmordant | \
    grep -c 'First name: Charlie'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_groups_cmordante_users(host):
    command = """set -o pipefail && echo '123123123'| \
    kinit cmordant > /dev/null && \
    ipa group-find --user=cmordant | grep -c 'cmordante'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_groups_wheel_users(host):
    command = """set -o pipefail && echo '123123123'| \
    kinit cmordant > /dev/null && \
    ipa group-find --user=cmordant | grep -c 'wheel'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout
