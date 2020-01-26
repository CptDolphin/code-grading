### Export env variables
```
export FLASK_APP=project/__init__.py
export FLASK_ENV=development
```

### To run first tests
```
python3.6 -m venv env
source env/bin/activate
pip install flask==1.0.2
python manage.py run
```

### Test working in the browser
```
http://localhost:5000/users/ping
```

