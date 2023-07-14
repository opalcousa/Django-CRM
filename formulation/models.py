from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    quantity = models.FloatField()

    def __str__(self):
        return self.name


class Formulation(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient, through='FormulationIngredient')
    instructions = models.TextField()

    def __str__(self):
        return self.name


class FormulationIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    formulation = models.ForeignKey(Formulation, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.ingredient.name} in {self.formulation.name}"
