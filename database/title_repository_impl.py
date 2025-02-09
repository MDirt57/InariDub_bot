from database.title_repository import TitleRepository
from database.models import Titles, Series
from sqlalchemy.orm import Session
from sqlalchemy import update, func

class TitleRepositoryImpl(TitleRepository):

    def __init__(self, session: Session):
        self.session = session

    def get_all_titles(self):
        return self.session.query(Titles).all()

    def get_sub_titles(self):
        title_episodes = self.session.query(func.count(Series.title_id), Series.title_id).where(Series.type == False, Series.title_id != None).group_by(Series.title_id).all()
        titles = []
        for count, title_id in title_episodes:
            titles.append((self.get_title_info(title_id), count))
        return titles

    def get_dub_titles(self):
        title_episodes = self.session.query(func.count(Series.title_id), Series.title_id).where(Series.type == True, Series.title_id != None).group_by(Series.title_id).all()
        titles = []
        for count, title_id in title_episodes:
            titles.append((self.get_title_info(title_id), count))
        return titles

    def get_title_info(self, title_id):
        return self.session.query(Titles).where(Titles.id == title_id)[0]

    def get_episode(self, title_id, episode_number, episode_type):
        print(episode_type)
        all_episodes = self.session.query(Series).where(Series.title_id == title_id, Series.type == episode_type).order_by(Series.episode_number)
        print(all_episodes.count())
        return all_episodes[episode_number], all_episodes.count()-1

    def get_all_episodes(self):
        return self.session.query(Series)

    def add_video_id(self, ep_id, video_id):
        new_record = update(Series).where(Series.id == ep_id).values({"bot_video_id": video_id})
        self.session.execute(new_record)
        self.session.commit()