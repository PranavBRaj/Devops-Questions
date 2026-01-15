# Jenkins CI Setup with GitHub – Student Portal Project

This project demonstrates a **complete Jenkins Continuous Integration (CI) workflow** using:
- Jenkins (WAR-based installation)
- Java (OpenJDK 21)
- GitHub repository integration
- SCM polling trigger
- Freestyle Jenkins job

---

## Phase 1: Environment Setup & Jenkins Installation

### Check Java Installation
Open the terminal and check the Java version.

```bash
java --version
```

(Java is not installed initially, so the command fails.)

### Install Java (OpenJDK 21)

```bash
sudo apt update
sudo apt install openjdk-21-jdk -y
```

Verify installation:

```bash
java --version
```

---

## Download and Run Jenkins (WAR File Method)

### Cleanup Previous Failed Attempts
Remove old Jenkins files from earlier failed installations.

```bash
rm -rf ~/.jenkins
rm -f jenkins.war
```

### Download Jenkins WAR File

```bash
wget https://updates.jenkins.io/download/war/2.479.1/jenkins.war
```

### Run Jenkins

```bash
java -jar jenkins.war
```

Wait until the terminal shows:

```
Jenkins is fully up and running
```

---

## Phase 2: Jenkins Initialization

### Unlock Jenkins
1. Open Firefox  
2. Go to:

```
http://localhost:8080
```

3. Copy the **Administrator password** from the terminal output
4. Paste it into the Jenkins unlock page
5. Click **Continue**

### Install Plugins
- Select **Install suggested plugins**
- Wait for installation to complete (some plugin warnings may be ignored)

### Create Admin User
- **Username:** aniket-14  
- **Password:** (user-defined)  
- **Full Name:** Optional  
- **Email:** Provided  

Click **Save and Continue**

### Instance Configuration
- Keep Jenkins URL as:

```
http://localhost:8080/
```

- Click **Save and Finish**
- Click **Start using Jenkins**

---

## Phase 3: GitHub Repository Setup

### Create GitHub Repository
- Log in to GitHub
- Create a **public repository** named `StudentPortal`

### Clone Repository and Add Content

```bash
git clone https://github.com/aniket-14/StudentPortal.git
cd StudentPortal
```

### Create HTML File

```bash
gedit index.html
```

Add the following content:

```html
<h1>Student</h1>
<h2>Jenkins</h2>
<h3>Testing</h3>
```

---

## GitHub Personal Access Token (Required)

GitHub no longer supports password-based authentication.

### Generate Token
1. GitHub Settings
2. Developer settings
3. Personal access tokens → Tokens (classic)
4. Generate new token
5. Enable **repo** permissions
6. Copy the token

### Push Code to GitHub

```bash
git add .
git commit -m "First Commit"
git push origin main
```

When prompted for a password, **paste the Personal Access Token**.

---

## Phase 4: Jenkins Job Configuration

### Create New Jenkins Job
1. Open Jenkins Dashboard
2. Click **New Item**
3. Job Name: `Student`
4. Select **Freestyle project**
5. Click **OK**

---

### Source Code Management (SCM)
- Select **Git**
- Repository URL:

```
https://github.com/aniket-14/StudentPortal.git
```

#### Add Credentials
- Username: `aniket-14`
- Password: GitHub Personal Access Token
- ID: `jenkins-test`

Select this credential.

### Branch Specifier
Change:

```
*/master
```

To:

```
*/main
```

---

### Build Triggers
Enable **Poll SCM**

```text
H * * * *
```

(This checks for GitHub changes periodically.)

---

### Build Steps
Add **Execute shell** and paste the following script:

```bash
echo "Starting Student Portal Jenkins"
echo "Build Time"
date

echo "Current Directory"
pwd

echo "List all the repo files"
ls -l

echo "Latest Commits"
git --no-paper log -3 --oneline

echo "Build Successfully Done"
```

Click **Save**

---

## Phase 5: Testing the Build

### Manual Build
1. Click **Build Now**
2. Open **Build #1**
3. Check **Console Output**
4. Verify build ends with **SUCCESS**

---

### SCM Polling Test (Automatic Build)

Edit the file:

```bash
gedit index.html
```

Make a change, then commit and push:

```bash
git add .
git commit -m "Another Change"
git push origin main
```

### Result
- Jenkins automatically detects the change
- A new build (**Build #2**) starts automatically

---

## Final Outcome

- Jenkins successfully installed using WAR file
- Java environment configured correctly
- GitHub repository integrated with Jenkins
- CI pipeline triggered using SCM polling
- Builds executed automatically on code changes

---

## Project Structure

```text
StudentPortal/
├── index.html
└── README.md
```
