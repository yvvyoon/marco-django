from django.db import models


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class SampleModel(BaseModel):
    user_id = models.BigIntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        managed = True
        db_table = 'sample_models'
        app_label = 'skeleton'
