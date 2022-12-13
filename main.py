from fastapi import FastAPI, HTTPException
import treatment

import models
import mailing_module

app = FastAPI()


@app.post("/client/")
def create_client(client: models.Client):
    treatment.create_client(client)
    return "Успешно."


@app.patch("/client/{client_id}")
def update_client(client_id: int, client: models.ClientUpdate):
    answer = treatment.update_client(client_id, client)
    if not answer:
        raise HTTPException(status_code=404, detail='Клиент не найден.')
    return answer


@app.delete("/client/{client_id}")
def delete_client(client_id: int):
    answer = treatment.delete_client(client_id)
    if not answer:
        raise HTTPException(status_code=404, detail='Клиент не найден.')
    return 'Клиент удалён.'


@app.post("/mailing/")
def create_mailing(mailing: models.Mailing):
    clients = treatment.create_mailing(mailing)
    mailing_module.create_mailing(mailing, clients)
    return 'Создано!'


@app.get("/mailing/{mailing_id}")
def get_mailings(mailing_id: int):
    answer = treatment.get_mailings(mailing_id)
    if not answer:
        raise HTTPException(status_code=404, detail='Рассылка не найдена.')
    return answer


@app.get("/messages/{mailing_id}")
def get_messages(mailing_id: int):
    answer = treatment.get_messages(mailing_id)
    if not answer:
        raise HTTPException(status_code=404, detail='Рассылка не найдена.')
    return answer


@app.patch("/mailing/{mailing_id}")
def update_mailing(mailing_id: int, mailing: models.MailingUpdate):
    answer = treatment.update_mailing(mailing_id, mailing)
    if not answer:
        raise HTTPException(status_code=404, detail='Рассылка не найдена.')
    return answer


@app.delete("/mailing/{mailing_id}")
def delete_mailing(mailing_id: int):
    answer = treatment.delete_mailing(mailing_id)
    if not answer:
        raise HTTPException(status_code=404, detail='Рассылка не найдена.')
    return 'Рассылка удалена.'


