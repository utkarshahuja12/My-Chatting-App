from django.db import models
from django.utils import timezone

class Message(models.Model):
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	send_date = models.DateTimeField(blank=True, null=True)
	read = models.BooleanField()
	sender = models.ForeignKey('auth.User',related_name='sender',on_delete=models.CASCADE)
	receiver = models.ForeignKey('auth.User',default=None,on_delete=models.CASCADE)
	def __str__(self):
		return "Done" + ":" + self.text + str(self.send_date)




