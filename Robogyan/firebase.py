import pyrebase
config = {
  "apiKey": "AIzaSyAKPSD6K6MN-5GdFf-C-6toG7CAtDmawm4",
  "authDomain": "samplemainsite.firebaseapp.com",
  "databaseURL": "https://files.firebaseio.com",
  "storageBucket": "samplemainsite.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

storage = firebase.storage()
def don(url):
    file = url.lstrip("files/")
    file = file[:-14]
    storage.child(url).download(file,"Robogyan/Data/"+file)
    
don("files/Robowar.docx-1677255096367")