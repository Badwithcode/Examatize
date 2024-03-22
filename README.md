Hey Folks,

## Clone the project


    git clone https://github.com/Badwithcode/Examatize.git


You will find a two folders "Frontend" and "Backend"

## Once after every pull
    # Frontend

    cd Frontend
    npm install
    npm run dev


    #Backend
    #For the first time

    cd Backend
    python3 -m venv venv
    venv/scripts/activate
    pip install -r requirements.txt
    python3 main.py
    
    #From next time
    venv/scripts/activate
    pip install -r requirements.txt
    python3 main.py


sudo service redis-server start
For more refer Jubair