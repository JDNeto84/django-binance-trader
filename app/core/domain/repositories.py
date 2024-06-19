from core.models import CustomUser

class UserRepository:
    def get_user_by_username(self, username: str):
        try:
            return CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return None
    
    def create_user(self, username: str, password: str, email: str):
        return CustomUser.objects.create_user(username=username, password=password, email=email)

