import requests
import smtplib
import os
import paramiko
import linode_api4
import time
import schedule

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS_ENV')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD_ENV')


def restart_server_and_container():
    # restart server
    print('Rebooting server...')
    linode_client = linode_api4.LinodeClient('INSERT_LINODE_TOKEN')
    server = linode_client.load(linode_api4.Instance, 'INSERT_LINODE_ID')
    server.reboot()

    # restart app
    while True:
        server = linode_client.load(linode_api4.Instance, 'INSERT_LINODE_ID')
        if server.status == 'running':
            time.sleep(5)
            restart_container()
            break


def send_notification(email_msg):
    with smtplib.SMTP('<INSERT_EMAIL_PROVIDER>', 'PORT') as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        msg = f"Subject: SITE DOWN\n{email_msg}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)


def restart_container():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('INSERT_HOST_IP', username='root', key_filename='INSERT_KEY_PATH')
    stdin, stdout, stderr = ssh.exec_command('docker start <INSERT_CONTAINER_ID>')
    print(stdout.readlines())
    ssh.close()
    print('App restarted')


def monitor_app():
    try:
        response = requests.get('URL_ENDPOINT')
        if response.status_code == 200:
            print('App running successfully')
        else:
            print('App down.Fix it')
            send_notification(f'App returned {response.status_code}.')
            restart_container()
    except Exception as ex:
        print(f'Connection error happened: {ex}')
        send_notification('App is not accessible at all.')
        restart_server_and_container()


schedule.every(5).minutes.do(monitor_app)

while True:
    schedule.run_pending()
