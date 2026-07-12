# SQL Injection

## Definition

SQL Injection is a web attack where malicious SQL queries are inserted into user input fields to manipulate a database.

## Example

Normal Query:

```sql
SELECT * FROM users WHERE username='admin';
```

Malicious Input:

```text
' OR 1=1--
```

## Prevention

- Prepared Statements
- Parameterized Queries
- Input Validation
- Least Privilege Access

## Tools

- SQLMap
- Burp Suite

---
*These notes are for educational purposes only.*
