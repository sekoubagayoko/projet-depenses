#!/usr/bin/env bash
# Script de construction pour Render

echo "🚀 Installation des dépendances..."
pip install -r requirements.txt

echo "📦 Collecte des fichiers statiques..."
python manage.py collectstatic --noinput

echo "🔄 Application des migrations..."
python manage.py migrate

echo "✅ Build terminé avec succès !"