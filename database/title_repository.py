from abc import ABC, abstractmethod


class TitleRepository(ABC):
    @abstractmethod
    def get_all_titles(self):
        pass

    @abstractmethod
    def get_title_info(self, title_id):
        pass

    @abstractmethod
    def get_episode(self, title_id, episode_number):
        pass