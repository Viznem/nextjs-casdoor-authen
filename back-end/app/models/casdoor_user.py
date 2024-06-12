from typing import Union, List

from pydantic import BaseModel


class CasdoorUser(BaseModel):
    username: str
    password: str
    owner: str
    name: str
    displayName: Union[str, None] = None
    email: Union[str, None] = None
    phone: Union[str, None] = None
    address: List[str] = []
