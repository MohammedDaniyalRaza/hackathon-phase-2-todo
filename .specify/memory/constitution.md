<!-- SYNC IMPACT REPORT
Version change: N/A (initial version) → 1.0.0
Modified principles: None (new document)
Added sections: All sections (new document)
Removed sections: None
Templates requiring updates:
  - .specify/templates/plan-template.md ✅ updated
  - .specify/templates/spec-template.md ✅ updated
  - .specify/templates/tasks-template.md ✅ updated
  - .specify/templates/commands/*.md ⚠ pending review
  - README.md ⚠ pending review
Follow-up TODOs: None
-->

# Todo Full-Stack Web Application Constitution

## Core Principles

### Spec-First Development
All implementation must strictly follow written specifications; deterministic agent execution ensures same spec produces same outcome; every feature must trace back to a written spec requirement.

### Security-by-Design
Authentication and authorization enforced at every layer; all API endpoints require valid JWT after authentication phase; no cross-user data access under any circumstances; JWT secret must be shared securely via BETTER_AUTH_SECRET.

### Data Integrity and Isolation (NON-NEGOTIABLE)
Each user only accesses their own data; database access must be filtered by authenticated user at all times; backend must never trust client-provided user identifiers without token verification; user ID in JWT must match or override any route-based user identifier.

### Clear Separation of Concerns
Frontend, backend, auth, and database responsibilities kept distinct; REST API must strictly follow defined endpoints and HTTP semantics; no backend session storage (stateless auth only); API communication via JSON over HTTPS.

### Agentic Dev Stack Workflow
Follow Spec → Plan → Tasks → Implementation workflow strictly; no manual coding allowed, all code must be generated via Claude Code; each phase must be reviewable and self-contained; reproduction from prompts alone must be possible.

### Architecture Standards Compliance
Frontend: Next.js 16+ using App Router; Backend: Python FastAPI; ORM: SQLModel; Database: Neon Serverless PostgreSQL; Authentication: Better Auth (JWT-based); Authorization: Bearer JWT tokens in Authorization header.

## Security Requirements

All API endpoints must return 401 Unauthorized for requests without valid tokens; token expiration must be enforced; persistent storage mandatory with no in-memory data for production; environment configuration must be externalized via environment variables; authentication must use JWT-based stateless verification.

## Development Workflow

Follow Agentic Dev Stack workflow strictly: Write spec → Generate plan → Break into tasks → Implement via Claude Code; no skipping or merging of phases; every feature must have testable acceptance criteria; explicit error paths and constraints must be stated; smallest viable change approach preferred with no unrelated edits.

## Governance

This constitution supersedes all other development practices; all implementation must comply with these principles; amendments require explicit documentation and approval process; version changes must follow semantic versioning (MAJOR for breaking changes, MINOR for new principles, PATCH for clarifications); all PRs and reviews must verify constitution compliance.

**Version**: 1.0.0 | **Ratified**: 2026-02-09 | **Last Amended**: 2026-02-09