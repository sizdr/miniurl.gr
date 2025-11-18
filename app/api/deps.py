from typing import Generator
from sqlmodel import Session
from fastapi import Depends
from typing import Annotated
from app.databases.general import DBActionsHTTP

from app.databases.manager import DatabaseManager

def get_db() -> Generator[Session, None, None]:
   yield from DatabaseManager.get_session()

SessionDependency = Annotated[Session, Depends(get_db)]

def get_dbactions_http(session: SessionDependency) -> DBActionsHTTP:
   return DBActionsHTTP(session)

DBActionsHTTPDependency = Annotated[DBActionsHTTP, Depends(get_dbactions_http)]

