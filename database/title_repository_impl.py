from database.title_repository import TitleRepository
from database.models import Titles, Series
from sqlalchemy.orm import Session


class TitleRepositoryImpl(TitleRepository):

    def __init__(self, session: Session):
        self.session = session

    def get_all_titles(self):
        return self.session.query(Titles).all()

    def get_title_info(self, title_id):
        return self.session.query(Titles).where(Titles.id == title_id)[0]

    def get_episode(self, title_id, episode_number):
        return self.session.query(Series).where(Series.title_id == title_id).order_by(Series.source_message_id)[episode_number-1]