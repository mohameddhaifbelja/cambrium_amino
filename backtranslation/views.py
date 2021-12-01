from django.http import JsonResponse
import json
import numpy as np
from . import models
# Create your views here.

def index(request):
    """
    List all code snippets, or create a new snippet.
    """
    # Read the json file containing the cumulative probablities of each amino acid
    Amino = models.Amino()
    if request.method == 'GET':
        
        token = request.GET.get('sequence')
        state, result = Amino.backtranslate(token)

        if state:
            return JsonResponse({"response":result,'status':200},safe=False)
        else:
             return JsonResponse({"error":result, 'status':404},safe=False,status=404)
        