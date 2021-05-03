# Netflixclonedjangoreact

A Netflix clone I created for the sake of practicing React ,Redux and Django REST API. It features design patterns recommended by the documentation. Some of the tools used include:

   1. Django
   2. Django REST API
   3. Redux
   4. React
   5. Responsive Web Design
   6. Bootstrap
 ### [Live Demo](https://dashboard.heroku.com/pipelines/c8400218-7f92-42b3-b906-e232b1fe6dbd)
 
 ### This projects have two parts: 
 - Frontend ( React and Redux )
 - Backend ( Django and Django REST API)


### Getting Started
#### Getting Started with Backend branch
Install python package. Download python from https://www.python.org/downloads/
.Then clone this github and save in your device.
```sh
git clone https://github.com/yogendrabohara/netflixclonedjangoreact/
cd netflixclonedjangoreact
cd backend
```

It is important to download the requirements to run this app in your localhost , hence to download all the requirements packages used during building phases. Use this command in local command prompt.

```sh
pip install -r requirements.txt
```

#### Before deployment , migrate all the changes and makemigrations using following shell command prompt:
```sh
python manage.py makemigrations

python manage.py migrate
python manage.py runserver
```

### Deployment
- Application will be serving on http://localhost:8000
- This will gives us API endpoints

### GETTING STARTED WITH FRONT END

#### Features 
- Without sign in/ sign up users can visit Home page
- Users can signup , login and logout
- Used Token authenication and stored in redux store 
- User can click on a movie and a modal should pop up.


#### Navigate to the front end folder

```sh
cd netflixclonedjangoreact
cd frontend
```

#### Install Dependencies
```sh 
npm install
```
#### Run the project on your local machine

```sh 
npm start
```


#### Deployment
- Application will be serving on http://localhost:3000














