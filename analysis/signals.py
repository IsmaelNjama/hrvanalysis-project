from django.db.models.signals import post_save
from django.db import transaction
from django.dispatch import receiver
from .models import Result, Sample
from .tasks import compute_result

@receiver(post_save, sender=Sample)
def create_result(sender, instance, created, **kwargs):
	if created:
		transaction.on_commit(lambda: compute_result.delay(instance.pk))