from model.note import Note
from model.file_manager import FileManager

file = "./storage/notes.json"

class NoteManager:
    def __init__(self):
        self.manager = FileManager(file)
        self.notes = self.manager.load_notes()

    def create_note(self, title, content, id):
        note = Note(title, content, id)

        note_data = {
            "title": title,
            "content": content,
            "id": str(id)
        }
        self.manager.save_note(note_data)

        self.notes.append(note)

    def delete_note(self, id):
        self.notes = [note for note in self.notes if note.get_id() != id]
        self.manager.delete_note(id)

    def edit_note(self, id, new_title, new_content):
        for note in self.notes:
            if note.get_id() == id:
                note.set_title(new_title)
                note.set_contenido(new_content)

        self.manager.edit_note(id, new_title, new_content)
                
    def get_notes(self):
        return self.notes
    
    def print_notes(self):
        return [str(note) for note in self.notes]