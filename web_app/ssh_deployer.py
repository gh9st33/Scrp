```python
import paramiko

class SSHDeployer:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.client = None

    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.host, self.port, self.username, self.password)

    def run_command(self, command):
        if self.client is None:
            self.connect()
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read()

    def deploy_scraper(self, scraper_config):
        # Assuming scraper_config is a dictionary with necessary details
        # like scraper name, script location, dependencies etc.
        commands = [
            f"cd {scraper_config['location']}",
            "git pull",
            "pip install -r requirements.txt",
            f"scrapyd-deploy {scraper_config['project_name']} -p {scraper_config['project_name']}"
        ]
        for command in commands:
            print(self.run_command(command))

    def disconnect(self):
        if self.client:
            self.client.close()
            self.client = None
```
This is a simple SSH deployer class in Python using the paramiko library. It connects to a remote server using SSH, runs commands to update and deploy a scraper, and then disconnects. The `deploy_scraper` method assumes that the scraper is a git project with a `scrapyd.cfg` file and a `requirements.txt` file.