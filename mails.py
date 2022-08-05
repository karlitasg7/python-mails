import smtplib
from email.message import EmailMessage
from pathlib import Path  # this is like os.path
from string import Template

if __name__ == '__main__':
    html = Template(Path('index.html').read_text())

    email = EmailMessage()
    email['from'] = 'From Me'
    email['to'] = 'xxx@gmail.com'  # here we put the email
    email['subject'] = 'My first email from python'

    email.set_content(html.substitute({'name': 'Hello'}), 'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()  # encryption
        smtp.login('email', 'pass')  # here it's necessary to put the email and password to use to send
        smtp.send_message(email)

        print('email send!!')
