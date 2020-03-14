import paramiko
import re


def get_snapshot_id(ip, username, password, vmname):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, password, timeout=5)
        # 获取特定主机的VM ID
        cmd = "vim-cmd vmsvc/getallvms |grep " + vmname
        stdin, stdout, stderr = ssh.exec_command(cmd)
        x = stdout.read().decode()
        vmid = x.split()[0]
        # 获取特定主机的所有快照ID
        cmd = "vim-cmd vmsvc/snapshot.get " + vmid
        stdin, stdout, stderr = ssh.exec_command(cmd)
        y = stdout.read().decode()
        # print(y)

        snaptshot_id = []
        for line in y.split('\n'):
            if 'Snapshot Id' in line:
                # print(line)
                result = re.match('-+Snapshot Id\s+:\s+(\d*)', line).groups()
                # print(result)
                snaptshot_id.append(int(result[0]))
            # print(snaptshot_id)
        # 控制最多快照数量，返回需要删除的老快照ID
        if len(snaptshot_id) > 2:  # 控制最多快照数量
            i = 1
            while i <= 2:
                snaptshot_id.pop()
                i += 1
            return ip, vmid, vmname, snaptshot_id
        else:
            return None
        ssh.close()
    except Exception as e:
        print(e)
        print('%stErrorn' % ip)


if __name__ == '__main__':
    print(get_snapshot_id('172.16.1.201', 'root', 'Cisc0123', 'CentOS'))
