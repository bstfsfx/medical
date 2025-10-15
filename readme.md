# Django Clinic Project

## Steps to build the project

### 1. Create virtual environment

```bash
mkvirtualenv medical
```

### 2. create project folder

```bash
django-admin startproject
```

### 3. run the server

```py
For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()

```
