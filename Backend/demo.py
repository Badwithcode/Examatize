from Models.Mongodb import users_table
from bcrypt import hashpw, gensalt


new_student = [
    {
        'roll_no' : '21EC097',
        'user_name' : 'naveen',
        'email' : 'rnaveen.2021eceb@sece.ac.in',
        'phone' : 1234567765,
        'batch' : 2025,
        'dept' : 'ECE',
        'password': hashpw('sece@123'.encode('utf-8'), gensalt()),
        'role':'student'
    },{
        'roll_no' : '21EC321',
        'user_name' : 'test123',
        'email' : 'test123@sece.ac.in',
        'phone' : 1234567865,
        'batch' : 2025,
        'dept' : 'ECE',
        'password': hashpw('test123'.encode('utf-8'), gensalt()),
        'role':'student'
    },{
        'roll_no' : 'EC321',
        'user_name' : 'test456',
        'email' : 'test456@sece.ac.in',
        'phone' : 1234567885,
        'batch' : 2025,
        'dept' : 'ECE',
        'password': hashpw('test456'.encode('utf-8'), gensalt()),
        'role':'teacher'
    }
]
users_table.insert_many(new_student)