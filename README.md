# Django ORM

### init after clone
```
python -m venv venv
.\venv\Scripts\activate
pip install pip-tools
pip-sync.exe (to install neccesary dependencies)
```

### start & common commands
```
python .\manage.py runserver
```

### on new dependencies
```
add it in file: requirements.in
pip-compile.exe (generate new file: requirements.txt)
```

### before commit
```
ruff format
pylint $(git ls-files '*.py')
