from django.db import models
from django.utils import timezone
class Dialog(models.Model):
	sender = models.ForeignKey('auth.User',related_name="sender", on_delete=models.CASCADE)
	receiver = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	def __str__(self):
		return _("Chatting with") + self.receiver

class Message(models.Model):
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	send_date = models.DateTimeField(blank=True, null=True)
	read = models.BooleanField()
	sender = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	def publish(self):
		self.send_date = timezone.now()
		self.save()
	def __str__(self):
		return self.sender + ":" + self.text + self.send_date




