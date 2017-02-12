
Percona-AutoTokuBackup
====================

Percona AutoTokuBackup commandline tool written in Python 3.
You can use this script to automate the usage of Percona TokuBackup.
Also you can optionally specify which files to copy during backup process.



Requirements:
-------------

    * Percona Server with enabled TokuDB engine & TokuBackup plugin
    * Python 3 (tested version 3.5.3)


Installing
-----------------

    From source:
    
    cd /home
    git clone https://github.com/Percona-Lab/percona-autotokubackup.git
    cd percona-autotokubackup
    python3 setup.py install
    
    Via pip3:
    
    pip3 install percona-autotokubackup
    
    > Python package dependencies will be installed automatically.
    
    
    
Project Structure:
------------------

    Here is project path tree:
    
        * backup                        -- Backup main logic goes here.(backup_calculation.py)
	* general_conf                  -- All-in-one config file and config reader class(generalops.py).
    	* setup.py                      -- Setuptools Setup file.
    	* tokubackup.py                 -- Commandline Tool provider script.
    	* /etc/tokubackup.conf          -- Main config file will be created from general_conf/tokubackup.conf file
    	

Configuration file:
-------------------

	[MySQL]
	mysql=/usr/bin/mysql
	user=root
	password=12345
	port=3306
	socket=/var/run/mysqld/mysqld.sock
	host=localhost
	datadir=/var/lib/mysql
	
	
	[Backup]
	backupdir=/var/lib/tokubackupdir
	
	[Copy]
	# The following copy_file_x options allow you to copy various files together with your backup
	# Highly recommended; a copy of your my.cnf file (usually /etc/my.cnf) and any cnf files referenced from it (i.e. includedir etc.)
	# You can also include other files you would like to take a copy of, like for example a text report or the mysqld error log
	# copy_file_1=
	# copy_file_2=
	# copy_file_...=
	# copy_file_10=
	
	#copy_file_1=/etc/my.cnf
	#copy_file_2=/var/log/messages
	#copy_file_3=
	#copy_file_4=
	#copy_file_5=
	#copy_file_6=
	#copy_file_7=
	#copy_file_8=
	#copy_file_9=
	#copy_file_10=


General Usage:
-------------
        1. Install using mentioned methods. 
        3. Edit /etc/tokubackup.conf file to reflect your settings and start to use.
        

Sample Output:
-------------

    tokubackup --help
    Usage: tokubackup [OPTIONS]

    Options:
    --backup              Take full backup using TokuBackup.
    --version             Version information.
    --defaults_file TEXT  Read options from the given file
    --help                Show this message and exit.

      
      
    # tokubackup --version
    Developed by Shahriyar Rzayev from Percona
    Link : https://github.com/Percona-Lab/percona-autotokubackup
    Email: shahriyar.rzayev@percona.com
    Based on Percona TokuBackup: https://www.percona.com/doc/percona-server/5.6/tokudb/toku_backup.html
    MySQL-AutoTokuBackup Version 1.1

    
    
    # tokubackup --backup --defaults_file=/etc/tokubackup_node2.conf 
    Backup will be stored in  /var/lib/tokubackupdir/2017-02-09_20-25-40
    Running backup command => /home/sh/percona-server/5.7.17/bin/mysql -uroot --password=msandbox --host=localhost --socket=/tmp/mysql_sandbox20194.sock -e set tokudb_backup_dir='/var/lib/tokubackupdir/2017-02-09_20-25-40'
    mysql: [Warning] Using a password on the command line interface can be insecure.
    Created file in backup directory -> /var/lib/tokubackupdir/2017-01-31_14-15-46/mysql_data_dir/__tokudb_lock_dont_delete_me_data
    Created file in backup directory -> /var/lib/tokubackupdir/2017-01-31_14-15-46/mysql_data_dir/__tokudb_lock_dont_delete_me_logs
    Created file in backup directory -> /var/lib/tokubackupdir/2017-01-31_14-15-46/mysql_data_dir/__tokudb_lock_dont_delete_me_temp
    Created file in backup directory -> /var/lib/tokubackupdir/2017-01-31_14-15-46/mysql_data_dir/log000000000006.tokulog29
    Created file in backup directory -> /var/lib/tokubackupdir/2017-01-31_14-15-46/mysql_data_dir/tokudb.rollback
    Created file in backup directory -> /var/lib/tokubackupdir/2017-01-31_14-15-46/mysql_data_dir/tokudb.environment
    Created file in backup directory -> /var/lib/tokubackupdir/2017-01-31_14-15-46/mysql_data_dir/tokudb.directory
    Created file in backup directory -> /var/lib/tokubackupdir/2017-01-31_14-15-46/mysql_data_dir/tc.log
    Created file in backup directory -> /var/lib/tokubackupdir/2017-01-31_14-15-46/mysql_data_dir/client-key.pem
    Created file in backup directory -> /var/lib/tokubackupdir/2017-01-31_14-15-46/mysql_data_dir/server-cert.pem
    Created file in backup directory -> /var/lib/tokubackupdir/2017-01-31_14-15-46/mysql_data_dir/server-key.pem
    Created file in backup directory -> /var/lib/tokubackupdir/2017-01-31_14-15-46/mysql_data_dir/ca.pem
    Created file in backup directory -> /var/lib/tokubackupdir/2017-01-31_14-15-46/mysql_data_dir/ca-key.pem
    Created file in backup directory -> /var/lib/tokubackupdir/2017-01-31_14-15-46/mysql_data_dir/auto.cnf
    Completed - OK


Supplementary Files
-------------------

The MySQL Global and Session variable values will be stored in backup directory. 
If you specify some files to copy in configuration file, they will be stored inside 'copied_files' directory.

    # ls -l 2017-02-09_20-25-40/
    
      copied_files            - Directory for copied files.
      global_variables        - File for MySQL global variables. 
      mysql_data_dir          - Directory for copied MySQL datadir.
      session_variables       - File for MySQL session variables. 
      tokubackup_binlog_info  - File for storing binary log position.
      tokubackup_slave_info   - File for storing slave info.




