import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountKey.json')

# Initialize the app with a custom auth variable, limiting the server's access
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://donggo-hs-kr-default-rtdb.firebaseio.com',
    'databaseAuthVariableOverride': {
        'uid': 'bad05c2d-cb0c-4b0c-b9a2-706a57619832'
    }
})

# The app only has access as defined in the Security Rules
# ref = db.reference('/dusenbird')
# print(ref.get())

def get_device():
    ref = db.reference('/dusenbird/device')
    return ref.get()