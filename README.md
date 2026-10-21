efile-efile/
├── app/
│   ├── __init__.py
│   ├── main.py             # The entry point of the FastAPI application
│   ├── dependencies.py
│   ├── routers/            # Handles API endpoints
│   │   ├── __init__.py
│   │   ├── admins.py
│   ├── core/               # Holds configurations and security settings
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   ├── models/             # Defines SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── admin.py
│   ├── schemas/            # Pydantic models for data validation
│   │   ├── __init__.py
│   │   ├── admin.py
│   ├── services/           # Contains business logic separate from API routes
│   │   ├── __init__.py
│   │   ├── admin_service.py
│   └── db/                 # Database configuartion
│       ├── __init__.py
│       ├── database.py
│       └── migrations/
├── tests/                  # Includes unit and integration tests
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_admin.py
├── .env
├── .gitignore
├── requirements.txt        # The purpose of the file is that so anyone can reproduce the environment with
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

## Run the dev server
```bash
python3 -m uvicorn app.main:app --reload
```
Run this in your browser http://127.0.0.1:8000 


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

## Tables
<pre>admin </pre>
<hr/>
<p>adminId </p>
<p>adminUsername </p>
<p>adminName </p>
<p>adminContactNo </p>
<p>adminPosition </p>
<p>adminUnit </p>
<p>adminPassword </p>

<pre>staff </pre>
<hr/>
<p>staffId (int)</p>
<p>staffUsername (string 255)</p>
<p>staffName (string 100)</p>
<p>staffContactNo (string 15)</p>
<p>staffUnit (string 50)</p>
<p>staffPassword (string 30)</p>

<pre>category </pre>
<hr/>
<p>categoryID (string 30)</p>
<p>categoryName (string 50)</p>

<pre>sub_category </pre>
<hr/>
<p>subid (int)</p>
<p>subName (string 100)</p>
<p>categoryID (string 30)</p>

<pre>cabinet </pre>
<hr/>
<p>cabinetid (int)</p>
<p>cabinetNo (string 30)</p>
<p>cabinetDesc (string 50)</p>
<p>categoryID (string 30)</p>
<p>subid (int)</p>

<pre>level </pre>
<hr/>
<p>levelid (int)</p>
<p>levelNo (int)</p>
<p>levelDesc (string 50)</p>
<p>categoryID (string 30)</p>
<p>cabinetid (int)</p>
<p>subid (int)</p>

<pre>file </pre>
<hr/>
<p>fileNo (string 30)</p>
<p>fileName (string 100)</p>
<p>fileDateIn (date)</p>
<p>categoryID (string 30)</p>
<p>cabinetid (int)</p>
<p>levelid (int)</p>
<p>subid (int)</p>
<p>fileStatus (string 30)</p>
<p>fileStat (string 30)</p>

<pre>transaction </pre>
<hr/>
<p>transID (int)</p>
<p>staffIC (string 12) </p>
<p>categoryID (string 30) </p>
<p>cabinetid (int) </p>
<p>levelid (int) </p>
<p>fileNo (string 30) </p>
<p>fileDateTaken (date) </p>
<p>fileDateReturn (date) </p>
<p>fileTransStatus (string 30)	</p>
<p>subid (int)</p>