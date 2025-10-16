import re

def check_email_regex(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        return True
    else:
        return False
    
def check_name_regex(name):
    regex = r"^[A-Za-z\s-]+$"
    if re.match(regex, name):
        return True
    else:
        return False
    