from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Result, Sample


@receiver(post_save, sender=Sample)
def compute_result(sender, instance, created, **kwargs):
	if created:
		Result.objects.create(sample=instance)
	instance.result.save()

@receiver(post_save, sender=Sample)
def save_result(sender, instance, created, **kwargs):
	instance.result.save()