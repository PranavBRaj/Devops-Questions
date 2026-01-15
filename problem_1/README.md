Phase 1: Project Setup and Initialization
Create Project Directory

Open the Linux terminal and create a new directory for the project.
//
mkdir question1
cd question1
//
Initialize Git Repository

Initialize an empty Git repository inside the project folder.
//
git init
//
Configure Git User Identity

Set the local Git username and email.
//
git config user.name "Your Name"
git config user.email "your_email@example.com"
//
Phase 2: Creating the Application (Question 1)
Create HTML File

Use a text editor to create the HTML file.
//
gedit form.html
//
Write HTML Code

Add basic HTML code for an Event Registration Form with the following fields:

Name

Email

Phone

Register (Submit button)

Save the file and close the editor.

Stage and Commit Changes

Add the file to staging and commit it.
//
git add .
git commit -m "First Commit"
//
Phase 3: Connecting to GitHub & Authentication
Create GitHub Repository

Log in to GitHub.

Create a new empty repository named question01.

Rename Local Branch

Rename the default branch to main.
//
git branch -M main
//
Link Remote Repository

Add the GitHub repository as the remote origin.
//
git remote add origin https://github.com/YourUsername/question01.git
//
Push Code to GitHub

Push the local repository to GitHub.
//
git push -u origin main
//
Authentication Using Personal Access Token (PAT)

GitHub no longer allows password-based authentication for CLI access.

Steps to generate a token:

Go to GitHub Settings

Open Developer settings

Navigate to Personal access tokens → Tokens (classic)

Click Generate new token (classic)

Add a note (e.g., "Practice")

Set expiration date

Select repo permissions

Generate and copy the token

When Git asks for a password during push, paste the token instead.

Phase 4: Branching and Modification (Question 2)
Create a New Branch

Create a branch to isolate new changes.
//
git branch update-form
//
Switch to New Branch

Move to the newly created branch.
//
git checkout update-form
//
Modify HTML File

Open the file again and add a new input field:

Department
//
gedit form.html

//
Save and close the file.

Commit Changes

Stage and commit the updates.
//
git add .
git commit -m "New Changes"
//
Push Branch to GitHub

Push the new branch to the remote repository.
//
git push origin update-form
//
Phase 5: Merging and Finalizing
Switch Back to Main Branch
//
git checkout main
//
Merge Feature Branch

Merge the update-form branch into main.
//
git merge update-form
//

Note: Running git pull origin main before merging is a good practice to ensure the branch is up to date.

Push Final Code

Push the merged changes to GitHub.
//
git push origin main
//
Final Outcome

Successfully created and version-controlled an HTML form

Used branching for feature updates

Merged changes cleanly into the main branch

Learned GitHub authentication using Personal Access Tokens
