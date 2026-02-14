from flask import Flask, render_template, request, redirect, url_for, session
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'valentine-secret-key-2026')

# Database connection function
def get_db_connection():
    """Create a database connection to Neon PostgreSQL"""
    try:
        database_url = os.getenv('DATABASE_URL')
        if not database_url:
            print("❌ DATABASE_URL environment variable missing")
            return None
        
        conn = psycopg2.connect(database_url)
        return conn
    except Exception as e:
        print(f"❌ Database connection error: {e}")
        return None


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
    """Handle Yes/No response and save to database immediately"""
    answer = request.form.get('answer')
    name = session.get('name')
    
    if not name or answer != 'yes':
        return redirect(url_for('index'))
    
    session['answer'] = answer
    saved = False
    error_msg = None
    
    # Save to Neon PostgreSQL immediately when Yes is clicked
    try:
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute(
                "INSERT INTO valentines (name, response, review) VALUES (%s, %s, %s) RETURNING id",
                (name, answer, '')
            )
            result = cursor.fetchone()
            conn.commit()
            
            if result:
                session['record_id'] = result['id']
                saved = True
            
            cursor.close()
            conn.close()
        else:
            error_msg = "Database not connected"
    except Exception as e:
        print(f"Error saving to database: {e}")
        error_msg = str(e)
    
    return render_template('review.html', name=name, saved=saved, error_msg=error_msg)


@app.route('/submit', methods=['POST'])
def submit():
    """Update review in database"""
    review = request.form.get('review', '')
    name = session.get('name')
    answer = session.get('answer')
    record_id = session.get('record_id')
    
    if not name or not answer:
        return redirect(url_for('index'))
    
    # Update the review in existing database record
    updated = False
    error_msg = None
    
    try:
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            
            if record_id:
                # Update existing record
                cursor.execute(
                    "UPDATE valentines SET review = %s WHERE id = %s",
                    (review, record_id)
                )
            else:
                # Fallback: insert if record_id missing
                cursor.execute(
                    "INSERT INTO valentines (name, response, review) VALUES (%s, %s, %s)",
                    (name, answer, review)
                )
            
            conn.commit()
            updated = True
            cursor.close()
            conn.close()
    except Exception as e:
        print(f"Error updating database: {e}")
        error_msg = str(e)
    
    return render_template('thank_you.html', name=name, updated=updated, error_msg=error_msg)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
