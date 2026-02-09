---
id: 1
title: "todo-fullstack-constitution-update"
stage: "constitution"
date_iso: "2026-02-09"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "todo-fullstack-app"
branch: "main"
user: "user"
command: "/sp.constitution"
labels: ["constitution", "setup", "governance"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - ".specify/memory/constitution.md"
tests_yaml: []
prompt_text: |
  Project: Todo Full-Stack Web Application (AI-Agentic, Spec-Driven)

  Objective:
  Transform a basic console-based todo application into a modern, secure, multi-user full-stack web application using an agentic development workflow (Spec → Plan → Tasks → Implementation) with zero manual coding.

  Core principles:
  - Spec-first development (all implementation must strictly follow written specs)
  - Deterministic agent execution (same spec → same outcome)
  - Security-by-design (authentication and authorization enforced at every layer)
  - Data integrity and isolation (each user only accesses their own data)
  - Clear separation of concerns (frontend, backend, auth, database)
  - Reproducibility (entire build process reproducible from prompts alone)

  Key standards:
  - No manual coding allowed; all code must be generated via Claude Code
  - Every feature must trace back to a written spec requirement
  - REST API must strictly follow defined endpoints and HTTP semantics
  - Authentication must use JWT-based stateless verification
  - Backend must never trust client-provided user identifiers without token verification
  - Database access must be filtered by authenticated user at all times
  - Environment configuration must be externalized via environment variables

  Architecture standards:
  - Frontend: Next.js 16+ using App Router
  - Backend: Python FastAPI
  - ORM: SQLModel
  - Database: Neon Serverless PostgreSQL
  - Authentication: Better Auth (JWT-based)
  - API communication: JSON over HTTPS
  - Authorization: Bearer JWT tokens in Authorization header

  Security standards:
  - All API endpoints require valid JWT after authentication phase
  - Requests without valid tokens must return 401 Unauthorized
  - User ID in JWT must match or override any route-based user identifier
  - JWT secret must be shared securely via BETTER_AUTH_SECRET
  - Token expiration must be enforced
  - No cross-user data access under any circumstances

  Development constraints:
  - All 5 Basic Level features must be implemented as a web application
  - Must expose RESTful CRUD endpoints for tasks
  - Must support multi-user concurrency
  - Persistent storage is mandatory (no in-memory data)
  - Frontend must be responsive and production-ready
  - No backend session storage (stateless auth only)

  Process constraints:
  - Follow Agentic Dev Stack workflow strictly:
    1. Write spec
    2. Generate plan
    3. Break into tasks
    4. Implement via Claude Code
  - Each phase must be reviewable and self-contained
  - No skipping or merging of phases

  Success criteria:
  - Full-stack application runs end-to-end
  - Users can sign up, sign in, and manage their own tasks
  - All API endpoints are protected and user-scoped
  - JWT authentication works across frontend and backend
  - Database persists data correctly per user
  - Project can be rebuilt entirely from specs and prompts
  - Reviewers can audit specs, plans, tasks, and outputs independently
response_text: |
  Updated the project constitution at .specify/memory/constitution.md with all the required principles for the Todo Full-Stack Web Application. The constitution now includes:
  - Core Principles: Spec-First Development, Security-by-Design, Data Integrity and Isolation, Clear Separation of Concerns, Agentic Dev Stack Workflow, Architecture Standards Compliance
  - Security Requirements section
  - Development Workflow section
  - Governance section
  All principles reflect the requirements for a secure, multi-user web application with proper authentication and authorization.
outcome: "completed"
evaluation: "success"
---

# Constitution Update for Todo Full-Stack Web Application

## Summary

Created a comprehensive constitution for the Todo Full-Stack Web Application project that enforces spec-first development, security-by-design, and proper agentic workflow practices.

## Details

The constitution establishes core principles that guide the development of the multi-user todo application with proper authentication, data isolation, and architectural standards.