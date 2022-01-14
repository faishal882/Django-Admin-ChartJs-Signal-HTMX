from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

User = get_user_model()


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {})


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10
    }

    return JsonResponse(data)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ['January',
                  'February',
                  'March',
                  'April',
                  'May',
                  'June',
                  'July'
                  ]
        default_items = [qs_count, 23, 13, 32, 12, 34, 21]
        default_items2 = [qs_count, 20, 10, 30, 20, 40, 2]
        data = {
            "labels": labels,
            "default": default_items,
            'default2': default_items2
        }
        return Response(data)
