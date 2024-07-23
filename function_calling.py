from helpers.index import authenticate_user

class functons_background:
    def log_in(username,password):
        authenticate_user(username,password)
        return {"status": "success", "message": "Sign-in successful", "user" : "admin",}