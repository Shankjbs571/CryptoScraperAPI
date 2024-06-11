# CryptoScraper

CryptoScraperAPI is a Django-based web application for scraping cryptocurrency data using Selenium. The project uses Celery for asynchronous task management and Docker for Redis.


## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/cryptoscraper.git
```
- Create a virtual env and install the dependencies specified in requirements.txt

### 2. RUN Redis Docker image

```bash
docker compose up
```

### 3. Start Celery worker 

```bash
celery -A cryptoscraper worker --pool=solo -l INFO
```

### 4. Now run the django server 

```bash
cd cryptoscraper
python manage.py runserver
```

### 5. Interact

open the link in browser and interact

## Django Admin Panel Screenshot
<img src="path_to_your_screenshot.png" alt="Screenshot" style="width: 50%;"/>


## Postman Screenshots
<img src="path_to_your_screenshot.png" alt="Screenshot" style="width: 50%;"/>

