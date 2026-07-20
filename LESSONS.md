# Lessons Learned

## First custom app and URL routing
20-07-2026
Created `apps/core/`, which contains platform-level app stuff like health checks
The following creates the necessary django files:
```bash
uv run python manage.py startapp core apps/core
```
Request flow for /health/:
Browser → config/urls.py → apps/core/urls.py → views.health_check → JsonResponse

- We created apps/core/urls.py and included the url for our /health endpoint
after creating the health_check view function with JsonResponse as "OK"
- A new app needs it's url endpoint defined in config/urls.py too,
we added path("", include("apps.core.urls")) for this, note that the path is set in /apps/core/urls.py

## Django project initialization
18-07-2026
A Django project is the configuration layer of the application.

It contains:

- settings
- URL routing
- deployment entry points

A Django app represents a business capability inside the project.