# URL Shortener

A Simple Django web application that shortens long urls.  
It takes any URL as an input from the user and generates a random short URL. If the user prefers, it is also possible to use a custom shortcode.

Deployed on Heroku  
https://django-urlshortener.herokuapp.com/

# Setup
Clone the project
```
$ git clone https://github.com/arbaishev/urlshortener.git
$ cd urlshortener
```

Create & activate virtual environment
```
$ python3 -m venv urlshortener
$ source urlshortener/Scripts/activate (for Linux)
  * urlshortener\Scripts\activate (for Windows)
```

Install the project dependencies  
`$ pip install -r requirements.txt`


# Running Locally

1. Go to `src/manage.py` and edit line 8:  
    `urlshortener.settings.production` → `urlshortener.settings.local`
2. Duplicate `src\urlshortener\settings\local_settings_example.py` and save as `local.py`
3. Enter your secret key & database settings in `local.py`  
(you can obtain a secret key from [MiniWebTool](https://miniwebtool.com/django-secret-key-generator/ "MiniWebTool"))
4. `$ python src/manage.py migrate`
5. `$ python src/manage.py createsuperuser`
6. `$ python src/manage.py collectstatic`
7. `$ python src/manage.py runserver`
___

# API 
- Get all data  
`curl -X GET https://django-urlshortener.herokuapp.com/api/`

- Create short URL without custom shortcode  
`curl -X POST -H "Content-Type:application/json" -d '{"url":"example.com"}' http://127.0.0.1:8000/api/short/`

- Create short URL with custom shortcode (maximum length: 6)  
`curl -X POST -H "Content-Type:application/json" -d '{"url":"example.com", "custom":"True", "custom_shortcode":"<custom shortcode>"}' https://django-urlshortener.herokuapp.com/api/short/`

- Get info on specific URL  
`curl -X GET https://django-urlshortener.herokuapp.com/api/<custom shortcode>`