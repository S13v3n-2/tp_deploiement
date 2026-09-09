from flask import Flask, jsonify
from healthcheck import HealthCheck, EnvironmentDump

app = Flask(__name__)

health = HealthCheck()
envdump = EnvironmentDump()
@app.route("/")
def home():
    return "Hello depuis Python + Nginx + Docker Compose !"

@app.route("/healthcheck")
def app_available():
    # Puisqu'il n'y a pas de dépendance externe (pas de Redis/SQL),
    # si Flask arrive à exécuter cette fonction, l'application est considérée comme saine.
    return jsonify({"status": "healthy", "message": "Flask application is running"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)