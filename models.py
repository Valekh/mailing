from datetime import datetime
from typing import Union

from pydantic import BaseModel, validator, ValidationError


class BaseModelConfig(BaseModel):
    class Config:
        orm_mode = True


class Mailing(BaseModelConfig):
    id: Union[int, None] = None
    start: datetime
    text: str
    filters: dict
    end: datetime

    @validator('filters')
    def check_keys(cls, filters):
        if ('tag' not in filters) or ("operator_cod" not in filters):
            raise ValueError
        return filters


class MailingUpdate(BaseModelConfig):
    start: Union[datetime, None] = None
    text: Union[str, None] = None
    filters: Union[dict, None] = None
    end: Union[datetime, None] = None


class Client(BaseModelConfig):
    id: Union[int, None] = None
    phone_number: int
    operator_cod: int
    tag: str
    timezone: str


class ClientUpdate(BaseModelConfig):
    phone_number: Union[int, None] = None
    operator_cod: Union[int, None] = None
    tag: Union[str, None] = None
    timezone: Union[str, None] = None


class Message(BaseModelConfig):
    id: Union[int, None] = None
    sending_date: datetime
    status: str
    mailing_id: int
    client_id: int
