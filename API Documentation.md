# API Documentation
This is a comprehensive API document with clear instructions on how to use the APIs, including sample request and response payloads.

---

### API 1: Create Account
This API is for creating a new account with the provided username and password.

**Endpoint:**
`/create`

**Request**  
The request payload must be a JSON containing the following fields:
- "username": a string representing the desired username for the account, with a minimum length of 3 characters and a maximum length of 32 characters.
- "password": a string representing the desired password for the account, with a minimum length of 8 characters and a maximum length of 32 characters, 
containing at least 1 uppercase letter, 1 lowercase letter, and 1 number.

Sample Request:
```
{
    "username": "test1",
    "password": "Test123321"
}
```

**Response**
The response payload will be a JSON with the following fields:
- "success": a boolean field indicating the outcome of the account creation process, with "true" indicating a successful creation and "false" indicating otherwise.
- "reason": a string field indicating the reason for a failed account creation process, such as "Username already exists".

Sample Response (Success):
```
{
    "reason": "Account created successfully",
    "success": true
}
```

Sample Response (Failure):
```
{
    "reason": "Username already exists",
    "success": false
}
```

Sample Response (Failure):
```
{
    "reason": "Password is not valid",
    "success": false
}
```

### API 2: Verify Account and Password
This API verifies the provided username and password.  
Remark: If the password verification fails five times, the user should wait one minute before attempting to verify the password again.

**Endpoint:**
`/verify`

**Request**  
The request payload must be a JSON containing the following fields:
- "username": a string representing the username of the account being accessed.
- "password": a string representing the password being used to access the account.

Sample Request:
```
{
    "username": "test1",
    "password": "Test123321"
}
```

**Response**
The response payload will be a JSON with the following fields:
- "success": a boolean field indicating the validity of the password provided for the given username, with "true" indicating that the password is correct and "false" indicating otherwise.
- "reason": a string field indicating the reason if needed.

Sample Response (Success):
```
{
    "reason": "Account verified successfully",
    "success": true
}
```

Sample Response (Failure):
```
{
    "reason": "Invalid username or password",
    "success": false
}
```

Sample Response (Failure):
```
{
    "reason": "Account is locked. Please try again 1 minute later",
    "success": false
}
```
