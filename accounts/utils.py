import threading
from accounts.models import User

class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()
        
def get_user_preferred_genres(user_id):
    
    try:
        user = User.objects.get(id=user_id)
        preferred_genres = user.preferred_genres.all()
        return [genre.name for genre in preferred_genres]
    except User.DoesNotExist:
        return []  #사용자가 없으면