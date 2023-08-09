# Localife
Final project Localife (WIP)


# Models



User (django model)

class User(AbstractUser)
These attributes are already included
'''
username: A string field that represents the unique username of the user.
password: A field that stores the user's password. It is stored as a hash for security reasons.
first_name: A string field to store the user's first name.
last_name: A string field to store the user's last name.
email: A string field to store the user's email address.
is_staff: A boolean field that determines if the user is a staff member with administrative access.
is_active: A boolean field that indicates if the user account is active.
date_joined: A DateTimeField that represents the date and time when the user account was created.
'''
location=models.CharField(max_length=255, blank=False)
social_instagram=models.URLField(
    max_length=255,
    blank=True,
    null=True,
)


Traveler(User)
'''
This inherit from User but is_staff is always False
'''
self.is_staff=False;
user_type=




Host(User)



Tag



Region




Experience (This is the activity that the host posts)


Review (V2)




# App division

home_app:

user_app:

search_app: Kai

post_app:

match_app:

finished_app:

test push


