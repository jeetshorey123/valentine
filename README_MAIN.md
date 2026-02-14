# Valentine's Day Website 💕

A beautiful, interactive Valentine's Day website built with Flask and Supabase.

## ✨ Features

- 💖 Beautiful pink gradient Valentine's theme
- 🎯 Interactive "Will you be my Valentine?" question
- 🏃 Moving "No" button that runs away (impossible to click!)
- 💌 Review/message collection
- 🗄️ Data storage in Supabase
- 🚀 Vercel deployment ready
- 📱 Fully responsive design

## 🚀 Quick Start (Local Development)

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

Create a `.env` file (copy from `.env.example`):

```env
SECRET_KEY=your-secret-key
SUPABASE_URL=your-supabase-url
SUPABASE_KEY=your-supabase-anon-key
```

### 3. Set Up Supabase Database

⚠️ **CRITICAL:** Run the SQL from `fix_supabase.sql` in your Supabase SQL Editor first!

1. Go to your Supabase project SQL Editor
2. Copy all content from `fix_supabase.sql`
3. Paste and run
4. Verify the `valentines` table is created with correct policies

### 4. Run the Application

```bash
python app.py
```

Visit: http://localhost:5000

## 🌐 Deploy to Vercel

See detailed instructions in `DEPLOY_INSTRUCTIONS.md`

**Quick steps:**

1. **Fix Supabase first** (run `fix_supabase.sql`)
2. Push code to GitHub
3. Import to Vercel
4. Add environment variables in Vercel dashboard
5. Deploy!

## 🗄️ Database Schema

```sql
CREATE TABLE valentines (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    response TEXT NOT NULL,
    review TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

## 📁 Project Structure

```
valentine/
├── app.py                 # Local Flask app
├── api/
│   └── index.py          # Vercel entry point
├── templates/             # HTML templates
├── static/               # CSS and assets
├── requirements.txt      # Dependencies
├── vercel.json          # Vercel config
└── fix_supabase.sql     # Database setup
```

## 🎨 Pages

1. **/** - Name input page
2. **/valentine** - "Will you be my Valentine?" with interactive buttons
3. **/review** - Message/review input
4. **/submit** - Saves to Supabase and shows thank you

## 🔧 Technologies

- **Backend:** Flask (Python)
- **Database:** Supabase (PostgreSQL)
- **Deployment:** Vercel
- **Frontend:** HTML, CSS, Vanilla JavaScript

## 💝 Made with Love

Created by Jeet for Valentine's Day 2026

## 📝 License

Free to use for personal Valentine's Day purposes! 💕
