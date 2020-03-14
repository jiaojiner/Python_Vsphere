import paramiko


def get_shudown_vm(ip, username, password):
    result = []
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, password, timeout=5)
        cmd = "vim-cmd vmsvc/getallvms | grep vSphere"
        stdin, stdout, stderr = ssh.exec_command(cmd)
        a = stdout.read().decode()

        for line in a.split('\n'):
            if line == '':
                next
            elif 'vSphere' in line.split()[1]:
                result.append(line.split()[0])
        return result
        ssh.close()
    except Exception as e:
        print(e)
        print('%stErrorn' % ip)


if __name__ == '__main__':
    print(get_shudown_vm('172.16.1.201', 'root', 'Cisc0123'))
