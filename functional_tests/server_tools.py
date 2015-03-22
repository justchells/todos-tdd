from os import path
import subprocess
THIS_FOLDER = path.dirname(path.abspath(__file__))
PATH_TO_FAB = 'C:\\Python\\Python27\\Scripts\\fab'

def create_session_on_server(host, email):
    return subprocess.check_output(
        [
            PATH_TO_FAB,
            'create_session_on_server:email={}'.format(email),
            '--host={}'.format(host),
            '--hide=everything, status',
        ],
        cwd=THIS_FOLDER
    ).decode().strip()

def reset_database(host):
    subprocess.check_call(
        [
            PATH_TO_FAB,
            'reset_database',
            '--host={}'.format(host)
        ],
        cwd=THIS_FOLDER
    )
