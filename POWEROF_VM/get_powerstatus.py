import paramiko
import re


def get_powerstatus(ip, username, password, vmid):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, password, timeout=5)
        cmd = "vim-cmd /vmsvc/power.getstate " + vmid
        stdin, stdout, stderr = ssh.exec_command(cmd)
        x = stdout.read().decode()
        for line in x.split('\n'):
            if re.match('.*Powered on.*', line.strip()):
                return (1)
            elif re.match('.*Powered off.*', line.strip()):
                return (2)
        ssh.close()
    except Exception as e:
        print(e)
        print('%stErrorn' % (ip))


if __name__ == '__main__':
    print(get_powerstatus('172.16.1.201', 'root', 'Cisc0123', '1'))
