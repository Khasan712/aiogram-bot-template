from enum import Enum

class UserRole(Enum):
    director = 'director'
    accounts_manager = 'accounts_manager'
    chat_manager = 'chat_manager'
    content_manager = 'content_manager'
    comments_manager = 'comments_manager'
    user = 'user'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

