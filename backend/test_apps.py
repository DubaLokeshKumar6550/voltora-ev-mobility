import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'voltora_backend.settings')
from django.conf import settings

print("Testing loading apps one by one...", flush=True)
for app in settings.INSTALLED_APPS:
    print(f"Loading {app}...", flush=True)
    try:
        from django.apps.config import AppConfig
        cfg = AppConfig.create(app)
        print(f"  -> Created config: {cfg.name}", flush=True)
    except Exception as e:
        print(f"  -> Error on {app}: {e}", flush=True)
print("All app configs created without hanging!", flush=True)
