import inject
from database import Session
from database.title_repository import TitleRepository
from database.title_repository_impl import TitleRepositoryImpl


def configure(binder):
    session = Session()
    binder.bind(TitleRepository, TitleRepositoryImpl(session))


inject.configure(configure)
