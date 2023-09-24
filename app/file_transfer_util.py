import subprocess
import sys

def transfer_file(src_path, dest_ip, dest_path):
    scp_command = f'scp {src_path} {dest_ip}:{dest_path}'
    process = subprocess.Popen(scp_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Failed to transfer file: {stderr.decode()}")
        sys.exit(1)
    else:
        print(f"File transferred successfully to {dest_ip}")
