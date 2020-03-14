from shutdown_vm import shutdown_vm
from get_shutdown_vm import get_shudown_vm
from get_powerstatus import get_powerstatus

# 配置一系列ESXi的地址
servers = ['172.16.1.201']
# 配置登录账号
username = 'root'
password = 'Cisc0123'


def shutdown_vm_daily():
    # 获取所有需要shutdown虚拟机的ID
    vms_dict = {}
    for server in servers:
        vms_dict[server] = get_shudown_vm(server, username, password)

    print(vms_dict)

    vms_poweron = {}
    # 获取所有需要shutdown虚拟机中的那些处于开机状态的虚拟机ID
    for server, vms in vms_dict.items():
        vms_poweron_list = []
        try:
            for vm in vms:
                if get_powerstatus(server, username, password, vm) == 1:
                    vms_poweron_list.append(vm)
        except:
            pass
        vms_poweron[server] = vms_poweron_list

    print(vms_poweron)
    # shutdown虚拟机
    for server, vms in vms_poweron.items():
        for vm in vms:
            shutdown_vm(server, username, password, vm)


if __name__ == '__main__':
    shutdown_vm_daily()
