from database.title_repository import TitleRepository
from database.models import Titles
from sqlalchemy.orm import Session


class TitleRepositoryImpl(TitleRepository):

    def __init__(self, session: Session):
        self.session = session

    def get_all_titles(self):
        return self.session.query(Titles).all()

    def get_full_info(self, full_name):
        return self.session.query(Titles).where(Titles.full_name == full_name)[0]