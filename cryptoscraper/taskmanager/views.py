from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job, Task
from .coinmarketcap import CoinMarketCap
from .tasks import scrape_coin_data

class StartScraping(APIView):
    def post(self, request):
        print("inside post")
        coins = request.data.get('coins', [])
        # Validate input
        if not all(isinstance(coin, str) for coin in coins):
            return Response({'error': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)
        
        # # Create a new job
        job = Job.objects.create()
        
        # # Submit tasks to Celery
        for coin in coins:
            scrape_coin_data.delay(job.job_id, coin)
        try:
            scraper = CoinMarketCap(coins[0])
            data = scraper.scrape_data()
            print(data)
            return Response({'status': 'Inside Try','data':data,'job_iddd': job.id}, status=status.HTTP_200_OK)
        


        except Exception as e:
            print(e)
            return Response({'error': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)


class ScrapingStatus(APIView):
    def get(self, request, job_id):
        job = Job.objects.get(id=job_id)
        tasks = Task.objects.filter(job=job)
        response_data = {
            'job_id': job.id,
            'tasks': [
                {'coin': task.coin, 'data': task.data} for task in tasks
            ]
        }
        return Response(response_data)
