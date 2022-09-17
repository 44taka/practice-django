from django.db import models


class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    class Meta:
        db_table = 'sample_tbl'

    def __str__(self):
        return self.title
