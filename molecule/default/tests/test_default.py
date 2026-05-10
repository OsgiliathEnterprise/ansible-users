"""Role testing files using testinfra."""


def test_user_exists(host):
    command = r"""set -o pipefail && echo '123ADMin'| \
    kinit admin > /dev/null && \
    ipa user-find cmordant | \
    grep -c 'First name: Charlie'"""
    with host.sudo():
        cmd = host.run(command)
    assert '1' in cmd.stdout


def test_user_mail_exists(host):
    command = r"""set -o pipefail && echo '123ADMin'| \
    kinit admin > /dev/null && \
    ipa user-find cmordant | \
    grep -c ' Email address: cmordant@osgiliath.test'"""
    with host.sudo():
        cmd = host.run(command)
    assert '1' in cmd.stdout


def test_groups_cmordante_users(host):
    command = """set -o pipefail && echo '123ADMin'| \
    kinit admin > /dev/null && \
    ipa group-find --user=cmordant | grep -c 'cmordante'"""
    with host.sudo():
        cmd = host.run(command)
    assert '1' in cmd.stdout


def test_groups_wheel_users(host):
    command = """set -o pipefail && echo '123ADMin'| \
    kinit admin > /dev/null && \
    ipa group-find --user=cmordant | grep -c 'wheel'"""
    with host.sudo():
        cmd = host.run(command)
    assert '1' in cmd.stdout
