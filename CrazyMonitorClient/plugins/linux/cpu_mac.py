#!/usr/bin/env python
#coding:utf-8

#apt-get install sysstat

import commands

def monitor(frist_invoke=1):
    shell_command = 'sar 1 3| grep "^Average:"'
    status,result = commands.getstatusoutput(shell_command)
    if status != 0:
        value_dic = {'status': status}
    else:
        value_dic = {}
        #print('---res:',result)
        user,nice,system,iowait,steal,idle = result.split()[2:]
        value_dic= {
            'user': user,
            'nice': nice,
            'system': system,
            'iowait': iowait,
            'steal': steal,
            'idle': idle

        }
    return value_dic

if __name__ == '__main__':
    print monitor()
