import os
import sys

print("Step 1: Setting up environment...", flush=True)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'voltora_backend.settings')

try:
    import django
    print("Step 2: Calling django.setup()...", flush=True)
    django.setup()
    print("Step 3: Django initialized successfully!", flush=True)
    
    from django.core.management import call_command
    print("Step 4: Running makemigrations users...", flush=True)
    call_command('makemigrations', 'users', interactive=False)
    print("Step 5: Running migrate...", flush=True)
    call_command('migrate', interactive=False)
    print("Step 6: Migrations completed successfully!", flush=True)
except Exception as e:
    import traceback
    print("ERROR OCCURRED:", e, flush=True)
    traceback.print_exc()
