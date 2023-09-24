#python ssh_util.py --key /path/to/private/key --server 192.168.1.1 --command "uptime"
#python ssh_util.py --key ~/.ssh/ssl-cert-manager --server 172.16.0.20 --command "uptime"

from paramiko import SSHClient, AutoAddPolicy
import argparse

def create_ssh_client(server_ip, key_path=None):
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    if key_path:
        ssh.connect(server_ip, key_filename=key_path)
    else:
        ssh.connect(server_ip)
    return ssh

def execute_command(ssh, command):
    stdin, stdout, stderr = ssh.exec_command(command)
    error = stderr.read().decode()
    if error:
        print(f"Failed to execute command: {error}")
    else:
        print(stdout.read().decode())

def close_ssh_client(ssh):
    ssh.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Execute commands on a remote server via SSH.')
    parser.add_argument('--server', required=True, help='IP address of the remote server')
    parser.add_argument('--command', required=True, help='Command to execute on the remote server')
    parser.add_argument('--key', help='Path to the authentication key', default=None)
    args = parser.parse_args()

    ssh = create_ssh_client(args.server, args.key)
    execute_command(ssh, args.command)
    close_ssh_client(ssh)
