FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# Copier le reste des fichiers dans le conteneur
COPY . /app

# Exposer le port 8000
EXPOSE 8000

# Démarrer l'application Flask
CMD ["python", "app.py"]


