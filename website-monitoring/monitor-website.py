import requests
import smtplib
import os
import paramiko
import linode_api4
import time
import schedule

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
LINODE_TOKEN=os.environ.get('LINODE_TOKEN')

def send_notification(email_msg):
      print('Sending email...')
      with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            msg=f"Subject: SITE DOWN\n{email_msg}"
            smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)

def restart_container():
        print('Restarting the application')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('public-ip-address-of-your-server', username='root', key_filename='your-home-directory/.ssh/id_ed25519')
        stdin, stdout, stderr = ssh.exec_command('docker start CONTAINER_ID')
        print(stdout.readlines())
        ssh.close()

def restart_server_and_container():
        # restart Linode server
    print('Rebooting server...')
    client = linode_api4.LinodeClient(LINODE_TOKEN)
    nginx_server = client.load(linode_api4.Instance, Linode-ID)
    nginx_server=client.reboot()

    # restart application
    while True:
        nginx_server = client.load(linode_api4.Instance, Linode-ID)
        if nginx_server.status == 'running':
                time.sleep(5)
                restart_container()
                break

def monitor_application():
        try:
            response = requests.get('http://public-ip-address-of-your-server.ip.linodeusercontent.com:8080/')
            if response.status_code == 200:
                print('Application is running successfully!')
            else:
                print('Application down: fix it!')
                message = f"Application returned {response.status_code}"
                send_notification(message)
                restart_container()
        except Exception as ex:
            print(f'Connection error happened {ex}')
            msg = "Application not accessible at all"
            send_notification(msg)
            restart_server_and_container()

schedule.every(5).minutes.do(monitor_application)

while True:
     schedule.run_pending()