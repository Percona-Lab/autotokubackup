#!/opt/Python3/bin/python3

import configparser
from os.path import isfile
import sys


class GeneralClass(object):

    def __init__(self, config='/etc/tokubackup.conf'):

        if isfile(config):
            con = configparser.ConfigParser()
            con.read(config)

            DB = con['MySQL']
            self.mysql = DB['mysql']
            self.mysql_user = DB['user']
            self.mysql_password = DB['password']
            self.mysql_port = DB['port']
            if 'socket' in DB:
                self.mysql_socket = DB['socket']
            self.mysql_host = DB['host']
            self.datadir = DB['datadir']

            ######################################################

            BCK = con['Backup']
            self.backupdir = BCK['backupdir']

            ######################################################
            self.to_be_copied = []
            CP = con['Copy']
            for i in range(1, 11):
                if 'copy_file_{}'.format(i) in CP:
                    if isfile(CP['copy_file_{}'.format(i)]):
                        self.to_be_copied.append(CP['copy_file_{}'.format(i)])
                    else:
                        print("WARN: specified file can not be copied")

        else:
            print("CRITICAL: Missing config file : /etc/tokubackup.conf")
            sys.exit(-1)
