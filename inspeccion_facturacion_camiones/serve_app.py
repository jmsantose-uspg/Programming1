from app import app, init_db
from waitress import serve


if __name__ == "__main__":
    with app.app_context():
        init_db()
    serve(app, host="0.0.0.0", port=5000, threads=8)
