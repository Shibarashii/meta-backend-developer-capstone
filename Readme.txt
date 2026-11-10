Little Lemon - Back-End Capstone (Django + DRF + MySQL)

SETUP
1. python -m venv .venv  then activate it
2. pip install -r requirements.txt
3. Create a MySQL database "littlelemon" and a user that can access it
   (the user also needs rights on "test_littlelemon" to run the tests).
4. Copy .env.example to .env and fill in your MySQL user and password.
5. python manage.py migrate
6. python manage.py runserver
7. python manage.py test      (runs the unit tests)

API PATHS TO TEST (e.g. with Insomnia)

Static HTML home page
  GET    /restaurant/

User registration and authentication (djoser)
  POST   /auth/users/                  {"username": "...", "password": "...", "email": "..."}
  POST   /auth/token/login/            {"username": "...", "password": "..."}  -> auth_token
  POST   /auth/token/logout/           (requires token)
  GET    /auth/users/me/               (requires token)
  POST   /restaurant/api-token-auth/   {"username": "...", "password": "..."}  -> token

Send the token on protected endpoints with the header:
  Authorization: Token <your token>

Menu API (reading is public, changes require a token)
  GET    /restaurant/menu/
  POST   /restaurant/menu/             {"title": "Pasta", "price": "9.50", "inventory": 5}
  GET    /restaurant/menu/<id>
  PUT    /restaurant/menu/<id>
  PATCH  /restaurant/menu/<id>
  DELETE /restaurant/menu/<id>

Table booking API (all methods require a token)
  GET    /restaurant/booking/tables/
  POST   /restaurant/booking/tables/   {"name": "Ana", "no_of_guests": 4, "booking_date": "2026-11-20T19:00:00Z"}
  GET    /restaurant/booking/tables/<id>/
  PUT    /restaurant/booking/tables/<id>/
  PATCH  /restaurant/booking/tables/<id>/
  DELETE /restaurant/booking/tables/<id>/
