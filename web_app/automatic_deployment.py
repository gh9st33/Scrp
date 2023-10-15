```python
import paramiko
from scp import SCPClient

def deploy_scraper_agent(server_ip, username, password, scraper_agent_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_ip, username=username, password=password)

    scp = SCPClient(ssh.get_transport())
    scp.put(scraper_agent_file, '/tmp/scraper_agent.py')

    stdin, stdout, stderr = ssh.exec_command('python3 /tmp/scraper_agent.py')
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')

    if error:
        print(f"Error occurred: {error}")
    else:
        print(f"Output: {output}")

    scp.close()
    ssh.close()

def automatic_deployment():
    servers = [
        {"ip": "192.168.1.1", "username": "user1", "password": "pass1"},
        {"ip": "192.168.1.2", "username": "user2", "password": "pass2"},
        # Add more servers as needed
    ]

    for server in servers:
        deploy_scraper_agent(server['ip'], server['username'], server['password'], 'scraper_agent.py')

if __name__ == "__main__":
    automatic_deployment()
```