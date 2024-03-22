from Models.MongoSchema import Users
from bcrypt import hashpw, gensalt


new_student = [
    {
        "roll_no": "21EC887",
        "user_name": "Rizwan admin",
        "email": "rizwanadmin.2021eceb@sece.ac.in",
        "phone": 9994011787,
        "batch": 2025,
        "department": "ECE",
        "password": hashpw("sece@123".encode("utf-8"), gensalt()),
        "role": "admin",
    },
    {
        "roll_no": "21EC097",
        "user_name": "naveen",
        "email": "rnaveen.2021eceb@sece.ac.in",
        "phone": 1234567765,
        "batch": 2025,
        "department": "ECE",
        "password": hashpw("sece@123".encode("utf-8"), gensalt()),
        "role": "admin",
    },
    {
        "roll_no": "21EC321",
        "user_name": "test123",
        "email": "test123@sece.ac.in",
        "phone": 1234567865,
        "batch": 2025,
        "department": "ECE",
        "password": hashpw("test123".encode("utf-8"), gensalt()),
        "role": "student",
    },
    {
        "roll_no": "EC321",
        "user_name": "test456",
        "email": "test456@sece.ac.in",
        "phone": 1234567885,
        "batch": 2025,
        "department": "ECE",
        "password": hashpw("test456".encode("utf-8"), gensalt()),
        "role": "teacher",
    },
]
for n in new_student:
    user = Users(**n)
    user.save()
