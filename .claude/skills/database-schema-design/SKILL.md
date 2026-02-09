---
name: database-schema-design
description: Design robust database schemas with tables, migrations, and relationships. Use for scalable applications.
---

# Database Schema Design

## Instructions

1. **Schema planning**
   - Identify core entities
   - Define clear relationships
   - Normalize data where required

2. **Table creation**
   - Use appropriate data types
   - Define primary and foreign keys
   - Apply indexes for performance

3. **Migrations**
   - Version-controlled schema changes
   - Reversible up/down migrations
   - Environment-safe execution

## Best Practices
- Follow naming conventions consistently
- Avoid redundant data
- Use migrations for every schema change
- Design with scalability in mind
- Document relationships and constraints

## Example Structure
```sql
-- users table
CREATE TABLE users (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(150) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- posts table
CREATE TABLE posts (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  title VARCHAR(200),
  body TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
);
