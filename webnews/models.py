from django.db import models

# Create your models here.


class newsinfo(models.Model):
	newstitle=models.CharField(primary_key=True,max_length=200)
	newsheading=models.CharField(null=False,blank=False,default=' ',max_length=200)
	newsimage1=models.ImageField(null=False,blank=False,upload_to='images/')
	newsimage2=models.ImageField(null=True,blank=True,upload_to='images/')
	datetime=models.DateTimeField(auto_now=True)
	newscategory=models.CharField(null=False,blank=False,max_length=15)
	newstext1=models.TextField(null=False,blank=False,max_length=2000)
	newstext2=models.TextField(null=False,blank=False,max_length=2000)
	newstext3=models.TextField(null=True,blank=True,max_length=2000)

	def __str__(self):
		return self.newstitle

class adv(models.Model):
	advid=models.IntegerField(primary_key=True)
	advname=models.CharField(max_length=100)
	advimg=models.ImageField(null=False,blank=False,upload_to='images/')
	advheight=models.IntegerField(null=True,blank=True)
	advside=models.CharField(default='left',max_length=10)
	datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.advname



