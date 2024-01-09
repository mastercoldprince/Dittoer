import argparse
import os
import subprocess
from datetime import datetime

# Set up the argument parser
parser = argparse.ArgumentParser(description='Backup or upload specific subdirectories of ditto.')
parser.add_argument('-l', action='store_true', help='Backup specified subdirectories from server to local machine')
parser.add_argument('-r', action='store_true', help='Backup specified subdirectories to remote server directory')
parser.add_argument('-p', action='store_true' , help='Upload specified subdirectory to remote home directory')
parser.add_argument('subdirectories', nargs='+', help='The subdirectories of ditto to backup or upload')
# Parse the arguments
args = parser.parse_args()
# Define the server list
server_list = [
    "node-0",
]

update_code_list = [
    "node-0",
    "node-1",
    "node-2",
        ]
# update_code_list = [
#     "node-0",
#     "node-1",
#     "node-2",
#     "node3",
#     "node4",
#     "node5",
#     "node6",
#     "node7",
#     "node8",
#     "node9",
#         ]
# User
user = 'coldp'

# Function to execute shell commands and provide feedback
def execute_command(command):
    try:
        result = subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Success: {result.stdout}")
        if result.stderr:
            print(f"Error: {result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}: {e.cmd}")
        print(f"Error message: {e.stderr}")

# Function to upload directories to servers
def upload_directories(local_directory, remote_directory, servers):
    for server in servers:
        print(f"Uploading {local_directory} to {server}:{remote_directory}...")
        execute_command(f"rsync -avz {local_directory} {user}@{server}:{remote_directory}")

# Function to backup or upload subdirectories of ditto
def handle_subdirectories(operation, subdirectories, local_path=None):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

    for subdirectory in subdirectories:
        ditto_subdir_backup = f"ditto_{timestamp}"
        upload_remote_path = "~/Ditto/"
        remote_path = f"~/Ditto/{subdirectory}"
        if operation == 'backup':
            for server in server_list:
                if local_path:
                    # Backup to local machine
                    local_backup_path = os.path.join(local_path, ditto_subdir_backup)
                    print(f"Backing up {subdirectory} from {server} to local {local_backup_path}...")
                    execute_command(f"scp -r {user}@{server}:{remote_path} {local_backup_path}")
                else:
                    # Backup to remote server
                    remote_backup_path = f"~/{ditto_subdir_backup}"
                    print(f"Backing up {subdirectory} on {server} to {remote_backup_path}...")
                    execute_command(f"ssh {user}@{server} 'mkdir -p {remote_backup_path} && cp -r {remote_path} {remote_backup_path}'")
        elif operation == 'upload':
            for server in update_code_list:
                print(f"Uploading {local_path} to {server}:{upload_remote_path}...")
                # execute_command(f"scp -r {local_path} {user}@{server}:{remote_path}")
                execute_command(f"rsync -avz {local_path} {user}@{server}:{upload_remote_path}")

# Perform the backup to local or remote
if args.l:
    local_backup_dir = './backup'
    if not os.path.exists(local_backup_dir):
        os.makedirs(local_backup_dir)
    handle_subdirectories('backup', args.subdirectories, local_path=local_backup_dir)

if args.r:
    handle_subdirectories('backup', args.subdirectories)

# Upload the folders if the -p option is given
if args.p:
    for subdirectory in args.subdirectories:
        local_path = subdirectory
        handle_subdirectories('upload', [subdirectory], local_path=local_path)
