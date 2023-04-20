import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

uid = "sBW4yUlvnnhroGzdLeztFfDKQe63"

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountKey.json')

# Initialize the app with a custom auth variable, limiting the server's access
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://donggo-hs-kr-default-rtdb.firebaseio.com',
    'databaseAuthVariableOverride': {
        'uid': 'test'
    }
})

# user = auth.get_user(uid)
# print('Successfully fetched user data: {0}'.format(user.uid))

# # Start listing users from the beginning, 1000 at a time.
# page = auth.list_users()
# while page:
#     for user in page.users:
#         print('User: ' + user.uid)
#     # Get next batch of users.
#     page = page.get_next_page()


# user = auth.update_user(
#     uid,
#     email='makerzip@hanmail.net',
#     phone_number='+821044156279',
#     email_verified=True,
#     password='newPassword',
#     display_name='메이커집',
#     photo_url='https://avatars.githubusercontent.com/u/58218300?v=4',
#     disabled=False)
# print('Sucessfully updated user: {0}'.format(user.uid))

# Iterate through all users. This will still retrieve users in batches,
# buffering no more than 1000 users in memory at a time.
for user in auth.list_users().iterate_all():
    print(f'User: {user.uid}')
    print(f'Mail: {user.email}')
    print(f'phone_number: {user.phone_number}')
    print(f'email_verified: {user.email_verified}')
    print(f'display_name: {user.display_name}')
    print(f'photo_url: {user.photo_url}')