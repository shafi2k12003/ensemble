from django.db import models

# Create your models here.
class gene_autocomplete(models.Model):
    species = models.CharField(max_length=255, blank=False, null=False)
    stable_id = models.CharField(max_length=128, blank=False, null=False)
    display_label = models.CharField(max_length=128, blank=False, null=False)
    location = models.CharField(max_length=60, blank=False, null=False)
    db = models.CharField(primary_key=True, unique=False, default=None, blank=True, null=False, max_length=32, db_column='db')

    class Meta:
        db_table = "gene_autocomplete"