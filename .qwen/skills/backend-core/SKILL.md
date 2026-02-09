---
name: backend-core
description: Generate backend routes, handle HTTP requests/responses, and connect applications to databases.
---

# Backend Core Development

## Instructions

1. **Routing**
   - Define RESTful routes (GET, POST, PUT, DELETE)
   - Organize routes by feature or module
   - Use clear and consistent URL naming

2. **Request & Response Handling**
   - Parse request parameters, body, and headers
   - Validate incoming data
   - Send structured JSON responses
   - Handle errors with proper status codes

3. **Database Integration**
   - Connect to databases (SQL or NoSQL)
   - Perform CRUD operations
   - Use environment variables for credentials
   - Implement basic query optimization

## Best Practices
- Follow MVC or modular architecture
- Always validate and sanitize inputs
- Use async/await for non-blocking operations
- Centralize error handling
- Keep business logic separate from routes

## Example Structure
```js
// routes/user.routes.js
import express from "express";
import { getUsers, createUser } from "../controllers/user.controller.js";

const router = express.Router();

router.get("/users", getUsers);
router.post("/users", createUser);

export default router;
