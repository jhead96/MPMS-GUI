from file_manager.Datafile import Datafile

class FileManager:

    def __init__(self) -> None:

        self.file_list = []
        self.active_file_id = None 


    def __str__(self) -> str:

        return f"{self.file_list}"


    def add_datafile(self, filename: str) -> None:
        id = self.generate_id()
        self.file_list.append(Datafile(id, filename))


    def generate_id(self) -> int:
        new_id = 0
        curr_ids = [f.id for f in self.file_list]

        while new_id in curr_ids:
            new_id += 1

        return new_id


    def remove_datafile(self, id: int) -> None:
        new_list = [f for f in self.file_list if f.id != id]
        self.file_list = new_list


    def set_active_datafile_id(self, id: int) -> None:
        self.active_file_id = id


    def get_active_datafile(self) -> list[Datafile]:
        return [f for f in self.file_list if f.id == self.active_file_id]

    
    def get_all_datafiles_as_dict(self) -> list[dict]:
        return [f.get_fields_as_dict() for f in self.file_list]


    def clear_files(self) -> None:
        self.file_list = []
        self.active_file_id = None