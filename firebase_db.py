import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountKey.json')

# Initialize the app with a custom auth variable, limiting the server's access
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://donggo-hs-kr-default-rtdb.firebaseio.com',
    'databaseAuthVariableOverride': {
        'uid': '26cda879-51f0-48f8-b286-5aaad0933d6c'
    }
})

# The app only has access as defined in the Security Rules
ref = db.reference('/dusenbird')
print(ref.get())