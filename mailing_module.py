from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

import models
import sending_service
import treatment


def create_mailing(mailing: models.Mailing, clients: list):
    if mailing.start <= datetime.now() < mailing.end:
        start_mailing(mailing, clients)
        return
    elif datetime.now() < mailing.start:
        planning_mailing(mailing.start, mailing, clients)


def start_mailing(mailing: models.Mailing, clients: list):
    for client in clients:
        if datetime.now() >= mailing.end:
            return False

        message = create_message(mailing, client.id)
        response = sending_service.send_message(message.id, client.phone_number, mailing.text)

        if response == 200:
            treatment.message_change_status(message, 'Успешно')
        else:
            treatment.message_change_status(message, f"Ошибка {response}")


def create_message(mailing: models.Mailing, client_id: int):
    now = datetime.now()
    message = models.Message(sending_date=now, status='Не отправлено', mailing_id=mailing.id, client_id=client_id)
    message.id = treatment.create_message(message)
    return message


def planning_mailing(start: datetime, mailing: models.Mailing, clients: list):
    sched = BackgroundScheduler()
    sched.add_job(start_mailing, 'date', run_date=start, args=[mailing, clients])
    sched.start()





