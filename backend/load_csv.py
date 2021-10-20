import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foodgram.settings")
django.setup()

import csv
from api.models import Ingredient

with open('ingredients.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Ingredient.objects.get_or_create(
            name=row[0],
            measurement_unit=row[1],
        )
