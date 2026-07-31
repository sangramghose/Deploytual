.PHONY: help install test lint run-backend run-frontend docker-build docker-up clean

help: ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install backend dependencies
	cd backend && pip install -r requirements.txt

test: ## Run backend tests
	cd backend && pytest tests/ -v

lint: ## Lint backend code
	cd backend && flake8 . --count --max-line-length=120 --statistics

run-backend: ## Start the FastAPI server locally
	cd backend && uvicorn main:app --reload

run-frontend: ## Serve the frontend locally
	npx serve frontend

docker-build: ## Build the backend Docker image
	docker build -t deploytual-backend ./backend

docker-up: ## Start the full stack with Docker Compose
	docker-compose up --build

clean: ## Remove Python cache and uploaded files
	find . -type d -name __pycache__ -exec rm -rf {} +
	rm -rf backend/uploads/*
