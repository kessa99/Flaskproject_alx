from flask import Flask
from app import creation_app

app = creation_app()

if __name__ == '__main__':
    app.run(debug=True)