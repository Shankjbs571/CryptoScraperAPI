import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptoscraper.settings')

app = Celery('cryptoscraper')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
app.conf.update(
    broker_connection_retry_on_startup=True,
)

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')




# {
#   "job_id": "<UUID>",
#   "tasks": [
#     {
#       "coin": "DUKO",
#       "output": {
#         "price": 0.003913,
#         "price_change": -5.44,
#         "market_cap": 37814377,
#         "market_cap_rank": 740,
#         "volume": 4583151,
#         "volume_rank": 627,
#         "volume_change": 12.21,
#         "circulating_supply": 9663955990,
#         "total_supply": 9999609598,
#         "diluted_market_cap": 39127766,
#         "contracts": [
#           {
#             "name": "solana",
#             "address": "HLptm5e6rTgh4EKgDpYFrnRHbjpkMyVdEeREEa2G7rf9"
#           }
#         ],
#         "official_links": [
#           {
#             "name": "website",
#             "link": "https://dukocoin.com"
#           }
#         ],
#         "socials": [
#           {
#             "name": "twitter",
#             "url": "https://twitter.com/dukocoin"
#           },
#           {
#             "name": "telegram",
#             "url": "https://t.me/+jlScZmFrQ8g2MDg8"
#           }
#         ]
#       }
#     },
#     {
# 	"coin": "NOT" ,
#     "output": {
# 			…
# 		 }
#     },
#     {
# 	"coin": "GORILLA",
#     "output": {
# 			…
# 		 }
#     }
#   ]
# }
