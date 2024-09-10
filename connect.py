import pexpect

hostname = "10.0.20.30"
username = "supascrtadminus3r"
password = "supascrtp4ssw0rd!!"

ssh_command = f"ssh {username}@{hostname}"
child = pexpect.spawn(ssh_command)
child.expect("password:")
child.sendline(password)
child.expect(["$", "#"])
child.interact()
child.sendline('top -b -n 1')
child.expect(["$", "#"])
child.sendline('exit')
child.expect(pexpect.EOF)

