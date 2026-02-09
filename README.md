# Todo Full-Stack Web Application

This is a full-stack web application for managing todo tasks with user authentication and authorization.

## Tech Stack

- **Frontend**: Next.js 16+ with App Router
- **Backend**: Python FastAPI
- **ORM**: SQLModel
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: Better Auth with JWT

## Features

- User registration and authentication
- Secure task management (create, read, update, delete)
- JWT-based session management
- Data isolation between users
- Responsive UI design

## Setup Instructions

### Prerequisites

- Node.js 18+
- Python 3.11+
- PostgreSQL (or access to Neon Serverless PostgreSQL)
- Git
- npm or yarn package manager

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set environment variables:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` file with your configuration

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. Set environment variables:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` file with your configuration

### Database Setup

1. From the backend directory with activated virtual environment:
   ```bash
   cd backend
   python -m alembic upgrade head
   ```

2. Seed initial data (optional):
   ```bash
   python -m scripts.seed_data
   ```

### Running the Application

#### Running Backend

From the backend directory with activated virtual environment:
```bash
cd backend
python -m uvicorn src.main:app --reload --port 8000
```

#### Running Frontend

From the frontend directory:
```bash
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
- `POST /v1/auth/register` - Register a new user
- `POST /v1/auth/login` - Login and get JWT token
- `POST /v1/auth/logout` - Logout user

### Tasks
- `GET /v1/tasks` - Get all tasks for authenticated user
- `POST /v1/tasks` - Create a new task
- `GET /v1/tasks/{taskId}` - Get a specific task
- `PUT /v1/tasks/{taskId}` - Update a task
- `DELETE /v1/tasks/{taskId}` - Delete a task

## Testing

### Backend tests
```bash
cd backend
python -m pytest
```

### Frontend tests
```bash
cd frontend
npm test
# or
yarn test
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