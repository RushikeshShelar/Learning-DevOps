from flask import Flask
import mysql.connector
import os


app = Flask(__name__)

@app.route('/')
def home():
    return "Flask Running with MySQL! in Docker using Docker Compose"

def connect_db():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'db'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE') 
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server version", db_info)
            return f"✅ Connected to MySQL Server version {db_info}"
    except mysql.connector.Error as err:
        print("Error while connecting to MySQL", err)
        return f"❌ Error: {err}"
        
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

@app.route('/db')
def db_status():
    return connect_db()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    connect_db()
    print("Flask app is running on port 5000")