from general_conf.generalops import GeneralClass
import click
from subprocess import Popen


class SysbenchRun(GeneralClass):

    def __init__(self, config):
        self.conf = config
        super().__init__(self.conf)

    def create_sysbench_command(self, sysbench_action):
        command = "sysbench  %s" \
                          " --mysql-db=%s " \
                          " --mysql-user=%s --mysql-password=%s --db-driver=mysql " \
                          " --max-requests=0  --mysql-socket=%s %s"
        general_command = (command) % (self.sysbench_options, self.sysbench_db,
                                       self.mysql_user, self.mysql_user,
                                       self.mysql_socket, sysbench_action)
        return general_command

    def run_sysbench(self, command_to_run):

        process = Popen(
            command_to_run,
            stdin=None,
            stdout=None,
            stderr=None)




@click.command()
@click.option(
    '--prepare',
    is_flag=True,
    help="Run sysbench prepare")

@click.option(
    '--run',
    is_flag=True,
    help="Run sysbench run"
)
@click.option(
    '--defaults_file',
    default='/etc/tokubackup.conf',
    help="Read options from the given file")

def all_procedure(prepare, run, defaults_file):
    if (not prepare) and (not defaults_file) and (not run):
        print("ERROR: you must give an option, run with --help for available options")
    elif prepare:
        obj = SysbenchRun(defaults_file)
        command_to_run = obj.create_sysbench_command(sysbench_action=prepare)
        obj.run_sysbench(command_to_run=command_to_run)
    elif run:
        obj = SysbenchRun(defaults_file)
        command_to_run = obj.create_sysbench_command(sysbench_action=run)
        obj.run_sysbench(command_to_run=command_to_run)


if __name__ == "__main__":
    all_procedure()