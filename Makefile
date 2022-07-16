run:
	python3 main.py

fastapi:
	python3 api/main.py

req:
	pip3 install -r requirements.txt

# Docker
compose:
	docker-compose up --build