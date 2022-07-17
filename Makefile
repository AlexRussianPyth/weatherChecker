run:
	python3 script.py

req:
	pip3 install -r requirements.txt

# Docker
compose:
	docker-compose up --build