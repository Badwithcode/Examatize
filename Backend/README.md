## Endpoints 

'/login'

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


'/token'

    TokenResource
        header: ['Authentication'] send token
            format: 'bearer ${localstorage.getItem('token)}'
        response:{
            "role": "teacher",
            "sub": "test456@sece.ac.in",
            "iat": 1707197627,
            "exp": 1707284027,
            "status": true
        }
        