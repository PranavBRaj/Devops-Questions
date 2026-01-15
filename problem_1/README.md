# Git & GitHub Workflow – Event Registration Form

This repository demonstrates a basic Git and GitHub workflow using a simple HTML Event Registration Form.  
It covers repository setup, file creation, branching, merging, and GitHub authentication using a Personal Access Token (PAT).

---

## Phase 1: Project Setup and Initialization

### Create Project Directory
Create a new directory and move into it.

```bash
mkdir question1
cd question1
```

### Initialize Git Repository
Initialize an empty Git repository.

```bash
git init
```

### Configure Git User Identity
Set the local Git username and email.

```bash
git config user.name "Your Name"
git config user.email "your_email@example.com"
```

---

## Phase 2: Creating the Application (Question 1)

### Create HTML File
Create an HTML file using a text editor.

```bash
gedit form.html
```

### Write HTML Code
Create a basic Event Registration Form containing:
- Name  
- Email  
- Phone  
- Register (Submit button)

Save the file and close the editor.

### Stage and Commit Changes
Add the file to staging and commit it.

```bash
git add .
git commit -m "First Commit"
```

---

## Phase 3: Connecting to GitHub & Authentication

### Create GitHub Repository
- Log in to GitHub
- Create a new empty repository named `question01`

### Rename Default Branch to Main

```bash
git branch -M main
```

### Add Remote Repository

```bash
git remote add origin https://github.com/YourUsername/question01.git
```

### Push Code to GitHub

```bash
git push -u origin main
```

---

## GitHub Authentication (Personal Access Token)

GitHub no longer supports password-based authentication for command-line access.

### Steps to Generate a Personal Access Token
1. Go to GitHub Settings
2. Open Developer Settings
3. Navigate to Personal Access Tokens → Tokens (classic)
4. Click Generate New Token (classic)
5. Add a note (e.g., Practice)
6. Set expiration date
7. Enable repo permissions
8. Generate and copy the token

When Git asks for a password, paste the token instead.

---

## Phase 4: Branching and Modification (Question 2)

### Create a New Branch

```bash
git branch update-form
```

### Switch to the New Branch

```bash
git checkout update-form
```

### Modify the HTML File
Add a new input field:
- Department

```bash
gedit form.html
```

Save and close the file.

### Commit the Changes

```bash
git add .
git commit -m "New Changes"
```

### Push the Branch to GitHub

```bash
git push origin update-form
```

---

## Phase 5: Merging and Finalizing

### Switch Back to Main Branch

```bash
git checkout main
```

### Merge the Feature Branch

```bash
git merge update-form
```

Recommended practice before merging:

```bash
git pull origin main
```

### Push Final Code

```bash
git push origin main
```

---

## Final Outcome

- Created and managed a Git repository
- Built a simple HTML Event Registration Form
- Used branching for feature updates
- Merged changes into the main branch
- Authenticated GitHub using a Personal Access Token

---

## Repository Structure

```text
question01/
├── form.html
└── README.md
```
