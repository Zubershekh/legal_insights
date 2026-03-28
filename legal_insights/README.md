# 🏛️ LEGAL INSIGHTS - Live Law Inspired Legal News Website

## ✨ FEATURES

### What Your Dad Can Post:
- ✅ **Judgment Posts** - News articles about court judgments with full details
- ✅ **Law/Act Posts** - Articles about new laws and amendments
- ✅ **Categories** - Supreme Court, High Court, Criminal Law, Civil Law, etc.
- ✅ **Featured Posts** - Highlight important news on homepage
- ✅ **Images** - Upload featured images for posts
- ✅ **PDFs** - Attach judgment/law documents
- ✅ **Tags** - For better SEO and organization
- ✅ **View Counter** - Track popular posts

### Public Website (No Login Required):
- 📱 **Fully Mobile Responsive** - Perfect on phones, tablets, and desktops
- 🎨 **Live Law Inspired Design** - Professional news portal look
- 🏠 **Homepage** - Featured stories + latest judgments + latest laws
- 📰 **Judgment Posts** - Browse and read judgment articles
- 📜 **Law Posts** - Browse and read law/act articles
- 🔍 **Search** - Find posts by keywords
- 📂 **Categories** - Browse by Supreme Court, Criminal Law, etc.
- 📥 **PDF Downloads** - Download judgment and law documents

### Admin Panel (Only Your Dad):
- 🔐 **Secure Login** - Only for admin user
- 📊 **Dashboard** - View statistics
- ➕ **Add/Edit/Delete** - Full CRUD for all content
- 🖼️ **Image Uploads** - Featured images for posts
- 📄 **PDF Uploads** - Judgment and law documents
- ✅ **Publish/Draft** - Control post visibility
- ⭐ **Featured Toggle** - Mark posts as featured for homepage
- 📱 **Mobile Friendly Admin** - Manage from phone/tablet

---

## 🚀 INSTALLATION (WINDOWS)

### Prerequisites:
- Python 3.8 or higher installed
- Windows 10/11

### Step 1: Extract the Project
Extract the `legal_insights` folder to your computer (e.g., `C:\legal_insights`)

### Step 2: Run Automatic Setup
1. Open the `legal_insights` folder
2. **Double-click** on `WINDOWS_SETUP.bat`
3. Wait for installation to complete

### Step 3: Create Admin Account
Open Command Prompt in the `legal_insights` folder and run:

```cmd
venv\Scripts\activate
python manage.py createsuperuser
```

When prompted:
- **Username**: admin (or whatever you want)
- **Email**: press Enter to skip
- **Password**: type password (won't show while typing - that's normal!)
- **Password again**: type same password

### Step 4: Start the Website
```cmd
python manage.py runserver
```

### Step 5: Open in Browser
- **Public Website**: http://127.0.0.1:8000/
- **Admin Login**: http://127.0.0.1:8000/admin-login/

---

## 📝 HOW TO USE (First Time)

### 1. Add Categories First
Before posting, create categories:

1. Login at http://127.0.0.1:8000/admin-login/
2. Click **"Categories"**
3. Click **"Add New"**
4. Add these one by one:
   - **Supreme Court**
   - **High Courts**
   - **Criminal Law**
   - **Civil Law**
   - **Constitutional Law**
   - **Corporate Law**
   - **Family Law**

### 2. Post Your First Judgment

1. Click **"Judgment Posts"** → **"Add New"**
2. Fill in the form:

**Example:**
```
Title: Supreme Court Grants Bail in Money Laundering Case

Court Name: Supreme Court of India

Judgment Date: 2024-02-08

Case Number: Criminal Appeal No. 456/2024

Judges: Justice ABC, Justice XYZ

Summary: The Supreme Court today granted bail to the accused in a money laundering case, observing that prolonged incarceration without trial violates fundamental rights.

Full Content: 
[Write complete article here]

The Supreme Court on Thursday granted bail to [name] in a money laundering case, noting that the accused has been in custody for over two years without trial.

A bench comprising Justice ABC and Justice XYZ observed that prolonged detention without conviction violates the constitutional right to life and liberty under Article 21.

The court noted that the trial is unlikely to conclude in the near future, and continuing detention would cause undue hardship to the accused.

[Continue with full analysis, background, legal points, implications, etc.]

Category: Select "Supreme Court" or "Criminal Law"

Tags: bail, money laundering, supreme court, article 21

Featured Image: (Optional - upload if you have)

PDF File: (Optional - upload judgment PDF if available)

☑️ Is Published (Check this to publish immediately)
☑️ Is Featured (Check this to show on homepage)
```

3. Click **"Save"**

### 3. Post Your First Law/Act

1. Click **"Law/Act Posts"** → **"Add New"**
2. Fill in:

**Example:**
```
Title: New Criminal Law Amendments Come Into Force from July 2024

Act Name: Bharatiya Nyaya Sanhita, 2023

Act Number: Act No. 45 of 2023

Enactment Date: 2024-07-01

Ministry: Ministry of Home Affairs

Summary: Major criminal law reforms replacing the IPC, CrPC, and Evidence Act came into effect today, marking a significant shift in India's criminal justice system.

Full Content:
[Write complete article with analysis]

Key Provisions:
- Replaces Indian Penal Code with Bharatiya Nyaya Sanhita
- Introduces community service as punishment
- Enhances provisions for crimes against women
- Digital evidence provisions strengthened

Category: Criminal Law

Tags: criminal law, amendments, new law, BNS

☑️ Is Published
☑️ Is Featured (if important)
```

