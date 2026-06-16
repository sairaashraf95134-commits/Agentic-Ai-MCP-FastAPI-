import os
import yagmail
from dotenv import load_dotenv

load_dotenv()


def send_email(
        to: str,
        subject: str,
        body: str
):
    """
    Send email using Gmail + Yagmail
    """

    gmail_user = os.getenv("EMAIL_ADDRESS")
    gmail_pass = os.getenv("EMAIL_PASSWORD")

    try:

        yag = yagmail.SMTP(
            gmail_user,
            gmail_pass
        )

        yag.send(
            to=to,
            subject=subject,
            contents=body
        )

        return f"Email sent successfully to {to}"

    except Exception as e:
        return f"Email sending failed: {str(e)}"