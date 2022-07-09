from pydoc import describe
from django.db import models
class Games(models.Model):
    id = models.IntegerField(verbose_name="ID", primary_key=True)
    tile = models.CharField(verbose_name="Tile", max_length=30,null=False)
    description = models.TextField(verbose_name="Description", max_length=255, null=False)
    year = models.IntegerField(verbose_name="Year")
    publisher = models.CharField(verbose_name="Publisher", max_length=255)
    def __str__(self) -> str:
        return f"{self.title} {self.description} {self.year} {self.publisher}".format(  self.title, self.description, self.year, self.publisher )



