# Data Model: Todo Full-Stack Web Application

## Overview
This document defines the data models for the Todo Full-Stack Web Application, including entities, relationships, and validation rules based on the feature specification.

## Core Entities

### User
Represents a registered user in the system

**Fields**:
- `id` (UUID/String): Unique identifier for the user (primary key)
- `email` (String): User's email address (unique, required)
- `password_hash` (String): Hashed password (required, stored securely)
- `created_at` (DateTime): Timestamp when the user account was created
- `updated_at` (DateTime): Timestamp when the user account was last updated
- `is_active` (Boolean): Whether the account is active (default: true)

**Validation Rules**:
- Email must be a valid email format
- Email must be unique across all users
- Password must meet minimum security requirements (length, complexity)
- Created and updated timestamps are automatically managed

**Relationships**:
- One User has many Tasks (one-to-many relationship)

### Task
Represents a todo item owned by a specific user

**Fields**:
- `id` (UUID/String): Unique identifier for the task (primary key)
- `title` (String): Title of the task (required, max 255 chars)
- `description` (Text): Detailed description of the task (optional)
- `completed` (Boolean): Whether the task is completed (default: false)
- `created_at` (DateTime): Timestamp when the task was created
- `updated_at` (DateTime): Timestamp when the task was last updated
- `user_id` (UUID/String): Foreign key linking to the owning user (required)

**Validation Rules**:
- Title must not be empty
- Title length must be between 1 and 255 characters
- User_id must reference an existing, active user
- Created and updated timestamps are automatically managed

**Relationships**:
- One Task belongs to one User (many-to-one relationship)

### Authentication Token
Represents an authenticated session containing user identity information

**Fields**:
- `token` (String): The JWT token string (primary key)
- `user_id` (UUID/String): Reference to the authenticated user (required)
- `expires_at` (DateTime): When the token expires (required)
- `created_at` (DateTime): When the token was issued
- `is_revoked` (Boolean): Whether the token has been revoked (default: false)

**Validation Rules**:
- Token must be a valid JWT format
- User_id must reference an existing, active user
- Expires_at must be in the future
- Created timestamp is automatically managed

**Relationships**:
- One Token belongs to one User (many-to-one relationship)

## Data Access Patterns

### User-Specific Filtering
All queries for tasks must be filtered by the authenticated user's ID to ensure data isolation between users.

### Indexes
- User.email: For efficient lookup during authentication
- Task.user_id: For efficient filtering of user-specific tasks
- AuthenticationToken.expires_at: For efficient cleanup of expired tokens

## State Transitions

### Task State Transitions
- `incomplete` → `completed`: When user marks task as done
- `completed` → `incomplete`: When user unmarks task as done

### User Account States
- `inactive` → `active`: When user completes registration
- `active` → `suspended`: When account is temporarily disabled
- `active` → `deleted`: When user deletes account

## Constraints

### Data Integrity
- Referential integrity: All foreign keys must reference existing records
- Unique constraints: User emails must be unique
- Not-null constraints: Required fields must have values

### Business Logic
- Users can only access their own tasks
- Tasks cannot be created without a valid user reference
- Authentication tokens expire after a configurable time period