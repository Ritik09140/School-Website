# 📤 Complete Guide: Push Code to GitHub + VS Code

---

## 🎯 Complete Workflow

```
┌─────────────────────────────────────────────────────────────┐
│  1. Download/Create Project Folder                          │
│     ↓                                                        │
│  2. Open in VS Code                                         │
│     ↓                                                        │
│  3. Test Locally (Live Server)                              │
│     ↓                                                        │
│  4. Push to GitHub                                          │
│     ↓                                                        │
│  5. Deploy Online (Netlify/Vercel)                          │
│     ↓                                                        │
│  6. Share with World! 🌍                                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 📥 STEP 1: Download Project Files

### Option A: Download as ZIP
1. Go to GitHub (if uploaded)
2. Click "Code" button
3. Click "Download ZIP"
4. Extract folder to your computer

### Option B: Clone from GitHub
```bash
git clone https://github.com/YOUR_USERNAME/school-website.git
cd school-website
```

---

## 🔧 STEP 2: Open in VS Code

### Windows:
```bash
# In Command Prompt or PowerShell
cd path\to\school-website
code .
```

### Mac/Linux:
```bash
cd /path/to/school-website
code .
```

✅ VS Code opens with your project

---

## 🚀 STEP 3: Test Locally with Live Server

### Install Live Server Extension:
1. Click **Extensions** icon (left sidebar)
   ```
   [Extensions icon looks like: ⊞]
   ```
2. Search for **"Live Server"**
3. Click **Install** (by Ritwick Dey)
4. Reload VS Code

### Run Live Server:
- **Right-click** `index.html` → **"Open with Live Server"**
- OR Press: **Alt + L**, then **Alt + O**
- OR Click **"Go Live"** button (bottom-right)

✅ Website opens at: `http://127.0.0.1:5500`

---

## 🌐 STEP 4: Push to GitHub

### 4a. Create GitHub Repository

1. Go to https://github.com
2. Click **"+"** icon (top-right)
3. Click **"New repository"**
4. Enter name: `school-website`
5. Click **"Create repository"**
6. **Copy the repository URL** (looks like: `https://github.com/username/school-website.git`)

### 4b. Push Code from VS Code

#### Method 1: Using VS Code Terminal (Easiest)

1. Open Terminal in VS Code: **Ctrl + `** (backtick)

2. Initialize Git:
```bash
git init
```

3. Add all files:
```bash
git add .
```

4. Create first commit:
```bash
git commit -m "Initial commit: Premium school website"
```

5. Add GitHub repository URL:
```bash
git remote add origin https://github.com/YOUR_USERNAME/school-website.git
```

6. Create main branch:
```bash
git branch -M main
```

7. Push to GitHub:
```bash
git push -u origin main
```

✅ **Code is now on GitHub!**

#### Method 2: Using Git Bash/Command Line

```bash
# 1. Navigate to project folder
cd C:\Users\YourName\Documents\school-website

# 2. Initialize Git
git init

# 3. Add all files
git add .

# 4. Commit
git commit -m "Initial commit: School website with all features"

# 5. Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/school-website.git

# 6. Push to GitHub
git branch -M main
git push -u origin main

# Done! 🎉
```

---

## 📤 STEP 5: Deploy Online

### Choose One:

#### ☁️ Option A: Netlify (Recommended)

1. Go to https://netlify.com
2. Click **"Sign up"** (use GitHub account)
3. Click **"New site from Git"**
4. Select **GitHub** as provider
5. Authorize Netlify
6. Select **school-website** repository
7. Click **"Deploy site"**

✅ **Your website is LIVE!** Get URL: `https://yourname.netlify.app`

---

#### ☁️ Option B: Vercel

1. Go to https://vercel.com
2. Click **"Sign Up"** (use GitHub)
3. Click **"Import Project"**
4. Select **school-website** repository
5. Click **"Import"**
6. Click **"Deploy"**

✅ **Website is LIVE at:** `https://yourproject.vercel.app`

