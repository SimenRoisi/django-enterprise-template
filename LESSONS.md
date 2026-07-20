# Lessons Learned

## First API endpoint (Phase 3)

20-07-2026

Exposed `Organization` over HTTP using Django REST Framework.

API request flow:

```
GET /organizations/
  → config/urls.py
  → apps/organizations/urls.py
  → OrganizationListView.get()
  → Organization.objects.all()
  → OrganizationSerializer (many=True)
  → Response(JSON)
```

Steps:

- Added `rest_framework` to `INSTALLED_APPS` in `config/settings.py`
- Created `OrganizationSerializer` in `serializers.py` — a `ModelSerializer` that maps model fields to JSON
- Created `OrganizationListView` in `views.py` — an `APIView` with a `get()` method
- Created `apps/organizations/urls.py` and mounted it in `config/urls.py` via `include()`
- Tested with browser or curl: `http://127.0.0.1:8000/organizations/`

Key details:

- Class-based views (including DRF `APIView`) must use `.as_view()` in `urlpatterns` — passing the class directly causes `urls.E009`
- `ModelSerializer` auto-generates fields from the model; `many=True` serializes a queryset
- `manage.py shell` is for ORM queries, not HTTP requests — use browser or `curl` for API testing

Not yet: POST/create, auth, permissions, service layer.

## First model creation (Phase 2)
20-07-2026
Created `apps/organizations/`, foundation for the future multi-tenancy
Model → database flow:
Organization (models.py) → makemigrations → migrations/0001_initial.py → migrate → organizations_organization table in SQLite → ORM queries / admin UI

Steps:
- Defined `Organization` in `apps/organizations/models.py` (`name`, `slug`, `created_at`)
- Set `name = "apps.organizations"` in `apps.py`; registered `OrganizationsConfig` in `INSTALLED_APPS`
- Registered model in `admin.py` to create/list orgs at `/admin/`
- Ran `makemigrations organizations` then `migrate`
- Read `0001_initial.py` — Django generated `CreateModel` with our fields
- Created a sample org via `manage.py shell`:

  ```python
  from apps.organizations.models import Organization
  Organization.objects.create(name="Acme Corp", slug="acme")
  ```

Note: admin manages data; migrations + models define schema.

## First custom app and URL routing (phase 1)
20-07-2026
Created `apps/core/`, which contains platform-level app stuff like health checks
The following creates the necessary django files:
```bash
uv run python manage.py startapp core apps/core
```
Request flow for /health/:
Browser → config/urls.py → apps/core/urls.py → views.health_check → JsonResponse

- We created apps/core/urls.py and included the url for our /health endpoint
after creating the health_check view function with JsonResponse as {"status": "ok"}
- A new app needs its url endpoint defined in config/urls.py too,
we added path("", include("apps.core.urls")) for this, note that the path is set in /apps/core/urls.py

## Django project initialization
18-07-2026
A Django project is the configuration layer of the application.

It contains:

- settings
- URL routing
- deployment entry points

A Django app represents a business capability inside the project.