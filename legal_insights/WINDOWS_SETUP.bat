@echo off
echo ======================================
echo LEGAL INSIGHTS - Windows Setup
echo ======================================
echo.

echo Step 1: Creating virtual environment...
python -m venv venv

echo Step 2: Activating virtual environment...
call venv\Scripts\activate.bat

echo Step 3: Installing Django and Pillow...
pip install Django==4.2.11 Pillow==10.2.0

echo Step 4: Creating database...
python manage.py makemigrations
python manage.py migrate

echo Step 5: Creating media directories...
mkdir media 2>nul
mkdir media\judgments 2>nul
mkdir media\judgments\pdfs 2>nul
mkdir media\judgments\images 2>nul
mkdir media\laws 2>nul
mkdir media\laws\pdfs 2>nul
mkdir media\laws\images 2>nul

echo.
echo ======================================
echo Setup Complete!
echo ======================================
echo.
echo NEXT STEPS:
echo 1. Run: python manage.py createsuperuser
echo 2. Run: python manage.py runserver
echo 3. Open: http://127.0.0.1:8000/
echo.
echo Admin Login: http://127.0.0.1:8000/admin-login/
echo ======================================
pause
