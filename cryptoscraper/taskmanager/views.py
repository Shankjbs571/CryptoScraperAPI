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
        
        # Validating input
        if not all(isinstance(coin, str) for coin in coins):
            return Response({'error': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)
        
        job = Job.objects.create()
        
        for coin in coins:
            scrape_coin_data.delay(job.job_id, coin)
        
        while job.status != 'completed':
            if all(t.status == 'completed' for t in job.task_set.all()):
                job.status = 'completed'
                job.save()
        
        return Response({'status': 'Inside Try','job_iddd': job.job_id}, status=status.HTTP_200_OK)

class ScrapingStatus(APIView):
    def get(self, request, job_id):
        job = Job.objects.get(job_id=job_id)
        tasks = Task.objects.filter(job=job)
        if job.status == 'completed':
            response_data = {
                'job_id': job.job_id,
                'tasks': [
                    {'coin': task.coin, 'output': task.data} for task in tasks
                ]
            }
        else:
            response_data = {
                'job_id': job.id,
                'status' : "pending",
            }

        return Response(response_data)
