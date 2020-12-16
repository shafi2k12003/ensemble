from rest_framework import status
from django.http import JsonResponse


# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.views import APIView, Response
from .models import gene_autocomplete
from .serializers import gene_autocompleteSerializer


@api_view(['GET'])
def genesView(request):

    if request.method == 'GET':
        lookup = request.GET.get('lookup')
        species = request.GET.get('species')
        if lookup is None:
            return Response('lookup parameter is mandatory', status=status.HTTP_400_BAD_REQUEST)
        else:
            if len(lookup) < 3:
                return Response('lookup should be 3 or more chars long', status=status.HTTP_400_BAD_REQUEST)
            else:
                gene_autocompletes=gene_autocomplete.objects.filter(display_label__startswith=lookup)
                if species is not None:
                    gene_autocompletes = gene_autocompletes.filter(species__startswith=species)
                gene_autocomplete_serializer = gene_autocompleteSerializer(gene_autocompletes, many=True)
                return JsonResponse(gene_autocomplete_serializer.data, safe=False)
    if request.method in ('POST', 'PUT', 'PATCH)'):
        return status.HTTP_405_METHOD_NOT_ALLOWED