# Password Reset — Feature Requirements

## Context

The application is a REST API for a user management platform. Authentication is handled via JWT tokens. The platform stores user accounts and supports self-service password recovery.

The following user stories describe the password reset feature to implement.

---

## User Stories

### US-01 — Request a password reset

**As a** registered user who has forgotten my password,  
**I want to** request a password reset link by providing my email address,  
**So that** I can regain access to my account.

**Acceptance criteria:**
- The endpoint accepts a valid email address
- If the email is associated with a registered account, a reset link is sent to that address
- The reset link contains a secure token that can be used to complete the reset
- The endpoint responds with a generic confirmation message

---

### US-02 — Reset the password using the token

**As a** user who received a password reset link,  
**I want to** submit a new password along with the token from the link,  
**So that** my account password is updated and I can log in again.

**Acceptance criteria:**
- The endpoint accepts a reset token and a new password
- The token must be valid
- If the token is valid, the user's password is updated in the database
- The endpoint responds with a confirmation that the password has been changed
- Authentication is not required to call this endpoint (the token serves as proof of identity)

---

### US-03 — Security baseline

**As a** platform operator,  
**I want** the password reset flow to follow basic security practices,  
**So that** user accounts are not easily compromised through the reset mechanism.

**Acceptance criteria:**
- Reset tokens must be unpredictable and unique per request
- Tokens must be associated with a specific user account
- Passwords must be stored securely (hashed, not in plaintext)
- The feature must integrate with the existing authentication infrastructure
