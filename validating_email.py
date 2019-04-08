import re

def fun(email):
    # return True if s is a valid email, else return False
    pattern = re.compile(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{1,3}$')
    return re.match(pattern, email)
