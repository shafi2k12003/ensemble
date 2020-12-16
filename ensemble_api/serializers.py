from rest_framework import serializers
from ensemble_api.models import gene_autocomplete


class gene_autocompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = gene_autocomplete
        fields = ('display_label',
                  'location',
                  'stable_id',
                  'species',
                  )