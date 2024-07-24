from helpers.index_helpers import authenticate_user
import logging

class functons_background:
    def log_in(username,password):
        response = authenticate_user(username,password)
        return response