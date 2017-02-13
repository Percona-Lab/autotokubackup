import click
import runpy
import os
import re
from backup import backup_calculation


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo("Developed by Shahriyar Rzayev from Percona")
    click.echo("Link : https://github.com/Percona-Lab/autotokubackup")
    click.echo("Email: shahriyar.rzayev@percona.com")
    click.echo(
        "Based on Percona TokuBackup: https://www.percona.com/doc/percona-server/5.6/tokudb/toku_backup.html")
    click.echo('AutoTokuBackup Version 1.2')
    ctx.exit()


def check_file_content(file):
    """Check if all mandatory headers and keys exist in file"""
    config_file = open(file, 'r')
    file_content = config_file.read()
    config_file.close()

    config_headers = ["MySQL", "Backup", "Copy"]
    config_keys = [
        "mysql",
        "user",
        "port",
        "password",
        "socket",
        "host",
        "datadir",
        "backupdir"]

    for header in config_headers:
        if header not in file_content:
            raise KeyError(
                "Mandatory header [%s] doesn't exist in %s" %
                (header, file))

    for key in config_keys:
        if key not in file_content:
            raise KeyError(
                "Mandatory key \'%s\' doesn't exists in %s." %
                (key, file))

    return True


def validate_file(file):
    """
    Check for validity of the file given in file path. If file doesn't exist or invalid
    configuration file, throw error.
    """
    if os.path.isfile(file):
        # filename extension should be .conf
        pattern = re.compile(r'.*\.conf')

        if pattern.match(file):
            # Lastly the file should have all 5 required headers
            if check_file_content(file):
                return
        else:
            raise ValueError("Invalid file extension. Expecting .conf")
    else:
        raise FileNotFoundError("Specified file does not exist.")


@click.command()
@click.option(
    '--backup',
    is_flag=True,
    help="Take full backup using TokuBackup.")
@click.option(
    '--version',
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Version information.")
@click.option(
    '--defaults_file',
    default='/etc/tokubackup.conf',
    help="Read options from the given file")

def all_procedure(backup, defaults_file):

    validate_file(defaults_file)

    if (not backup) and (not defaults_file):
        print("ERROR: you must give an option, run with --help for available options")
    elif backup:
        # runpy.run_module(backup_calculation.main(defaults_file))
        backup_calculation.main(defaults_file)


if __name__ == "__main__":
    all_procedure()
