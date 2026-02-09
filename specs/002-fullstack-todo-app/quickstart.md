# Quickstart Guide: Todo Full-Stack Web Application

## Overview
This guide provides instructions for setting up and running the Todo Full-Stack Web Application locally.

## Prerequisites
- Node.js 18+ (for frontend development)
- Python 3.11+ (for backend development)
- PostgreSQL (or access to Neon Serverless PostgreSQL)
- Git
- npm or yarn package manager

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd todo-fullstack-app
```

### 2. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env file with your configuration
```

#### Backend Environment Variables
- `DATABASE_URL`: Connection string for PostgreSQL database
- `BETTER_AUTH_SECRET`: Secret key for JWT token signing
- `NEON_DATABASE_URL`: Connection string for Neon Serverless PostgreSQL (if using)

### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd ../frontend

# Install dependencies
npm install
# or
yarn install

# Set environment variables
cp .env.example .env
# Edit .env file with your configuration
```

#### Frontend Environment Variables
- `NEXT_PUBLIC_API_BASE_URL`: Base URL for the backend API
- `NEXT_PUBLIC_BETTER_AUTH_URL`: URL for the authentication service

### 4. Database Setup
```bash
# From the backend directory with activated virtual environment
cd backend

# Run database migrations
python -m alembic upgrade head

# Seed initial data (optional)
python -m scripts.seed_data
```

### 5. Running the Application

#### Running Backend
```bash
# From the backend directory with activated virtual environment
cd backend
python -m uvicorn main:app --reload --port 8000
```

#### Running Frontend
```bash
# From the frontend directory
cd frontend
npm run dev
# or
yarn dev
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Backend API Docs: http://localhost:8000/docs

## API Endpoints

### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and get JWT token
- `POST /auth/logout` - Logout user

### Tasks
- `GET /tasks` - Get all tasks for authenticated user
- `POST /tasks` - Create a new task
- `GET /tasks/{taskId}` - Get a specific task
- `PUT /tasks/{taskId}` - Update a task
- `DELETE /tasks/{taskId}` - Delete a task

## Testing
```bash
# Backend tests
cd backend
python -m pytest

# Frontend tests
cd frontend
npm test
# or
yarn test
```

## Troubleshooting

### Common Issues
1. **Database Connection Error**: Verify DATABASE_URL in your .env file
2. **JWT Authentication Error**: Ensure BETTER_AUTH_SECRET is set consistently across services
3. **CORS Error**: Check that frontend URL is added to CORS_ALLOWED_ORIGINS in backend config

### Resetting the Development Environment
```bash
# Reset database
cd backend
python -m scripts.reset_db

# Clear frontend cache
cd frontend
rm -rf node_modules package-lock.json
npm install
```

## Development Workflow

### Adding New Features
1. Update the OpenAPI specification in `contracts/openapi.yaml`
2. Implement backend functionality following FastAPI best practices
3. Implement frontend components and API service calls
4. Write tests for new functionality
5. Update documentation as needed

### Environment Configuration
For local development, ensure the following configuration:
- Backend running on port 8000
- Frontend running on port 3000
- JWT tokens properly configured for authentication
- Database connection established and migrated