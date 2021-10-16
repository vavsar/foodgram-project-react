from django.contrib import admin

from .models import (Favorites, Follow, Ingredient, IngredientInRecipe,
                     Purchase, Recipe, Tag)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('^name',)


class IngredientInRecipeAdmin(admin.TabularInline):
    model = IngredientInRecipe
    fk_name = 'recipe'


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'favorited')
    list_filter = ('author', 'name', 'tags')
    exclude = ('ingredients',)

    inlines = [
        IngredientInRecipeAdmin,
    ]

    def favorited(self, obj):
        favorited_count = Favorites.objects.filter(recipe=obj).count()
        return favorited_count

    favorited.short_description = 'В избранном'


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('author', 'user')


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Favorites, FavoriteAdmin)
admin.site.register(Follow, SubscriptionAdmin)
admin.site.register(IngredientInRecipe, RecipeIngredientAdmin)


# from django.contrib import admin
# from django.contrib.auth import get_user_model
#
# from .models import Tag, Ingredient, Recipe, Follow
#
# User = get_user_model()
#
#
# class TagAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'name',
#         'color',
#         'slug',
#     )
#
#
# class IngredientAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'name',
#         'measurement_unit',
#     )
#
#
# class RecipeAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'get_tags',
#         'author',
#         'get_ingredients',
#         'is_favorited',
#         'is_in_shopping_cart',
#         'name',
#         'image',
#         'text',
#         'cooking_time',
#         'pub_date',
#     )
#
#     def get_ingredients(self, obj):
#         return obj.ingredients.all()
#
#     def get_tags(self, obj):
#         return obj.tags.all()
#
#
#
# admin.site.register(Tag, TagAdmin)
# admin.site.register(Ingredient, IngredientAdmin)
# admin.site.register(Recipe, RecipeAdmin)
