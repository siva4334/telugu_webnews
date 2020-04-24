from django.db import models

# Create your models here.


class newsinfo(models.Model):
	newsid=models.IntegerField(null=True,blank=True)
	newstitle=models.CharField(primary_key=True,max_length=200)
	newsheading=models.CharField(null=False,blank=False,default=' ',max_length=200)
	newsimage1=models.ImageField(null=False,blank=False,upload_to='images/')
	newsimage2=models.ImageField(null=True,blank=True,upload_to='images/')
	datetime=models.DateTimeField(auto_now=True)
	newscategory=models.CharField(null=False,blank=False,max_length=15)
	newstext1=models.TextField(null=False,blank=False,max_length=1000)
	newstext2=models.TextField(null=False,blank=False,max_length=1000)
	newstext3=models.TextField(null=True,blank=True,max_length=1000)

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
			

class tablehead(models.Model):
	th1title=models.CharField(max_length=50)
	th2title=models.CharField(max_length=50)
	th11=models.CharField(max_length=10)
	th12=models.CharField(max_length=10)
	th13=models.CharField(max_length=10)
	th14=models.CharField(max_length=10)
	th14=models.CharField(max_length=10)
	th21=models.CharField(max_length=10)
	th22=models.CharField(max_length=10)
	th23=models.CharField(max_length=10)
	th24=models.CharField(max_length=10)
	th25=models.CharField(max_length=10)

	
	def __str__(self):
		return str(self.th11)
			
class tabledata1(models.Model):
	td11=models.CharField(max_length=10)
	td12=models.CharField(max_length=10)
	td13=models.CharField(max_length=10)
	td14=models.CharField(max_length=10)
	td15=models.CharField(max_length=10)
	td21=models.IntegerField()
	td22=models.IntegerField()
	td23=models.IntegerField()
	td24=models.IntegerField()
	td25=models.IntegerField()
	td31=models.IntegerField()
	td32=models.IntegerField()
	td33=models.IntegerField()
	td34=models.IntegerField()
	td35=models.IntegerField()
	td41=models.IntegerField()
	td42=models.IntegerField()
	td43=models.IntegerField()
	td44=models.IntegerField()
	td45=models.IntegerField()
	td51=models.IntegerField()
	td52=models.IntegerField()
	td53=models.IntegerField()
	td54=models.IntegerField()
	td55=models.IntegerField()
	td61=models.IntegerField()
	td62=models.IntegerField()
	td63=models.IntegerField()
	td64=models.IntegerField()
	td65=models.IntegerField()

	def __str__(self):
		return str(self.td11)
			

class tabledata2(models.Model):
	td11=models.CharField(max_length=10)
	td12=models.CharField(max_length=10)
	td13=models.CharField(max_length=10)
	td14=models.CharField(max_length=10)
	td15=models.CharField(max_length=10)
	td21=models.IntegerField()
	td22=models.IntegerField()
	td23=models.IntegerField()
	td24=models.IntegerField()
	td25=models.IntegerField()
	td31=models.IntegerField()
	td32=models.IntegerField()
	td33=models.IntegerField()
	td34=models.IntegerField()
	td35=models.IntegerField()
	td41=models.IntegerField()
	td42=models.IntegerField()
	td43=models.IntegerField()
	td44=models.IntegerField()
	td45=models.IntegerField()
	td51=models.IntegerField()
	td52=models.IntegerField()
	td53=models.IntegerField()
	td54=models.IntegerField()
	td55=models.IntegerField()
	td61=models.IntegerField()
	td62=models.IntegerField()
	td63=models.IntegerField()
	td64=models.IntegerField()
	td65=models.IntegerField()

	def __str__(self):
		return str(self.td11)
			