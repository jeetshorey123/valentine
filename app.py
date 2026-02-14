from flask import Flask, render_template, request, redirect, url_for, session
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')

# Supabase configuration
supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase: Client = create_client(supabase_url, supabase_key)


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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
