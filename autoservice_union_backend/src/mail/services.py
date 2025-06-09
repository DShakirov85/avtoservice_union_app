from typing import TypedDict

from fastapi_mail import ConnectionConfig, MessageSchema, FastMail
from settings import settings


class Attachment(TypedDict):
    file: str
    type: str


class EmailManager:
    def __init__(self):
        self.email_address = settings.EMAIL_ADDRESS
        self.email_password = settings.EMAIL_PASSWORD
        self.email_port = settings.MAIL_PORT
        self.email_server = settings.MAIL_SERVER
        self.email_tls = settings.MAIL_TLS
        self.email_ssl = settings.MAIL_SSL
        self.use_credentials = settings.USE_CREDENTIALS

    async def send_participation_email(
            self,
            email: str,
            participation_form: str,
            survey_form: str
    ) -> None:
        conf = ConnectionConfig(
            MAIL_USERNAME=self.email_address,
            MAIL_PASSWORD=self.email_password,
            MAIL_FROM=self.email_address,
            MAIL_PORT=self.email_port,
            MAIL_SERVER=self.email_server,
            MAIL_STARTTLS=self.email_tls,
            MAIL_SSL_TLS=self.email_ssl,
            USE_CREDENTIALS=self.use_credentials
        )
        message = MessageSchema(
            subject="Подтверждение регистрации в Союзе Автосервисов",
            recipients=[email],
            body="Присылаем документы.",
            subtype="plain",
            attachments=self.get_attachments(participation_form, survey_form)
        )
        fm = FastMail(conf)
        await fm.send_message(message)

    def get_attachments(
            self,
            participation_form: str,
            survey_form: str
    ) -> list[Attachment]:
        return [self.get_attachment(f) for f in (participation_form, survey_form)]

    def get_attachment(
            self,
            file: str
    ) -> Attachment:
        return {
            "file": file,
            "type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            }
