from django.db import models

class K8sCluster(models.Model):
    name = models.CharField(max_length=100, unique=True)
    api_endpoint = models.URLField()
    provider_info = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name