from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest

class AuthenticationService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def login_user(self, request: HttpRequest, username: str, password: str):
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return True
        return False
    
    def logout_user(self, request: HttpRequest):
        logout(request)
    
    def register_user(self, username: str, password: str, email: str):
        return self.user_repository.create_user(username, password, email)
