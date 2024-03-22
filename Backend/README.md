## Endpoints 

'/login'    <b>completed</b>

    LoginResource
        login api to authenticat ethe users.
        input : email and password
        validation
            email should end with @sece.ac.in
            password: greater that 6 letters

        response:{
            "status": true,
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoidGVhY2hlciIsInN1YiI6InRlc3Q0NTZAc2VjZS5hYy5pbiIsImlhdCI6MTcwNzE5NzYyNywiZXhwIjoxNzA3Mjg0MDI3fQ.JyT0TV-6LKLy8cmI3R6vKm3TkdgdXi3u80e5tvWos6k"
            }

            or

            {
            "status": false,
            "message": "User Not Found"
            }


'/token' <b>completed</b>

    TokenResource
        header: ['Autherization'] send token
            format: 'bearer ${localstorage.getItem('token)}'
        response:{
            "role": "teacher",
            "sub": "test456@sece.ac.in",
            "iat": 1707197627,
            "exp": 1707284027,
            "status": true
        }
        

'/profile' <b> Completed Rizwan need to complete it </b>

    UserResource
        header: z['Autherization'] send token
            format: 'bearer ${localstorage.getItem('token)}'
        response:{
            Try to display the every content of the user except the password
        }

'/upcoming' <b>Rizwan need to complete it</b>

    UpcomingTestResource
         header: ['Autherization'] send token
            format: 'bearer ${localstorage.getItem('token)}'
        response:{
            Display the test Details fully which time is less thn current time -> do it using filter(aggregate)
        }

'/tests' <b>Rizwan need to complete it</b>

    TestResource
        header: ['Autherization'] send token
            format: 'bearer ${localstorage.getItem('token)}'
        response:{
            Display the test Details fully (every tests)
        }

'/completed' <b>Rizwan need to complete it</b>

    CompletedTestResource
        header: ['Autherization'] send token
            format: 'bearer ${localstorage.getItem('token)}'
        response:{
           Will discuss later
        }