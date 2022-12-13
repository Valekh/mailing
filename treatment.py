import models
import db


def create_client(pd_client: models.Client):
    db_client = db.Client(**pd_client.dict())
    db.Session.add(db_client)
    db.Session.commit()
    db.Session.refresh(db_client)
    return db_client


def update_client(client_id: int, client: models.ClientUpdate):
    db_client = db.Session.get(db.Client, client_id)
    if not db_client:
        return None
    client_data = client.dict(exclude_unset=True)
    for key, value in client_data.items():
        setattr(db_client, key, value)
    db.Session.add(db_client)
    db.Session.commit()
    db.Session.refresh(db_client)
    return db_client


def delete_client(client_id: int):
    db_client = db.Session.get(db.Client, client_id)
    if not db_client:
        return None
    db.Session.delete(db_client)
    db.Session.commit()
    return True


def create_mailing(pd_mailing: models.Mailing):
    db_mailing = db.Mailing(**pd_mailing.dict())
    db.Session.add(db_mailing)
    db.Session.commit()
    db.Session.refresh(db_mailing)
    clients = get_clients_from_filters(pd_mailing)
    pd_mailing.id = db_mailing.id
    return clients


def get_clients_from_filters(pd_mailing: models.Mailing):
    operator_cod = pd_mailing.filters['operator_cod']
    tag = pd_mailing.filters['tag']
    result = db.Session.query(db.Client).filter(db.Client.operator_cod == operator_cod,
                                                    db.Client.tag == tag).all()
    return result


def get_mailings(mailing_id: int):
    success = db.Session.query(db.Message).filter(db.Message.status == 'Успешно').count()
    error = db.Session.query(db.Message).filter(db.Message.status == 'Ошибка 400').count()
    mailing_info = db.Session.query(db.Mailing).filter(db.Mailing.id == mailing_id).first()
    result = {"Информация о рассылке": mailing_info,
              "Успешных сообщений": success,
              "Сообщений с ошибкой 400": error}
    return result


def get_messages(mailing_id: int):
    return db.Session.query(db.Message).filter(db.Message.mailing_id == mailing_id).all()


def update_mailing(mailing_id: int, mailing: models.MailingUpdate):
    db_mailing = db.Session.get(db.Mailing, mailing_id)
    if not db_mailing:
        return None
    mailing_data = mailing.dict(exclude_unset=True)
    for key, value in mailing_data.items():
        setattr(db_mailing, key, value)
    db.Session.add(db_mailing)
    db.Session.commit()
    db.Session.refresh(db_mailing)
    return db_mailing


def delete_mailing(mailing_id: int):
    db_mailing = db.Session.get(db.Mailing, mailing_id)
    if not db_mailing:
        return None
    db.Session.delete(db_mailing)
    db.Session.commit()
    return True


def create_message(pd_message: models.Message):
    db_message = db.Message(**pd_message.dict())
    db.Session.add(db_message)
    db.Session.commit()
    db.Session.refresh(db_message)
    return db_message.id


def message_change_status(pd_message: models.Message, status:str):
    bd_message = db.Session.query(db.Message).filter(db.Message.id == pd_message.id).first()
    bd_message.status = status
    db.Session.commit()
