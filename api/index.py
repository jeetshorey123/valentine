from flask import Flask, render_template, request, redirect, url_for, session
import os

# Import supabase
try:
    from supabase import create_client, Client
    SUPABASE_AVAILABLE = True
except ImportError:
    SUPABASE_AVAILABLE = False

# Initialize Flask app - MUST be at module level for Vercel
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'valentine-secret-key-2026')

# Supabase configuration
supabase_url = os.environ.get('SUPABASE_URL')
supabase_key = os.environ.get('SUPABASE_KEY')

# Only create supabase client if credentials are provided
if SUPABASE_AVAILABLE and supabase_url and supabase_key:
    try:
        supabase: Client = create_client(supabase_url, supabase_key)
    except Exception as e:
        print(f"Supabase initialization error: {e}")
        supabase = None
else:
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
    """Handle Yes/No response"""
    answer = request.form.get('answer')
    name = session.get('name')
    
    if not name or answer != 'yes':
        return redirect(url_for('index'))
    
    session['answer'] = answer
    return render_template('review.html', name=name)


@app.route('/submit', methods=['POST'])
def submit():
    """Submit review and save to Supabase"""
    review = request.form.get('review', '')
    name = session.get('name')
    answer = session.get('answer')
    
    if not name or not answer:
        return redirect(url_for('index'))
    
    # Save to Supabase
    try:
        if supabase:
            data = {
                'name': name,
                'response': answer,
                'review': review
            }
            result = supabase.table('valentines').insert(data).execute()
        return render_template('thank_you.html', name=name)
    except Exception as e:
        print(f"Error saving to database: {e}")
        return render_template('thank_you.html', name=name, error=True)


@app.route('/api/health')
def health():
    """Health check endpoint for Vercel"""
    return {'status': 'ok', 'message': 'Valentine app is running'}


# No app.run() needed - Vercel handles this


