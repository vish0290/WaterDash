import pyrebase


def update_field(field,value):  
    firebase=pyrebase.initialize_app(config)
    data = {field:value}
    db = firebase.database()
    return  db.update(data) 