3. Click **"Save"**

---

## 💡 WRITING TIPS FOR YOUR DAD

### 1. **Titles Should Be Catchy Headlines**
❌ Bad: "Judgment in Case No. 123/2024"
✅ Good: "SC Grants Bail in Money Laundering Case, Cites Fundamental Rights"

### 2. **Summary = Preview (2-3 sentences)**
This shows in listing pages. Make it compelling!

Example:
"The Supreme Court today granted bail in a high-profile money laundering case, observing that prolonged detention without trial violates constitutional rights. The bench noted that fundamental rights cannot be sacrificed at the altar of investigation."

### 3. **Full Content = Complete Article**
This is where you write the complete news story with:
- What happened?
- When and where?
- Who are the parties?
- What did the court say?
- Legal analysis
- Implications
- Background

Write like a news article, not just facts!

### 4. **Use Featured Wisely**
Only mark 3-4 posts as "Featured" at a time. These show prominently on the homepage.

### 5. **Add Images When Possible**
Makes posts more attractive and professional. You can use:
- Court building photos
- Justice photos (if public domain)
- Related imagery

### 6. **Always Upload PDFs When Available**
Lawyers love reading original documents!

### 7. **Tags Help SEO**
Good tags: `bail, criminal law, supreme court, fundamental rights`

### 8. **Post Regularly**
Aim for 2-3 posts per week minimum to keep visitors engaged.

---

## 📱 MOBILE RESPONSIVE

This website is **100% mobile responsive**:
- ✅ Perfect on smartphones (all sizes)
- ✅ Great on tablets
- ✅ Excellent on desktops
- ✅ Navigation menu adapts to screen size
- ✅ Images resize properly
- ✅ Text is readable on all devices
- ✅ Admin panel works on mobile too!

Test it by resizing your browser or opening on your phone!

---

## 🔄 DAILY USAGE

### To Start the Website:
```cmd
cd C:\legal_insights
venv\Scripts\activate
python manage.py runserver
```

Keep the command prompt window open while using the website.

### To Stop:
Press `Ctrl + C` in the command prompt

### To Access:
- Public Site: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin-login/

---

## 🎨 DESIGN INSPIRED BY LIVE LAW

This website design is **inspired by Live Law** with:
- ✅ Professional news portal layout
- ✅ Red and white color scheme
- ✅ Featured stories section
- ✅ Latest news sections
- ✅ Sidebar with categories
- ✅ Clean, readable typography
- ✅ Professional article pages
- ✅ Responsive mobile design

**BUT** it's your own unique website, not a copy!

---

## ⚠️ IMPORTANT NOTES

### 1. **Python 3.13 Compatible**
This version is tested and works with Python 3.13 (and 3.8+).
No password validation errors!

### 2. **Keep Terminal Open**
The command prompt window must stay open while the website is running.

### 3. **Backup Regularly**
Backup the `db.sqlite3` file weekly to save your data.

### 4. **Remember Admin Password**
Write it down in a safe place!

### 5. **PDF File Sizes**
Keep PDFs under 10MB for faster loading.

### 6. **Image Sizes**
Recommended: 1200x600 pixels for featured images.

---

## 📊 WHAT'S INCLUDED

```
legal_insights/
├── manage.py                  # Django management
├── WINDOWS_SETUP.bat         # Auto setup script
├── README.md                 # This file
├── requirements.txt          # Python packages
├── legal_insights/           # Main project
│   ├── settings.py          # Configuration
│   ├── urls.py              # URL routing
│   └── wsgi.py              # Server config
├── news/                     # Main app
│   ├── models.py            # Database models
│   ├── views.py             # View logic
│   ├── forms.py             # Admin forms
│   ├── urls.py              # App URLs
│   ├── admin.py             # Django admin
│   └── templates/           # All HTML pages
└── media/                    # Uploaded files
    ├── judgments/
    │   ├── pdfs/
    │   └── images/
    └── laws/
        ├── pdfs/
        └── images/
```

---

## 🆘 TROUBLESHOOTING

### Error: "python not recognized"
**Fix**: Install Python from python.org and check "Add to PATH" during installation.

### Error: "Django not installed"
**Fix**: Run `pip install Django==4.2.11 Pillow==10.2.0`

### Can't Login
**Fix**: Create superuser again: `python manage.py createsuperuser`

### Port Already in Use
**Fix**: Use different port: `python manage.py runserver 8001`

### Images Not Showing
**Fix**: Make sure media folders exist and restart server.

---

## 🎓 FOR YOUR DAD

**Remember:**
1. ✍️ Write like you're writing for a newspaper
2. 📸 Add images when possible
3. 📄 Upload PDFs when available
4. 🏷️ Use good tags for SEO
5. ⭐ Mark only important posts as Featured
6. 📅 Post regularly (2-3 times per week)
7. 📱 Check on mobile too!

**This is YOUR legal news portal!**
Post judgment analysis, new law updates, legal commentary - just like Live Law does!

---

## 📞 SUPPORT

For any issues, check:
1. This README file
2. Django documentation: https://docs.djangoproject.com/
3. Bootstrap documentation: https://getbootstrap.com/

---

**🎉 You're Ready to Launch Your Legal News Website!**

**Technology**: Django 4.2 | Bootstrap 5 | Mobile Responsive
**Compatible**: Python 3.8 - 3.13
**Platform**: Windows 10/11
**Style**: Live Law Inspired Professional Design

**Made Simple & Professional! 🏛️**
