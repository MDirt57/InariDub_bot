from abc import ABC, abstractmethod


class TitleRepository(ABC):
    @abstractmethod
    def get_all_titles(self):
        pass

    # @abstractmethod
    # def get_video(self):
    #     pass

    @abstractmethod
    def get_full_info(self, full_name):
        pass
