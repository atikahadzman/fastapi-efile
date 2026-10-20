efile-efile/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── admins.py
│   ├── internal/
│   │   ├── __init__.py
│   │   └── admin.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── admin.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── admin.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── admin_service.py
│   └── db/
│       ├── __init__.py
│       ├── database.py
│       └── migrations/
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_admin.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── run.sh


## Reference 
<p> https://dev.to/blumenbluu/how-to-start-fastapi-jaf </p>

<p> https://dev.to/mohammad222pr/structuring-a-fastapi-project-best-practices-53l6 </p>


## Install
```bash
pip install sqlalchemy
```

```bash
pip install pymysql
```

```bash
pip install passlib[bcrypt]
```


## Issues
<p>1. Import "sqlalchemy" could not be resolvedPylancereportMissingImports</p>

```bash
pip install sqlalchemy
```

<p>if this error occur</p>
<p>error: externally-managed-environment</p>

try these steps

1. Install the full python package if you haven't already
```bash
sudo apt update && sudo apt install python3-full -y
```

2. Create a virtual environment named 'venv'
```bash
python3 -m venv venv
```

3. Activate the virtual environment
```bash
source venv/bin/activate
```

4. Now pip install will work flawlessly
```bash
pip install sqlalchemy
```

