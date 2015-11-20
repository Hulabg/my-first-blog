from django.db import models
from django.utils import timezone

class Post(models.Model): # El nombre Post de la clase, es el nombre que queremos darle a esta clase
	author = models.ForeignKey('auth.User')
	title = models.CharField (max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self): # Publish es el nombre del metodo que estamos estableciendo. Podemos poner lo que queramos
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
