#! /usr/bin/env python3
import email
import json
from datetime import date
from email.message import EmailMessage
from pathlib import Path
from smtplib import SMTP

CONFIG = Path(__file__).with_name('config.json')
TASK_FOLDER = Path(__file__).parent / 'tasks'


class Mailer:
    def __init__(self, config: dict):
        self.name_from = config['name_from']
        self.mail_from = config['mail_from']
        self.smtp = SMTP(config['host'], port=587)
        self.smtp.starttls()
        self.smtp.login(config['user'], config['pass'])

    def close(self):
        self.smtp.quit()

    def send_email(self, to: str, subject: str, body: str):
        message = EmailMessage()
        message.set_content(body, charset='utf-8', cte='quoted-printable')
        message["From"] = f"{self.name_from} <{self.mail_from}>"
        message["To"] = to
        message["Subject"] = subject
        message["Date"] = email.utils.formatdate()

        self.smtp.send_message(message)


def load_template(template: Path) -> tuple[str, str]:
    template_lines = template.read_text().splitlines(keepends=False)
    assert template_lines[0] != ''
    assert template_lines[1] == ''
    assert template_lines[2] != ''
    return template_lines[0], '\n'.join(template_lines[2:])


def send_mail(mailer: Mailer, recipient_email: str, task: Path):
    subject, body = load_template(task)
    print(f'Sending "{subject}" to "{recipient_email}" ({task=})')
    mailer.send_email(to=recipient_email, subject=subject, body=body)


def main():
    today = date.today()
    task_prefix = today.strftime('%m-%d-')
    config = json.loads(CONFIG.read_text())
    mailer = Mailer(config)
    for recipient_dir in sorted(TASK_FOLDER.glob('*')):
        recipient_email = config['recipients'][recipient_dir.name]
        for task in sorted(recipient_dir.glob(f'{task_prefix}*')):
            send_mail(mailer, recipient_email, task)
    mailer.close()


if __name__ == '__main__':
    main()
