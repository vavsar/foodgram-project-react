from django.contrib.auth import get_user_model
from rest_framework import viewsets

User = get_user_model()


class TagModelViewSet(viewsets.ModelViewSet):
    pass


class IngredientModelViewSet(viewsets.ModelViewSet):
    pass


class RecipeModelViewSet(viewsets.ModelViewSet):
    pass



