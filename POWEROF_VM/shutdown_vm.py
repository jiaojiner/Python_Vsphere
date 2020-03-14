import paramiko

def shutdown_vm(ip,username,password,vmid):
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(ip,22,username,password,timeout=5)
		cmd = "vim-cmd vmsvc/power.off " + vmid
		stdin,stdout,stderr = ssh.exec_command(cmd)
		x = stdout.read().decode()
		#print(x)
		ssh.close()
	except Exception as e:
		print(e)
		print('%stErrorn'%(ip))	

if __name__ == '__main__':
	shutdown_vm('172.16.1.201','root','Cisc0123','1')