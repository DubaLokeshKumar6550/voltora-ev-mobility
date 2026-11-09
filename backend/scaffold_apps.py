import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APPS_DIR = os.path.join(BASE_DIR, 'apps')

apps_list = [
    'users',
    'bikes',
    'rentals',
    'marketplace',
    'payments',
    'reviews',
    'notifications',
    'locations',
    'wishlist',
    'subscriptions',
    'support'
]

for app in apps_list:
    app_dir = os.path.join(APPS_DIR, app)
    os.makedirs(app_dir, exist_ok=True)
    os.makedirs(os.path.join(app_dir, 'migrations'), exist_ok=True)
    
    # migrations/__init__.py
    with open(os.path.join(app_dir, 'migrations', '__init__.py'), 'w') as f:
        pass
        
    # __init__.py
    init_path = os.path.join(app_dir, '__init__.py')
    if not os.path.exists(init_path):
        with open(init_path, 'w') as f:
            pass
            
    # apps.py
    pascal_name = "".join(word.capitalize() for word in app.split('_'))
    apps_content = f"""from django.apps import AppConfig

class {pascal_name}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.{app}'
    verbose_name = '{app.replace('_', ' ').capitalize()}'
"""
    with open(os.path.join(app_dir, 'apps.py'), 'w') as f:
        f.write(apps_content)
        
    # models.py
    models_path = os.path.join(app_dir, 'models.py')
    if not os.path.exists(models_path):
        with open(models_path, 'w') as f:
            f.write("from django.db import models\n")
            
    # admin.py
    admin_path = os.path.join(app_dir, 'admin.py')
    if not os.path.exists(admin_path):
        with open(admin_path, 'w') as f:
            f.write("from django.contrib import admin\n")
            
    # views.py
    views_path = os.path.join(app_dir, 'views.py')
    if not os.path.exists(views_path):
        with open(views_path, 'w') as f:
            f.write("from rest_framework import viewsets, permissions\n")
            
    # serializers.py
    serializers_path = os.path.join(app_dir, 'serializers.py')
    if not os.path.exists(serializers_path):
        with open(serializers_path, 'w') as f:
            f.write("from rest_framework import serializers\n")

    # urls.py
    urls_path = os.path.join(app_dir, 'urls.py')
    if not os.path.exists(urls_path):
        with open(urls_path, 'w') as f:
            f.write("from django.urls import path\n\nurlpatterns = []\n")

print("All apps successfully scaffolded!")
