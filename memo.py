import uuid

class Memo:
    def __init__(self, title, content):
        self.id = uuid.uuid4().hex
        self.title = title
        self.content = content

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content
        }