from paramiko import SSHClient, AutoAddPolicy
import sys

def create_ssh_client(server_ip):
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(server_ip)
    return ssh

def execute_command(ssh, command):
    stdin, stdout, stderr = ssh.exec_command(command)
    error = stderr.read().decode()
    if error:
        print(f"Failed to execute command: {error}")
        sys.exit(1)
    else:
        print(stdout.read().decode())

def close_ssh_client(ssh):
    ssh.close()
