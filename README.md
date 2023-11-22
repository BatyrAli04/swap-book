# swap-book

1. Create .env file and include it:
PROJECT_NAME=Book Swapping
DESCRIPTION=book exchange systems
VERSION=0.0.1
API_V1_PREFIX=/api/v1

DATABASE_PORT=5432
POSTGRES_PASSWORD=123
POSTGRES_USER=postgres
POSTGRES_DB=swapping-book
POSTGRES_HOST=postgres
POSTGRES_HOSTNAME=postgres

AUTHJWT_SECRET_KEY=b2b1f22cfcfd764d54388b855bdabdf7edfe03c09f3a2c08ecd412f529da9c6d
REFRESH_TOKEN_EXPIRES_IN=10080
ACCESS_TOKEN_EXPIRES_IN=60000
JWT_ALGORITHM=RS256

DEBUG=False

2. Enter docker compose up --build
3. Open http://localhost:8002
