# Little Lemon — Back-End Capstone

Django + Django REST Framework + MySQL back end for the Little Lemon restaurant: a static home page, a menu API, a table booking API, and user registration with token authentication.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a MySQL database `littlelemon` and a user that can access it. The user also needs rights on `test_littlelemon` to run the tests.
4. Copy `.env.example` to `.env` and fill in your MySQL user and password.
5. Apply migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
6. Run the unit tests:
   ```bash
   python manage.py test
   ```

## API paths to test (e.g. with Insomnia)

Protected endpoints need the token in a header, in either form:

```
Authorization: Token <your token>
Authorization: Bearer <your token>    (Insomnia: Auth tab → Bearer Token)
```

### Static HTML home page

| Method | Path |
|---|---|
| GET | `/restaurant/` |

### User registration and authentication (djoser)

| Method | Path | Body / notes |
|---|---|---|
| POST | `/auth/users/` | `{"username": "...", "password": "...", "email": "..."}` |
| POST | `/auth/token/login/` | `{"username": "...", "password": "..."}` → `auth_token` |
| POST | `/auth/token/logout/` | requires token |
| GET | `/auth/users/me/` | requires token |
| POST | `/restaurant/api-token-auth/` | `{"username": "...", "password": "..."}` → `token` |

### Menu API (reading is public, changes require a token)

| Method | Path | Body |
|---|---|---|
| GET | `/restaurant/menu/` | |
| POST | `/restaurant/menu/` | `{"title": "Pasta", "price": "9.50", "inventory": 5}` |
| GET | `/restaurant/menu/<id>` | |
| PUT / PATCH | `/restaurant/menu/<id>` | same fields as POST |
| DELETE | `/restaurant/menu/<id>` | |

### Table booking API (all methods require a token)

| Method | Path | Body |
|---|---|---|
| GET | `/restaurant/booking/tables/` | |
| POST | `/restaurant/booking/tables/` | `{"name": "Ana", "no_of_guests": 4, "booking_date": "2026-11-20T19:00:00Z"}` |
| GET | `/restaurant/booking/tables/<id>/` | |
| PUT / PATCH | `/restaurant/booking/tables/<id>/` | same fields as POST |
| DELETE | `/restaurant/booking/tables/<id>/` | |
