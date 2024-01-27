class Note:
    def __init__(self, title, content, id):
        self.title = title
        self.content = content
        self.id = id

    def __str__(self):
        return f"{self.title};{self.content}"

    def get_title(self):
        return self.title

    def set_title(self, new_title):
        self.title = new_title

    def get_contenido(self):
        return self.content
    
    def set_contenido(self, new_content):
        self.content = new_content

    def get_id(self):
        return self.id