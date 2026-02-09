---
id: 0001
title: update-claude-md-project-reqs
stage: general
date: 2026-02-09
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: DANIYAL
command: Update CLAUDE.md file based on project requirements
labels: ["project-setup", "configuration", "todo-app"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - /mnt/c/Users/DANIYAL/Desktop/Hackathon-2-phase-2/CLAUDE.md
tests:
 - none
---

## Prompt

Update the claude.md file based on my project requirements. In this file:
- Use Auth Agent for authentication
- Use Frontend Agent for frontend development (e.g., Next.js)
- Use DB Agent for database design and operations
- Use Backend Agent for FastAPI development

Below are my project requirements:
"""
Phase II: Todo Full-Stack Web Application
Basic Level Functionality
Objective: Using Claude Code and Spec-Kit Plus transform the console app into a modern multi-user web application with persistent storage.
💡Development Approach: Use the Agentic Dev Stack workflow: Write spec → Generate plan → Break into tasks → Implement via Claude Code. No manual coding allowed. We will review the process, prompts, and iterations to judge each phase and project.
Requirements
Implement all 5 Basic Level features as a web application
Create RESTful API endpoints
Build responsive frontend interface
Store data in Neon Serverless PostgreSQL database
Authentication – Implement user signup/signin using Better Auth
Technology Stack
Layer
Technology
Frontend
Next.js 16+ (App Router)
Backend
Python FastAPI
ORM
SQLModel
Database
Neon Serverless PostgreSQL
Spec-Driven
Claude Code + Spec-Kit Plus
Authentication
Better Auth

Better Auth can be configured to issue JWT (JSON Web Token) tokens when users log in. These tokens are self-contained credentials that include user information and can be verified by any service that knows the secret key.
How It Works
User logs in on Frontend → Better Auth creates a session and issues a JWT token
Frontend makes API call → Includes the JWT token in the Authorization: Bearer <token> header
Backend receives request → Extracts token from header, verifies signature using shared secret
Backend identifies user → Decodes token to get user ID, email, etc. and matches it with the user ID in the URL
Backend filters data → Returns only tasks belonging to that user
"""

## Response snapshot

Updated the CLAUDE.md file to reflect the project requirements for the Todo Full-Stack Web Application. The changes include:

1. Added a Project Requirements section with details about Phase II: Todo Full-Stack Web Application
2. Included information about specialized agent usage (Auth Agent, Frontend Agent, DB Agent, Backend Agent)
3. Added Better Auth integration details with JWT token handling flow
4. Updated the Technology Stack table with specific technologies
5. Enhanced the Architect Guidelines to address the Todo application requirements
6. Added Agentic Dev Stack Workflow section with agent-specific responsibilities
7. Updated the Project Structure to include new directories for backend, frontend, auth, and database
8. Modified various sections to align with the project goals

## Outcome

- ✅ Impact: Successfully updated CLAUDE.md with comprehensive project requirements and agent usage guidelines
- 🧪 Tests: none required
- 📁 Files: Updated CLAUDE.md with project-specific configurations
- 🔁 Next prompts: Ready to proceed with spec creation for the Todo application
- 🧠 Reflection: The updated CLAUDE.md now serves as a comprehensive guide for implementing the Todo Full-Stack Web Application using the Agentic Dev Stack workflow

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin creating the feature specification using the updated guidelines
