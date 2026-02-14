# 🚨 IMPORTANT: Fix Supabase Database Error

## Your website is getting this error:
**"Error saving to database: new row violates row-level security policy"**

## ✅ Quick Fix (5 minutes):

### Step 1: Open Supabase SQL Editor
Click this link: **https://supabase.com/dashboard/project/cjkbjehzblbgyehndkmy/sql/new**

### Step 2: Copy & Run This SQL

Open the file `fix_supabase.sql` and copy ALL the code (or copy below):

```sql
-- COMPLETE SUPABASE SETUP
DROP TABLE IF EXISTS valentines CASCADE;

CREATE TABLE valentines (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    response TEXT NOT NULL,
    review TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_valentines_created_at ON valentines(created_at DESC);
CREATE INDEX idx_valentines_name ON valentines(name);

ALTER TABLE valentines ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Allow anyone to insert"
ON valentines
FOR INSERT
TO public
WITH CHECK (true);

CREATE POLICY "Allow anyone to select"
ON valentines
FOR SELECT
TO public
USING (true);
```

### Step 3: Click "RUN" or Press Ctrl+Enter

You should see: ✅ Success. No errors

### Step 4: Test Your Website

1. Go to http://localhost:5000
2. Enter a name
3. Click "Yes" 
4. Leave a review
5. Submit

It should now say: ✨ **All Set!** ✨ (instead of error)

---

## 📊 View Your Data in Supabase

After someone submits, you can view the data:

1. Go to: https://supabase.com/dashboard/project/cjkbjehzblbgyehndkmy/editor
2. Click on the `valentines` table
3. See all submissions!

---

## ✅ What's Been Set Up:

- ✅ Beautiful pink Valentine's UI
- ✅ Moving "No" button (can't be clicked!)
- ✅ Supabase connection configured
- ✅ Environment variables (.env file)
- ✅ "Made by Jeet" footer on all pages
- ✅ Enhanced button styling
- ⏳ **Just need to run the SQL above!**

---

If you still get errors after running the SQL, let me know!
