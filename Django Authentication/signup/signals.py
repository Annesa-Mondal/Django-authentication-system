# # code
# from django.db.models.signals import post_save, pre_delete
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import Userprofile

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
# 	if created:
# 		Userprofile.objects.create(user=instance)
# 	else:
# 		print("HHHH<----->")
		

	