mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

clean:
	flake8 .
	isort .