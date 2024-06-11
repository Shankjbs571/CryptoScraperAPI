from celery import shared_task
from .models import Job, Task
from .coinmarketcap import CoinMarketCap
import time 

@shared_task
def scrape_coin_data(job_id, coin):
    job = Job.objects.get(job_id=job_id)
    task = Task.objects.create(job=job, coin=coin)
    try:

        scraper = CoinMarketCap(coin)
        data = scraper.scrape_data()
        task.data = data
        task.status = 'completed'

    except Exception as e:
        task.status = 'failed'
    task.save()
    return data
    

@shared_task
def add(x,y):
    return x+y
