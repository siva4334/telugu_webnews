from django.contrib import admin

# Register your models here.

# Register your models here.
from webnews.models import newsinfo,adv

# Register your models here.

class newsinfoadmin(admin.ModelAdmin):
	list=['newstitle','newsheading','newsimage1','newsimage2','datetime','newscategory','newstext1','newstext2','newstext3']

class advadmin(admin.ModelAdmin):
	list=['advid','advname','advimg','advheight','advside','datetime']


admin.site.register(newsinfo,newsinfoadmin)
admin.site.register(adv,advadmin)
