import smtplib
from email.message import EmailMessage


def send_email(receiver, filepath):

    sender = "jeyathakseena8@gmail.com"
    password = "hiul xcqz rqqz bcad"

    msg = EmailMessage()

    msg["Subject"] = "Review Analysis Report"
    msg["From"] = sender
    msg["To"] = receiver

    msg.set_content(
    "Attached is your automated review analysis report."
    )

    with open(filepath, "rb") as f:
        file_data = f.read()

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="pdf",
        filename="report.pdf"
    )

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    server.login(sender, password)

    server.send_message(msg)

    server.quit()