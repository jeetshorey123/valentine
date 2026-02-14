# Instructions to set up your Valentine's Day Website

## 1. Installation

Install Python dependencies:
```bash
pip install -r requirements.txt
```

## 2. Supabase Setup

### A. Create a Supabase Project
1. Go to https://supabase.com
2. Create a new project
3. Wait for the project to be set up

### B. Create the Database Table
1. Go to the SQL Editor in your Supabase dashboard
2. Run the SQL code from `database_schema.sql`

### C. Get Your Credentials
1. Go to Project Settings > API
2. Copy your Project URL
3. Copy your anon/public key

## 3. Environment Configuration

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your Supabase credentials:
   - Replace `your-supabase-project-url` with your actual Supabase URL
   - Replace `your-supabase-anon-key` with your actual Supabase anon key
   - Replace `your-secret-key-here-change-this-to-random-string` with a random secret key

## 4. Running the Application

```bash
python app.py
```

The application will be available at: http://localhost:5000

## Features

- **Page 1**: Name input
- **Page 2**: "Will you be my valentine?" with Yes/No buttons
  - The "No" button moves away when you try to click it!
  - Only "Yes" can be selected
- **Page 3**: Review/message input
- **Page 4**: Thank you confirmation

All responses are saved to Supabase database!

## Project Structure

```
valentine/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (create from .env.example)
├── .env.example          # Environment variables template
├── database_schema.sql   # SQL schema for Supabase
├── templates/
│   ├── index.html        # Name input page
│   ├── valentine.html    # Valentine question page
│   ├── review.html       # Review input page
│   └── thank_you.html    # Confirmation page
└── static/
    └── style.css         # Styling
```

## Notes

- Make sure to keep your `.env` file secure and never commit it to version control
- The `.gitignore` file is included to prevent accidental commits of sensitive data
