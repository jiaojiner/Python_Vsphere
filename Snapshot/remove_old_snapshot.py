from device_info import vms
from get_snapshot_info import get_snapshot_id
from remove_snapshot import remove_snapshot

username = 'root'
password = 'Cisc0123'

need_remove = []


def remove_old_snapshot():
    # 找到需要删除的快照
    for vmname, esxiip in vms.items():
        result = get_snapshot_id(esxiip, username, password, vmname)
        # print(vmname,result)
        if result != None:
            need_remove.append(result)
    # print(need_remove)
    # 删除快照
    for snapshot_need_remove in need_remove:
        for snapshot_need_remove_id in snapshot_need_remove[3]:
            print('移除' + snapshot_need_remove[2] + '的第' + str(snapshot_need_remove_id) + '号快照！')
            remove_snapshot(snapshot_need_remove[0], username, password, snapshot_need_remove[1],
                            snapshot_need_remove_id)


if __name__ == '__main__':
    remove_old_snapshot()
