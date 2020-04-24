from django.contrib import admin

# Register your models here.

# Register your models here.
from webnews.models import newsinfo,adv,tablehead,tabledata1,tabledata2

# Register your models here.

class newsinfoadmin(admin.ModelAdmin):
	list=['newsid','newstitle','newsheading','newsimage1','newsimage2','datetime','newscategory','newstext1','newstext2','newstext3']

class advadmin(admin.ModelAdmin):
	list=['advid','advname','advimg','advheight','advside','datetime']
	
class tableheadadmin(admin.ModelAdmin):	
	list=['th1title','th2title','th11','th12','th13','th14','th14','th21','th22','th23','th24','th25']

class tabledata1admin(admin.ModelAdmin):
	list=['td11','td12','td13','td14','td15','td21','td22','td23','td24','td25','td31','td32','td33','td34','td35','td41','td42','td43','td44','td45','td51','td52','td53','td54','td55','td61','td62','td63','td64','td65']


class tabledata2admin(admin.ModelAdmin):
	list=['td11','td12','td13','td14','td15','td21','td22','td23','td24','td25','td31','td32','td33','td34','td35','td41','td42','td43','td44','td45','td51','td52','td53','td54','td55','td61','td62','td63','td64','td65']


admin.site.register(newsinfo,newsinfoadmin)
admin.site.register(adv,advadmin)
admin.site.register(tablehead,tableheadadmin)
admin.site.register(tabledata1,tabledata1admin)
admin.site.register(tabledata2,tabledata2admin)