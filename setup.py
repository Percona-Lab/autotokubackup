from setuptools import setup

datafiles = [('/etc', ['general_conf/tokubackup.conf'])]

setup(
    name='percona-autotokubackup',
    version='1.1',
    packages=['general_conf', 'backup'],
    py_modules=['tokubackup'],
    url='https://github.com/Percona-Lab/percona-autotokubackup',
    license='GPL',
    author='Shahriyar Rzayev',
    author_email='shahriyar.rzayev@percona.com',
    description='Commandline tool written in Python3 for using Percona TokuBackup',
    install_requires=[
        'click>=3.3',
        'mysql-connector>=2.0.2',
        'watchdog>=0.8.3'
    ],
    entry_points='''
        [console_scripts]
        tokubackup=tokubackup:all_procedure
    ''',
    data_files=datafiles,
)
