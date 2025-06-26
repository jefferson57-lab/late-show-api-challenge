# Late Show API

A RESTful API for managing episodes, guests, and appearances for a late show, built with Flask, Flask-RESTful, SQLAlchemy, and JWT authentication.

## Features

- User registration and login with JWT authentication
- CRUD operations for episodes, guests, and appearances
- Relational data modeling with SQLAlchemy
- Database seeding with Faker
- API endpoints for managing and retrieving show data

## Project Structure

```
.
├── server/
│   ├── app.py                # Flask app and API resource registration
│   ├── config.py             # Configuration (use environment variables)
│   ├── extensions.py         # Database and migration extensions
│   ├── seed.py               # Script to seed the database with fake data
│   ├── controllers/          # API endpoint controllers
│   └── models/               # SQLAlchemy models
├── challenge-4-lateshow.postman_collection.json  # Postman collection for API testing
├── Pipfile                   # Python dependencies
├── .gitignore
└── README.md
```

## Setup

1. **Clone the repository**

   ```sh
   git clone <repo-url>
   cd late-show-api-challenge
   ```

2. **Install dependencies**

   ```sh
   pipenv install
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory with your configuration (e.g., database URI, JWT secret). Example:

   ```
   FLASK_APP=server/app.py
   FLASK_ENV=development
   DATABASE_URI=sqlite:///late_show.db
   JWT_SECRET_KEY=your_jwt_secret_key
   ```

4. **Run database migrations**

   ```sh
   pipenv run flask db upgrade
   ```

5. **Seed the database**

   ```sh
   pipenv run python server/seed.py
   ```

6. **Start the server**

   ```sh
   pipenv run python server/app.py
   ```

   The API will be available at `http://localhost:5555/`.

## API Endpoints

- `POST /register` — Register a new user
- `POST /login` — Login and receive a JWT token
- `GET /episodes` — List all episodes
- `GET /episodes/<id>` — Get episode details (with appearances)
- `GET /guests` — List all guests
- `POST /appearances` — Create a new appearance (JWT required)

## Example Postman Collection

A ready-to-use Postman collection is provided:  
[challenge-4-lateshow.postman_collection.json](challenge-4-lateshow.postman_collection.json)

**How to use:**
1. Import the collection into Postman.
2. Register and login to get your JWT token.
3. Set the `access_token` variable in Postman for authenticated requests.
4. Test all endpoints using the provided requests.

## Models Overview

- **User**: Handles authentication and stores user credentials.
- **Guest**: Represents a guest on the show.
- **Episode**: Represents an episode of the show.
- **Appearance**: Links a guest to an episode with a rating.

## Seeding the Database

The [`server/seed.py`](server/seed.py) script uses Faker to populate the database with sample users, guests, episodes, and appearances for testing.

## Development Notes

- All API endpoints return JSON responses.
- JWT authentication is required for creating appearances.
- Ratings for appearances must be between 1 and 5.

## Testing

Use [Postman](https://www.postman.com/) or similar tools to test the API endpoints. Import the provided Postman collection for ready-to-use requests.

## License

MIT License
