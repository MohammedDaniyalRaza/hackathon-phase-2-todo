---
name: auth-skill
description: Implement secure authentication systems including signup, signin, password hashing, JWT tokens, and Better Auth integration.
---

# Authentication Skill

## Instructions

1. **User Authentication Flow**
   - User signup and signin
   - Input validation
   - Error handling and responses

2. **Password Security**
   - Hash passwords using bcrypt or argon2
   - Never store plain-text passwords
   - Secure password comparison

3. **Token-Based Authentication**
   - Generate JWT tokens on login
   - Use access and refresh tokens
   - Token expiration and renewal

4. **Authorization**
   - Protect private routes
   - Middleware for token verification
   - Role-based access control (optional)

5. **Better Auth Integration**
   - Configure Better Auth provider
   - Social login support (Google, GitHub, etc.)
   - Session management

## Best Practices
- Always hash passwords before saving
- Use HTTPS for auth routes
- Store JWTs securely (httpOnly cookies preferred)
- Short-lived access tokens
- Proper logout and token invalidation
- Follow OWASP authentication guidelines

## Example Structure
```js
// Signup
app.post("/signup", async (req, res) => {
  const hashedPassword = await bcrypt.hash(req.body.password, 10);
  // save user
});

// Signin
app.post("/signin", async (req, res) => {
  const isValid = await bcrypt.compare(password, user.password);
  const token = jwt.sign({ id: user.id }, process.env.JWT_SECRET);
  res.json({ token });
});

// Protected Route
app.get("/dashboard", verifyToken, (req, res) => {
  res.send("Authorized User");
});