---

#### ☁️ Option C: GitHub Pages (Free!)

1. Go to your GitHub repository
2. Click **Settings** (top-right)
3. Scroll to **"Pages"** (left sidebar)
4. Under "Source", select **"main"** branch
5. Click **"Save"**

✅ **Website is LIVE at:** `https://yourusername.github.io/school-website`

---

## 🔄 STEP 6: Update Code (Later)

After making changes locally:

```bash
# 1. Check what changed
git status

# 2. Add changed files
git add .

# 3. Commit with message
git commit -m "Update: Add teacher photos"

# 4. Push to GitHub
git push

# ✅ Website auto-updates online!
```

---

## 📝 Example: Complete First-Time Setup

```bash
# 1. Open VS Code
code .

# 2. Open Terminal (Ctrl + `)

# 3. Initialize Git
git init

# 4. Add all files
git add .

# 5. First commit
git commit -m "Initial commit: New Achiever School Website"

# 6. Add GitHub repo URL (replace with YOUR URL)
git remote add origin https://github.com/YOUR_USERNAME/school-website.git

# 7. Create main branch
git branch -M main

# 8. Push to GitHub
git push -u origin main

# ✅ Done! Check GitHub - your code is there!

# 9. Deploy to Netlify (optional)
# Go to https://netlify.com
# Connect GitHub repo
# Auto-deploys on every push!
```

---

## ✅ Verification Checklist

- [ ] Downloaded project files
- [ ] Opened in VS Code
- [ ] Installed Live Server
- [ ] Tested locally (Live Server running)
- [ ] Created GitHub account
- [ ] Created GitHub repository
- [ ] Pushed code to GitHub (git push successful)
- [ ] Deployed online (Netlify/Vercel/GitHub Pages)
- [ ] Website is live with working URL
- [ ] All links work correctly
- [ ] Images display properly
- [ ] Responsive on mobile (F12 → Device Toolbar)

---

## 🆘 Troubleshooting

### ❌ "Git is not recognized"
**Solution:** Install Git from https://git-scm.com/download
Then restart VS Code and Terminal

### ❌ "Permission denied"
**Solution:** You need to set up SSH key
```bash
ssh-keygen -t rsa -b 4096
# Add key to GitHub Settings → SSH Keys
```

### ❌ "Failed to push"
**Solution:** Pull first, then push
```bash
git pull origin main
git push origin main
```

### ❌ "Website still shows old version"
**Solution:** Clear browser cache
- Ctrl + Shift + Delete (Windows)
- Cmd + Shift + Delete (Mac)
- Hard refresh: Ctrl + F5

### ❌ "Live Server not working"
**Solution:** 
1. Restart VS Code completely
2. Reinstall Live Server extension
3. Try port 3000: `http://127.0.0.1:3000`

---

## 🎯 GitHub Commands Quick Reference

| Command | Purpose |
|---------|---------|
| `git init` | Start Git tracking |
| `git add .` | Add all files to staging |
| `git commit -m "msg"` | Save changes with message |
| `git push` | Upload to GitHub |
| `git pull` | Download latest from GitHub |
| `git status` | See what changed |
| `git log` | View commit history |
| `git branch` | List all branches |

---

## 🎉 You've Successfully:

✅ Created premium school website
✅ Tested locally in VS Code
✅ Pushed code to GitHub
✅ Deployed online for the world
✅ Built professional web presence

---

## 📞 Next Steps

1. Share website URL with parents & students
2. Add more teacher photos as they're ready
3. Keep updating with latest news & notices
4. Monitor website performance
5. Collect feedback from users

---

**Your school website is now LIVE! 🚀🎓**

---

## 📖 Useful Links

- **Git Guide:** https://git-scm.com/docs
- **GitHub:** https://github.com
- **Netlify:** https://netlify.com
- **Vercel:** https://vercel.com
- **VS Code:** https://code.visualstudio.com

---

**Made with ❤️ for The New Achiever Pre-Science School**
