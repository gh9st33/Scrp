```python
import paramiko

class SSHDeployment:

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        self.ssh.connect(self.host, self.port, self.username, self.password)

    def run_command(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        return stdout.read()

    def deploy_scraper(self, scraper_name):
        commands = [
            f"git clone https://github.com/your-repo/{scraper_name}.git",
            f"cd {scraper_name}",
            "pip install -r requirements.txt",
            "python main.py &"
        ]
        for command in commands:
            self.run_command(command)

    def disconnect(self):
        self.ssh.close()

if __name__ == "__main__":
    ssh_deployment = SSHDeployment('host', 'port', 'username', 'password')
    ssh_deployment.connect()
    ssh_deployment.deploy_scraper('scraper_name')
    ssh_deployment.disconnect()
```