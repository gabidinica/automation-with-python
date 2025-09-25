# Demo Project: Website Monitoring and Recovery

## Technologies Used
- Python
- Linode
- Docker
- Linux

## Project Description
This project involves setting up a website monitoring and recovery system on a cloud server.

### Steps:
1. **Server Setup**
   - Create a server on a cloud platform (Linode).
   
2. **Docker Deployment**
   - Install Docker on the remote server.
   - Run a Docker container to host the application.
   
3. **Website Monitoring**
   - Write a Python script that monitors the website by accessing it and validating the HTTP response.
   
4. **Notification System**
   - Write a Python script that sends an email notification when the website is down.
   
5. **Automatic Recovery**
   - Write a Python script that automatically restarts the application and server when the application is down.

----

## Create a Server on a Cloud Platform (Linode)

1. **Go to Linode**: [https://cloud.linode.com/linodes](https://cloud.linode.com/linodes)  
2. **Click "Create Linode"**  

3. **Configure Linode:**
   - **Image:** Debian 11  
   - **Region:** Frankfurt (eu-central)  
   - **Linode Plan:** Click on **Shared CPU** and select **Linode 2GB server**  
   - **Root Password:** Type a secure password  
   - **SSH Keys:**  
     1. Click on **Add an SSH Key**  
     2. Label it: `Python-monitoring`  
     3. Get your public SSH key from your terminal:  
        ```bash
        cat ~/.ssh/id_ed25519.pub
        ```  
     4. Copy the output and paste it into the Linode SSH Key window  
     5. Click **Add Key**  

4. **Create Linode** by clicking the **Create Linode** button.
5. **Copy SSH Access Command**  
   - From the Linode dashboard, copy the SSH access command:  
     ```bash
     ssh root@your-ip
     ```
   
6. **Login as Root User**  
   - Paste the command into your terminal and press **Enter**.  
   - You will now be logged in as the **root user** on your Linode server.
7. **Verify OS Version**  
   - Check the OS release to confirm you are on Debian 11:  
     ```bash
     cat /etc/os-release
     ```  
   - Example output:  
     ```
     PRETTY_NAME="Debian GNU/Linux 11 (bullseye)"
     ```

8. **Install Docker**  
   - Follow the official Docker installation guide for Debian:  
     [https://docs.docker.com/engine/install/debian/](https://docs.docker.com/engine/install/debian/)

### Run Nginx Container with Docker

1. **Start Nginx Container**  
   ```bash
   docker run -d -p 8080:80 nginx
   ```

2. Check Running Containers: `docker ps`
3. To access the application, open a web browser and paste: `http://<your-public-ip>:8080`


- **Access the Webpage Using DNS Name**  
   - In the script, we will access the page using its DNS name.

- **Install Required Library**  
   - To make HTTP requests, install the `requests` library:  
     ```bash
     pip install requests
     ```

- **View Webpage Content**  
   - To see the exact text from the webpage, use:  
     ```python
     print(response.text)
     ```

-  **Send Email Notifications**  
   - To send email when the website is down, use the built-in Python module `smtplib`.

### Gmail Setup for Sending Emails via Python

1. **Two-Factor Authentication (2FA) Considerations**  
   - Gmail supports 2FA.  
   - If **2FA is NOT enabled**, you can allow your Gmail account to accept access from programs/apps:  
     [https://myaccount.google.com/lesssecureapps](https://myaccount.google.com/lesssecureapps)  
   - Turn on the toggle to allow less secure app access.
2. **If 2FA is Enabled**  
   - The toggle for less secure apps will no longer be available.  
   - This option does **not work with multi-factor authentication (MFA)**.
3. **Generate an App Password**  
   - If 2FA is activated, go to: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)  
   - Create a new app password:
     - Name: `website-monitor`  
     - Click **Generate**  
   - Copy the generated password.

4. Paste the generated password into your Python script to allow it to send emails.
5. Store sensitive information like email passwords as **environment variables** instead of hardcoding them in the script.

- To set the environment variables as global: cat ~/.bash_profile
To simulate a connection error, stop the docker container and then run the script.

### Restart the Application

1. **Connect to Linode Server via SSH**  
2. **Execute Docker Start**  
   - Run the command on the server to restart the container:  
     ```bash
     docker start <container-name>
     ```

3. **Use Paramiko for SSH in Python**  
   - Install the library:  
     ```bash
     pip install paramiko
     ```
   - Connect to your server using Paramiko:  
     ```python
     import paramiko

     ssh = paramiko.SSHClient()
     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     ssh.connect(
         'public-ip-address-of-your-server',  # Replace with your server's public IP
         username='root',
         key_filename='your-home-directory/.ssh/id_ed25519'  # Replace with your home directory
     )
     ```

## Using Linode API in Python

1. **Install Linode Python Library**  
   - Library: [https://pypi.org/project/linode-api4/](https://pypi.org/project/linode-api4/)  
   - Install with pip:  
     ```bash
     pip install linode_api4
     ```

2. **Create Linode API Token**  
   - In Linode, go to **My Profile → API Tokens**  
   - Click **Create a Personal Access Token**  
     - **Label:** python  
     - **Permissions:** Read/Write for everything  
     - Click **Create Token**  
   - Copy the Access Token (displayed only once)

3. **Store Token as Environment Variable**  
   - Example (Linux/macOS):  
     ```bash
     export LINODE_TOKEN='your-access-token'
     ```

4. Go to your Linode dashboard and copy the **Linode ID**.

5. **Access Nginx Server via API**  
```python
   from linode_api4 import LinodeClient, Instance

   client = LinodeClient("your-access-token")
   nginx_server = client.load(Instance, Linode-ID)  # Replace Linode-ID with your server's ID
```
 
