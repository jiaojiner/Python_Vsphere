import paramiko

def remove_snapshot(ip,username,password,vmid,snapshotid):
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(ip,22,username,password,timeout=5)
		cmd = "vim-cmd vmsvc/snapshot.remove " + str(vmid) + " " + str(snapshotid)
		stdin,stdout,stderr = ssh.exec_command(cmd)
		x = stdout.read().decode()
		#print(x)
		ssh.close()
	except Exception as e:
		print(e)
		print('%stErrorn'%(ip))	

if __name__ == '__main__':
	remove_snapshot('172.16.1.201','root','Cisc0123',1,4)