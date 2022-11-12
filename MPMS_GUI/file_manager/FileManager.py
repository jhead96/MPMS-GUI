from Datafile import Datafile

class FileManager:

    def __init__(self) -> None:
        self.file_list = []
        self.active_file_id = None 


    def add_file(self) -> None:
        pass

    def remove_file(self) -> None:
        pass

    def set_active_file_id(self, id: int) -> None:
        self.active_file_id = id

    def get_active_file_id(self) -> list[Datafile]:
        return [i for i in self.file_list if i.id == self.active_file_id]

    def clear_files(self) -> None:
        self.file_list = []
        self.active_file_id = None


