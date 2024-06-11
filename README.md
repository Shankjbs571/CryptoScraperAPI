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
<img src="https://github.com/Shankjbs571/CryptoScraperAPI/blob/main/assets/admin_panel_ss/Screenshot%20(55).png?raw=true" alt="Screenshot" />
<img src="https://github.com/Shankjbs571/CryptoScraperAPI/blob/main/assets/admin_panel_ss/Screenshot%20(57).png?raw=true" alt="Screenshot" />
<img src="https://github.com/Shankjbs571/CryptoScraperAPI/blob/main/assets/admin_panel_ss/Screenshot%20(59).png?raw=true" alt="Screenshot" />
<img src="https://github.com/Shankjbs571/CryptoScraperAPI/blob/main/assets/admin_panel_ss/Screenshot%20(60).png?raw=true" alt="Screenshot" />
<img src="https://github.com/Shankjbs571/CryptoScraperAPI/blob/main/assets/admin_panel_ss/Screenshot%20(61).png?raw=true" alt="Screenshot" />
<img src="https://github.com/Shankjbs571/CryptoScraperAPI/blob/main/assets/admin_panel_ss/Screenshot%20(62).png?raw=true" alt="Screenshot" />


## Postman Screenshots
<img src="https://github.com/Shankjbs571/CryptoScraperAPI/blob/main/assets/postman_ss/Screenshot%20(63).png?raw=true" alt="Screenshot" />
<img src="https://github.com/Shankjbs571/CryptoScraperAPI/blob/main/assets/postman_ss/Screenshot%20(64).png?raw=true" alt="Screenshot" />
<img src="https://github.com/Shankjbs571/CryptoScraperAPI/blob/main/assets/postman_ss/Screenshot%20(65).png?raw=true" alt="Screenshot" />

