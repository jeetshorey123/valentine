# 🚀 Deployment Instructions

## 🔴 CRITICAL: Fix Supabase First!

### Your website shows: ⚠️ "Error saving your response"

**This is because Supabase Row Level Security (RLS) is blocking data inserts.**

### ✅ IMMEDIATE FIX (2 minutes):

1. **Open Supabase SQL Editor:**
   👉 https://supabase.com/dashboard/project/cjkbjehzblbgyehndkmy/sql/new

2. **Copy ALL code from `fix_supabase.sql`** (entire file)

3. **Paste into SQL Editor and click RUN** (or Ctrl+Enter)

4. **Wait for**: ✅ Success messages

5. **Test locally**: 
   - Go to http://localhost:5000
   - Enter name → Click Yes → Write review → Submit
   - Should see: ✨ **All Set!** ✨ (NOT error)

---

## 📊 Verify Data is Saving

After fixing, check if data is being saved:

1. Go to: https://supabase.com/dashboard/project/cjkbjehzblbgyehndkmy/editor
2. Click the `valentines` table
3. You should see entries with names and reviews!

---

## 🌐 Deploy to Vercel (After Supabase is Fixed)

### Prerequisites
- GitHub account
- Vercel account (free at vercel.com)

### Steps:

#### 1. Create GitHub Repository
```bash
cd C:\Users\91983\OneDrive\Desktop\valentine
git init
git add .
git commit -m "Initial commit - Valentine's Day website"
```

Create a new repo on GitHub, then:
```bash
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

#### 2. Deploy to Vercel

1. Go to: https://vercel.com/new
2. Click "Import Git Repository"
3. Select your valentine repository
4. **Framework Preset:** Select "Other"
5. **Add Environment Variables:**
   - Click "Environment Variables"
   - Add these three variables:
   
   | Name | Value |
   |------|-------|
   | `SECRET_KEY` | `valentine-secret-key-2026` |
   | `SUPABASE_URL` | `https://cjkbjehzblbgyehndkmy.supabase.co` |
   | `SUPABASE_KEY` | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNqa2JqZWh6YmxiZ3llaG5ka215Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEwMTU5NTMsImV4cCI6MjA4NjU5MTk1M30.v-1YSbPXn9PdQuR0wDP0s9AJuIBcGSKF79XtSsb8jqE` |

6. Click **Deploy**

7. Wait 1-2 minutes for deployment to complete

8. Your site will be live at: `https://your-project-name.vercel.app`

9. **Test your live site** - make sure data saves to Supabase!

#### 3. Custom Domain (Optional)

In Vercel dashboard:
1. Go to your project settings
2. Click "Domains"
3. Add your custom domain
4. Follow DNS configuration instructions

---

## 🐛 Troubleshooting

### Still getting "Error saving" message?

**Check Supabase Policies:**
```sql
-- Run this in Supabase SQL Editor to verify policies:
SELECT * FROM pg_policies WHERE tablename = 'valentines';
```

You should see:
- `anon_insert_policy`
- `anon_select_policy`

If not, run `fix_supabase.sql` again!

### Test Supabase connection:
```python
# Run this in your terminal to test:
python -c "from supabase import create_client; client = create_client('https://cjkbjehzblbgyehndkmy.supabase.co', 'YOUR_KEY'); print(client.table('valentines').select('*').execute())"
```

---

## 📁 Project Structure

```
valentine/
├── app.py                      # Main Flask app (for local dev)
├── api/
│   ├── __init__.py            # Python package marker
│   └── index.py               # Vercel serverless entry point
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Python version for Vercel
├── vercel.json                 # Vercel configuration
├── .env                        # Local environment variables (DO NOT COMMIT)
├── .env.example                # Template for environment variables
├── .gitignore                  # Files to ignore in git
├── fix_supabase.sql           # 🔴 RUN THIS FIRST!
├── database_schema.sql         # Original schema
├── templates/                  # HTML templates
│   ├── index.html
│   ├── valentine.html
│   ├── review.html
│   └── thank_you.html
└── static/
    └── style.css               # Styling

```

---

## ✅ Checklist

- [ ] Run `fix_supabase.sql` in Supabase
- [ ] Test locally - confirm no errors
- [ ] Verify data appears in Supabase table
- [ ] Create GitHub repo
- [ ] Push code to GitHub
- [ ] Deploy to Vercel with environment variables
- [ ] Test live site
- [ ] Share your Valentine's website! 💕

---

Made with 💖 by Jeet
