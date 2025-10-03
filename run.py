from waitress import serve
from app import app  # replace 'app' with your Flask app object

serve(app, host='0.0.0.0', port=8080)
