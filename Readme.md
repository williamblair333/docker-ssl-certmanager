# Docker SSL Cert Manager

Docker SSL Cert Manager is a Dockerized solution for managing SSL/TLS certificates for your local domains using a private Certificate Authority (CA). This project encapsulates the process of certificate generation, distribution to a web server, executing arbitrary commands on the remote server, and restarting the web server, all within a Docker container.

## Features

- Setup a private Certificate Authority (CA) to issue certificates for local domains.
- Automated certificate generation for specified domains.
- Secure transfer of certificates to a remote web server.
- Execution of arbitrary commands on the remote server.
- Automated web server restart to apply the new certificates.

## Prerequisites

- Docker
- Docker Compose

## Directory Structure

docker-ssl-cert-manager/
├── Dockerfile: Defines the Docker container including the necessary dependencies.
├── docker-compose.yml: Docker Compose configuration file.
├── file_transfer_util.py: Utility for transferring files to remote servers.
├── setup-cert.py: Script to generate SSL certificates.
├── ssh_util.py: Utility for creating SSH connections and executing commands on remote servers.
├── web_server_util.py: Script to restart the web server on a remote server.

## Getting Started

1. **Clone this repository to your local machine**:
    ```bash
    git clone https://github.com/williamblair333/docker-ssl-cert-manager.git
    cd docker-ssl-cert-manager
    ```
2. **Generate a certificate for a domain**:

    ```bash
    docker-compose run ca python setup-cert.py mydomain
    ```

3. **Transfer the generated certificate and key to a remote server**:

    ```bash
    docker-compose run ca python file_transfer_util.py /certs/mydomain.crt user@remote-server:/path/to/certs/
    docker-compose run ca python file_transfer_util.py /certs/mydomain.key user@remote-server:/path/to/certs/
    ```

4. **Restart the web server on the remote server to apply the new certificate**:

    ```bash
    docker-compose run ca python web_server_util.py user@remote-server apache2
    ```

    Replace `apache2` with `nginx` or other web server software if necessary.

## Notes, Security

- Ensure that your SSH keys and other sensitive data are securely handled and not exposed to unauthorized individuals or systems. 
- This project is intended for local development and testing purposes and may need additional security hardening for production use.

## Notes, General

- The `docker-compose run` commands allow you to execute the scripts within the Docker container while interacting with remote servers.
- Ensure the remote server accepts SSH connections and the specified user has the necessary permissions to write to the `/path/to/certs/` directory and restart the web server.
