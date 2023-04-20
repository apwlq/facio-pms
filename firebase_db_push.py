import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountKey.json')

# Initialize the app with a custom auth variable, limiting the server's access
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://donggo-hs-kr-default-rtdb.firebaseio.com',
    'databaseAuthVariableOverride': {
        'uid': 'test'
    }
})

# The app only has access as defined in the Security Rules
ref = db.reference('/test')
print(ref.get())

with open("test.json", "r", encoding="utf8") as f:
    file_contents = json.load(f)
# ref.set(file_contents)

ref.update(file_contents)