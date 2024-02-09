import pandas as pd
from pydantic import BaseModel, Field


class NewStudentBase(BaseModel):
    email: str = Field(pattern='^[a-zA-Z0-9._%+-]+@sece\.ac\.in$')
    user_name: str
    roll_no: str
    phone: int
    batch: int
    dept: str


from bcrypt import hashpw, gensalt
def get_student_details_in_excel(file):
    row_c = 1
    try:
        dataframe = pd.read_excel(file)
        password = 'sece@123'
        hashpassword = hashpw(password.encode('utf-8'), gensalt())
        students_list = []
        for index, row in dataframe.iterrows():
            new_student = {
                'roll_no' : row['roll_no'],
                'user_name' : row['user_name'],
                'email' : row['email'],
                'phone' : row['phone'],
                'batch' : row['batch'],
                'dept' : row['dept']
            }
            if NewStudentBase.model_validate(new_student).model_dump():
                new_student.update({'password': hashpassword, 'role':'student'})
                students_list.append(new_student)
                row_c += 1
            else:
                raise ValueError(f"Error in : {row_c} row")
        return {'status':True, 'result':students_list}
    except Exception as e:
        raise ValueError(f"Error in row:{row_c}")