import json
import uuid
from model.note import Note
class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def save_note(self, note):
        try:
            with open(self.file_name, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append(note)

        with open(self.file_name, "w") as f:
            json.dump(data, f)

    def load_notes(self):
        try:
            with open(self.file_name, "r") as json_file:
                notes_data = json.load(json_file)
        except FileNotFoundError:
            notes_data = []

        # Creamos la lista de notas
        notes = []
        for note_data in notes_data:
            note = Note(note_data["title"], note_data["content"], uuid.UUID(note_data["id"]).hex)
            notes.append(note)

        return notes
    
    def delete_note(self, id):
        try:
            with open(self.file_name, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data = [obj for obj in data if obj["id"].replace("-", "") != id]

        with open(self.file_name, "w") as f:
            json.dump(data, f)

    def edit_note(self, id, new_title, new_content):
        try:
            with open(self.file_name, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        for obj in data:
            if obj["id"].replace("-", "") == id:
                obj["title"] = new_title
                obj["content"] = new_content

        with open(self.file_name, "w") as f:
            json.dump(data, f)