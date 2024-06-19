from django.contrib import admin

# Register your models here.
from django.apps import apps
from django.contrib import admin

# Loop to register all models for now

app_models = apps.get_app_config('avantecore').get_models()
for model in app_models:
    try:

        admin.site.register(model)

    except Exception:
        pass
