import os

class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY")
    REGISTERED_USERS={
        "kevinb@codingtemple.com":{"name":"Kevin", "password":"123abc"},
        "dylans@codingtemple.com":{"name":"Dylan", "password":"Colt45"},
        "joel@codingtemple.com":{"name":"Joel", "password":"MorphinTime"},
        "codingnannah@gmail.com":{"name":"Diana", "password":"Diana123"}
    }