from abc import ABC, abstractmethod


class TitleRepository(ABC):
    @abstractmethod
    def get_all_titles(self):
        pass

    @abstractmethod
    def get_sub_titles(self):
        pass

    @abstractmethod
    def get_dub_titles(self):
        pass

    @abstractmethod
    def get_title_info(self, title_id):
        pass

    @abstractmethod
    def get_episode(self, title_id, episode_number, episode_type):
        pass

    @abstractmethod
    def get_all_episodes(self):
        pass

    @abstractmethod
    def add_video_id(self, ep_id, video_id):
        pass