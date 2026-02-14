from flask import Flask, render_template, request, redirect, url_for, session
import os
from pathlib import Path

# Get the base directory (parent of 'api' folder)
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize Flask app - MUST be at module level for Vercel
app = Flask(__name__,
            template_folder=str(BASE_DIR / 'templates'),
            static_folder=str(BASE_DIR / 'static'))
app.secret_key = os.environ.get('SECRET_KEY', 'valentine-secret-key-2026')

# Import and initialize Supabase
try:
    from supabase import create_client, Client
    supabase_url = os.environ.get('SUPABASE_URL')
    supabase_key = os.environ.get('SUPABASE_KEY')
    
    if supabase_url and supabase_key:
        supabase = create_client(supabase_url, supabase_key)
    else:
        supabase = None
except Exception as e:
    print(f"Supabase error: {e}")
    supabase = None


@app.route('/')
def index():
    """First page - ask for name"""
    session.clear()
    return render_template('index.html')


@app.route('/valentine', methods=['POST'])
def valentine():
    """Second page - Will you be my valentine?"""
    name = request.form.get('name')
    if not name:
        return redirect(url_for('index'))
    
    session['name'] = name
    return render_template('valentine.html', name=name)


@app.route('/response', methods=['POST'])
def response():
    """Handle Yes/No response and save to Supabase immediately"""
    answer = request.form.get('answer')
    name = session.get('name')
    
    if not name or answer != 'yes':
        return redirect(url_for('index'))
    
    session['answer'] = answer
    saved = False
    error_msg = None
    
    # Save to Supabase immediately when Yes is clicked
    try:
        if supabase:
            data = {
                'name': name,
                'response': answer,
                'review': ''  # Empty review for now
            }
            result = supabase.table('valentines').insert(data).execute()
            if result.data and len(result.data) > 0:
                session['record_id'] = result.data[0]['id']
                saved = True
        else:
            error_msg = "Database not connected"
    except Exception as e:
        print(f"Error saving to database: {e}")
        error_msg = str(e)
    
    return render_template('review.html', name=name, saved=saved, error_msg=error_msg)


@app.route('/submit', methods=['POST'])
def submit():
    """Update review in Supabase"""
    review = request.form.get('review', '')
    name = session.get('name')
    answer = session.get('answer')
    record_id = session.get('record_id')
    
    if not name or not answer:
        return redirect(url_for('index'))
    
    # Update the review in existing Supabase record
    updated = False
    error_msg = None
    
    try:
        if supabase and record_id:
            result = supabase.table('valentines').update({'review': review}).eq('id', record_id).execute()
            updated = True
        elif supabase and not record_id:
            # Fallback: insert if record_id missing
            data = {
                'name': name,
                'response': answer,
                'review': review
            }
            result = supabase.table('valentines').insert(data).execute()
            updated = True
    except Exception as e:
        print(f"Error updating database: {e}")
        error_msg = str(e)
    
    return render_template('thank_you.html', name=name, updated=updated, error_msg=error_msg)


@app.route('/api/health')
def health():
    """Health check endpoint"""
    return {'status': 'ok', 'message': 'Valentine app is running'}
