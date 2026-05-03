# Bonus Task 7: Login Attempt Limit (Integrated with Existing System)

## Task 7: Limit Login Attempts

### Enhances the existing `login()` function by locking a user after multiple failed attempts.

- **Function name**: `login()`

- **Params**:  
  - user_db (dictionary) – stores usernames and passwords  
  - attempts_db (dictionary) – tracks failed login attempts per user  

- **returns**: auth_status (boolean) – True if login successful, False otherwise  

### Notes
- *Same logic as the existing `login()` function, but with added tracking.*  
- *If username does not exist → print "User not found".*  
- *If password is incorrect → increase attempt count in attempts_db.*  
- *If a user reaches 3 failed attempts → print "Account locked" and block login.*  
- *If login is successful → reset attempts to 0.*  

# Bonus Task 8: Role-Based Access Control (Integrated with Existing System)

## Task 8: Add User Roles (Admin vs Normal User)

### Extends the system to support different user roles.

- **Function name**: `create_user`

- **Params**:  
  - user_db (dictionary) – stores usernames and passwords  
  - role_db (dictionary) – stores usernames and their roles (e.g., "admin", "user")  

- **returns**:  
  - user_db (dictionary) – updated  
  - role_db (dictionary) – updated  
  - Prints the username, password, and assigned role  

---

### Notes
- *Same logic as `create_new_user()`.*  
- *Ensure the username is not empty and does not already exist.*  
- *Ask the user to input a role ("admin" or "user").*  
- *Store the role in role_db using the username as the key.*  
- *Generate a strong password using `generate_password()`.*  

---

## Additional Function: Admin-Only Access

### Restricts certain actions to admin users only.

- **Function name**: `admin_view_users()`

- **Params**:  
  - user_db (dictionary) – stores usernames and passwords in plaintext 
  - role_db (dictionary) – stores user roles  
  - current_user (string) – the username currently logged in  

- **returns**: none  
  - Prints all users (only if admin)  

### Notes
- *Check if current_user exists in role_db.*  
- *If role is "admin", allow access and call `view_user_data(user_db)`.*  
- *If not, print "Access Denied".*  