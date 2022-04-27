def test_config():
    return True

def add_friend(name, bday, bdaydictionary):
    bdaydictionary[name] = bday

def update_friend(name, bday, bdaydictionary):
    bdaydictionary[name] = bday

def del_friend(name, bdaydictionary):
    del bdaydictionary[name]