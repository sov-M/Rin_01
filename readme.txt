py.exe -m venv venv
.\venv\Scripts\activate
pip install -r .\requirements.txt
py.exe .\manage.py makemigrations 
py.exe .\manage.py migrate   
py.exe .\manage.py runserver   