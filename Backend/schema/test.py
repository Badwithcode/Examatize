from mongoengine import connect

# Replace 'your-database' and 'your-host' with your actual database name and host
try:
    connect(host='mongodb://localhost:27017/Examatize')
    print("connected to DB")
except:
    print("error")
# connect(db='Examatize', host='mongodb+srv://rnaveen28102003:examatize@cluster0.lj6pugm.mongodb.net/?retryWrites=true&w=majority')


from mongoengine import Document, StringField, IntField

class User(Document):
    username = StringField(required=True, max_length=50)
    age = IntField()

# Create:

user = User(username='john_doe', age=25)
user.save()
# Read:

# # Find all users
# all_users = User.objects()

# # Find users with a specific condition
# specific_users = User.objects(age__gte=21)
# # Update:

# # Update a specific user
# user_to_update = User.objects(username='john_doe').first()
# user_to_update.age = 26
# user_to_update.save()

# # Delete:
# # Delete a specific user
# user_to_delete = User.objects(username='john_doe').first()
# user_to_delete.delete()

# # Querying:

# # Find users older than 30
# users_above_30 = User.objects(age__gt=30)
# # Indexes:

# class User(Document):
#     username = StringField(required=True, max_length=50, unique=True)
#     age = IntField()

#     meta = {
#         'indexes': [
#             {'fields': ['age'], 'sparse': True},
#         ]
#     }