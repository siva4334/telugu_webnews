from django.shortcuts import render
from django.http import HttpResponse
from webnews.models import newsinfo,adv,tablehead,tabledata1,tabledata2

# Create your views here.
def mainpage(request):
	top_news1=newsinfo.objects.all().order_by('-datetime')[:1]
	top_news2=newsinfo.objects.all().order_by('-datetime')[1:2]
	top_news3=newsinfo.objects.all().order_by('-datetime')[2:3]
	sub_news11=newsinfo.objects.all().order_by('-datetime')[3:4]
	sub_news12=newsinfo.objects.all().order_by('-datetime')[4:5]
	sub_news13=newsinfo.objects.all().order_by('-datetime')[5:6]
	sub_news21=newsinfo.objects.all().order_by('-datetime')[6:7]
	sub_news22=newsinfo.objects.all().order_by('-datetime')[7:8]
	sub_news23=newsinfo.objects.all().order_by('-datetime')[8:9]
	sub_news31=newsinfo.objects.all().order_by('-datetime')[9:10]
	sub_news32=newsinfo.objects.all().order_by('-datetime')[10:11]
	sub_news33=newsinfo.objects.all().order_by('-datetime')[11:12]
	sub_news41=newsinfo.objects.all().order_by('-datetime')[12:13]
	sub_news42=newsinfo.objects.all().order_by('-datetime')[13:14]
	sub_news43=newsinfo.objects.all().order_by('-datetime')[14:15]
	sub_news51=newsinfo.objects.all().order_by('-datetime')[15:16]
	sub_news52=newsinfo.objects.all().order_by('-datetime')[16:17]
	sub_news53=newsinfo.objects.all().order_by('-datetime')[17:18]
	sub_news61=newsinfo.objects.all().order_by('-datetime')[18:19]
	sub_news62=newsinfo.objects.all().order_by('-datetime')[19:20]
	sub_news63=newsinfo.objects.all().order_by('-datetime')[20:21]
	sub_news71=newsinfo.objects.all().order_by('-datetime')[21:22]
	sub_news72=newsinfo.objects.all().order_by('-datetime')[22:23]
	sub_news73=newsinfo.objects.all().order_by('-datetime')[23:24]
	sub_news81=newsinfo.objects.all().order_by('-datetime')[24:25]
	sub_news82=newsinfo.objects.all().order_by('-datetime')[25:26]
	sub_news83=newsinfo.objects.all().order_by('-datetime')[26:27]
	sub_news91=newsinfo.objects.all().order_by('-datetime')[27:28]
	sub_news92=newsinfo.objects.all().order_by('-datetime')[28:29]
	sub_news93=newsinfo.objects.all().order_by('-datetime')[29:30]
	sub_news101=newsinfo.objects.all().order_by('-datetime')[30:31]
	sub_news102=newsinfo.objects.all().order_by('-datetime')[31:32]
	sub_news103=newsinfo.objects.all().order_by('-datetime')[32:33]
	sub_news111=newsinfo.objects.all().order_by('-datetime')[33:34]
	sub_news112=newsinfo.objects.all().order_by('-datetime')[34:35]
	sub_news113=newsinfo.objects.all().order_by('-datetime')[35:36]
	sub_news121=newsinfo.objects.all().order_by('-datetime')[36:37]
	sub_news122=newsinfo.objects.all().order_by('-datetime')[37:38]
	sub_news123=newsinfo.objects.all().order_by('-datetime')[38:39]
	sub_news131=newsinfo.objects.all().order_by('-datetime')[39:40]
	sub_news132=newsinfo.objects.all().order_by('-datetime')[40:41]
	sub_news133=newsinfo.objects.all().order_by('-datetime')[41:42]
	sub_news141=newsinfo.objects.all().order_by('-datetime')[42:43]
	sub_news142=newsinfo.objects.all().order_by('-datetime')[43:44]
	sub_news143=newsinfo.objects.all().order_by('-datetime')[44:45]
	sub_news151=newsinfo.objects.all().order_by('-datetime')[45:46]
	sub_news152=newsinfo.objects.all().order_by('-datetime')[46:47]
	sub_news153=newsinfo.objects.all().order_by('-datetime')[47:48]
	sub_news161=newsinfo.objects.all().order_by('-datetime')[48:49]
	sub_news162=newsinfo.objects.all().order_by('-datetime')[49:50]
	sub_news163=newsinfo.objects.all().order_by('-datetime')[50:51]
	
	
# Left adv data
	leftadvfil=adv.objects.all().filter(advside='left')
	leftadv1=leftadvfil.order_by('-datetime')[:1]
	leftadv2=leftadvfil.order_by('-datetime')[1:2]
	leftadv3=leftadvfil.order_by('-datetime')[2:3]
	leftadv4=leftadvfil.order_by('-datetime')[3:4]
	leftadv5=leftadvfil.order_by('-datetime')[4:5]
# rightadvdata(request):
	rightadvfil=adv.objects.all().filter(advside='right')
	rightadv1=rightadvfil.order_by('-datetime')[:1]
	rightadv2=rightadvfil.order_by('-datetime')[1:2]
	rightadv3=rightadvfil.order_by('-datetime')[2:3]
	rightadv4=rightadvfil.order_by('-datetime')[3:4]
	rightadv5=rightadvfil.order_by('-datetime')[4:5]
	mynews={'top_news1':top_news1,'top_news2':top_news2,'top_news3':top_news3,'sub_news11':sub_news11,'sub_news12':sub_news12,'sub_news13':sub_news13,'sub_news21':sub_news21,'sub_news22':sub_news22,'sub_news23':sub_news23,'sub_news31':sub_news31,	'sub_news32':sub_news32,	'sub_news33':sub_news33,'sub_news41':sub_news41,'sub_news42':sub_news42,'sub_news43':sub_news43,'sub_news51':sub_news51,'sub_news52':sub_news52,'sub_news53':sub_news53,'sub_news61':sub_news61,'sub_news62':sub_news62,'sub_news63':sub_news63,'sub_news71':sub_news71,'sub_news72':sub_news72,'sub_news73':sub_news73,'sub_news81':sub_news81,'sub_news82':sub_news82,'sub_news83':sub_news83,'sub_news91':sub_news91,'sub_news92':sub_news92,'sub_news93':sub_news93,'sub_news101':sub_news101,'sub_news102':sub_news102,'sub_news103':sub_news103,
	'leftadv1':leftadv1,'leftadv2':leftadv2,'leftadv3':leftadv3,'leftadv4':leftadv4,'leftadv5':leftadv5,'rightadv1':rightadv1,'rightadv2':rightadv2,'rightadv3':rightadv3,'rightadv4':rightadv4,'rightadv5':rightadv5}
	return render(request,'main.html',context=mynews)
		
def subpage(request,title):
	all_news=newsinfo.objects.all()
	t_news=filter(lambda x: (x.newstitle == title), all_news)
	top_news1=newsinfo.objects.all().order_by('-datetime')[:1]
	top_news2=newsinfo.objects.all().order_by('-datetime')[1:2]
	top_news3=newsinfo.objects.all().order_by('-datetime')[2:3]
	sub_news11=newsinfo.objects.all().order_by('-datetime')[3:4]
	sub_news12=newsinfo.objects.all().order_by('-datetime')[4:5]
	sub_news13=newsinfo.objects.all().order_by('-datetime')[5:6]
	sub_news21=newsinfo.objects.all().order_by('-datetime')[6:7]
	sub_news22=newsinfo.objects.all().order_by('-datetime')[7:8]
	sub_news23=newsinfo.objects.all().order_by('-datetime')[8:9]
	sub_news31=newsinfo.objects.all().order_by('-datetime')[9:10]
	sub_news32=newsinfo.objects.all().order_by('-datetime')[10:11]
	sub_news33=newsinfo.objects.all().order_by('-datetime')[11:12]
	sub_news41=newsinfo.objects.all().order_by('-datetime')[12:13]
	sub_news42=newsinfo.objects.all().order_by('-datetime')[13:14]
	sub_news43=newsinfo.objects.all().order_by('-datetime')[14:15]
	sub_news51=newsinfo.objects.all().order_by('-datetime')[15:16]
	sub_news52=newsinfo.objects.all().order_by('-datetime')[16:17]
	sub_news53=newsinfo.objects.all().order_by('-datetime')[17:18]
	sub_news61=newsinfo.objects.all().order_by('-datetime')[18:19]
	sub_news62=newsinfo.objects.all().order_by('-datetime')[19:20]
	sub_news63=newsinfo.objects.all().order_by('-datetime')[20:21]
	sub_news71=newsinfo.objects.all().order_by('-datetime')[21:22]
	sub_news72=newsinfo.objects.all().order_by('-datetime')[22:23]
	sub_news73=newsinfo.objects.all().order_by('-datetime')[23:24]
	
	leftadvfil=adv.objects.all().filter(advside='left')
	leftadv1=leftadvfil.order_by('-datetime')[:1]
	leftadv2=leftadvfil.order_by('-datetime')[1:2]
	leftadv3=leftadvfil.order_by('-datetime')[2:3]
	leftadv4=leftadvfil.order_by('-datetime')[3:4]
	leftadv5=leftadvfil.order_by('-datetime')[4:5]
# rightadvdata(request):
	rightadvfil=adv.objects.all().filter(advside='right')
	rightadv1=rightadvfil.order_by('-datetime')[:1]
	rightadv2=rightadvfil.order_by('-datetime')[1:2]
	rightadv3=rightadvfil.order_by('-datetime')[2:3]
	rightadv4=rightadvfil.order_by('-datetime')[3:4]
	rightadv5=rightadvfil.order_by('-datetime')[4:5]
	text={'t_news':t_news,'top_news1':top_news1,'top_news2':top_news2,'top_news3':top_news3,'sub_news11':sub_news11,'sub_news12':sub_news12,'sub_news13':sub_news13,'sub_news21':sub_news21,'sub_news22':sub_news22,'sub_news23':sub_news23,'sub_news31':sub_news31,	'sub_news32':sub_news32,	'sub_news33':sub_news33,'sub_news41':sub_news41,'sub_news42':sub_news42,'sub_news43':sub_news43,'sub_news51':sub_news51,'sub_news52':sub_news52,'sub_news53':sub_news53,'sub_news61':sub_news61,'sub_news62':sub_news62,'sub_news63':sub_news63,'sub_news71':sub_news71,'sub_news72':sub_news72,'sub_news73':sub_news73,'leftadv1':leftadv1,'leftadv2':leftadv2,'leftadv3':leftadv3,'leftadv4':leftadv4,'leftadv5':leftadv5,'rightadv1':rightadv1,'rightadv2':rightadv2,'rightadv3':rightadv3,'rightadv4':rightadv4,'rightadv5':rightadv5}
	return render(request,'inner1.html',context=text)

def national(request):
	nationalnews=newsinfo.objects.all().filter(newscategory='national')
	national11=nationalnews.order_by('-datetime')[:1]
	national12=nationalnews.order_by('-datetime')[1:2]
	national21=nationalnews.order_by('-datetime')[2:3]
	national22=nationalnews.order_by('-datetime')[3:4]
	national31=nationalnews.order_by('-datetime')[4:5]
	national32=nationalnews.order_by('-datetime')[5:6]
	national41=nationalnews.order_by('-datetime')[6:7]
	national42=nationalnews.order_by('-datetime')[7:8]
	national51=nationalnews.order_by('-datetime')[8:9]
	national52=nationalnews.order_by('-datetime')[9:10]
	national61=nationalnews.order_by('-datetime')[10:11]
	national62=nationalnews.order_by('-datetime')[11:12]
	national71=nationalnews.order_by('-datetime')[12:13]
	national72=nationalnews.order_by('-datetime')[13:14]
	national81=nationalnews.order_by('-datetime')[14:15]
	national82=nationalnews.order_by('-datetime')[15:16]
	national91=nationalnews.order_by('-datetime')[16:17]
	national92=nationalnews.order_by('-datetime')[17:18]
	national101=nationalnews.order_by('-datetime')[18:19]
	national102=nationalnews.order_by('-datetime')[19:20]
	
	leftadvfil=adv.objects.all().filter(advside='left')
	leftadv1=leftadvfil.order_by('-datetime')[:1]
	leftadv2=leftadvfil.order_by('-datetime')[1:2]
	leftadv3=leftadvfil.order_by('-datetime')[2:3]
	leftadv4=leftadvfil.order_by('-datetime')[3:4]
	leftadv5=leftadvfil.order_by('-datetime')[4:5]
# rightadvdata(request):
	rightadvfil=adv.objects.all().filter(advside='right')
	rightadv1=rightadvfil.order_by('-datetime')[:1]
	rightadv2=rightadvfil.order_by('-datetime')[1:2]
	rightadv3=rightadvfil.order_by('-datetime')[2:3]
	rightadv4=rightadvfil.order_by('-datetime')[3:4]
	rightadv5=rightadvfil.order_by('-datetime')[4:5]
	national_news={'leftadv1':leftadv1,'leftadv2':leftadv2,'leftadv3':leftadv3,'leftadv4':leftadv4,'leftadv5':leftadv5,'rightadv1':rightadv1,'rightadv2':rightadv2,'rightadv3':rightadv3,'rightadv4':rightadv4,'rightadv5':rightadv5,'national11':national11,'national12':national12,'national21':national21,'national22':national22,'national31':national31,'national32':national32,'national41':national41,'national42':national42,'national51':national51,'national52':national52,'national61':national61,'national62':national62,'national71':national71,'national72':national72,'national81':national81,'national82':national82,'national91':national91,'national92':national92,'national101':national101,'national102':national102}
	return render(request,'national.html',context=national_news)

def international(request):
	internationalnews=newsinfo.objects.all().filter(newscategory='international')
	international11=internationalnews.order_by('-datetime')[:1]
	international12=internationalnews.order_by('-datetime')[1:2]
	international21=internationalnews.order_by('-datetime')[2:3]
	international22=internationalnews.order_by('-datetime')[3:4]
	international31=internationalnews.order_by('-datetime')[4:5]
	international32=internationalnews.order_by('-datetime')[5:6]
	international41=internationalnews.order_by('-datetime')[6:7]
	international42=internationalnews.order_by('-datetime')[7:8]
	international51=internationalnews.order_by('-datetime')[8:9]
	international52=internationalnews.order_by('-datetime')[9:10]
	international61=internationalnews.order_by('-datetime')[10:11]
	international62=internationalnews.order_by('-datetime')[11:12]
	international71=internationalnews.order_by('-datetime')[12:13]
	international72=internationalnews.order_by('-datetime')[13:14]
	international81=internationalnews.order_by('-datetime')[14:15]
	international82=internationalnews.order_by('-datetime')[15:16]
	international91=internationalnews.order_by('-datetime')[16:17]
	international92=internationalnews.order_by('-datetime')[17:18]
	international101=internationalnews.order_by('-datetime')[18:19]
	international102=internationalnews.order_by('-datetime')[19:20]
	
	leftadvfil=adv.objects.all().filter(advside='left')
	leftadv1=leftadvfil.order_by('-datetime')[:1]
	leftadv2=leftadvfil.order_by('-datetime')[1:2]
	leftadv3=leftadvfil.order_by('-datetime')[2:3]
	leftadv4=leftadvfil.order_by('-datetime')[3:4]
	leftadv5=leftadvfil.order_by('-datetime')[4:5]
# rightadvdata(request):
	rightadvfil=adv.objects.all().filter(advside='right')
	rightadv1=rightadvfil.order_by('-datetime')[:1]
	rightadv2=rightadvfil.order_by('-datetime')[1:2]
	rightadv3=rightadvfil.order_by('-datetime')[2:3]
	rightadv4=rightadvfil.order_by('-datetime')[3:4]
	rightadv5=rightadvfil.order_by('-datetime')[4:5]
	international_news={'leftadv1':leftadv1,'leftadv2':leftadv2,'leftadv3':leftadv3,'leftadv4':leftadv4,'leftadv5':leftadv5,'rightadv1':rightadv1,'rightadv2':rightadv2,'rightadv3':rightadv3,'rightadv4':rightadv4,'rightadv5':rightadv5,'international11':international11,'international12':international12,'international21':international21,'international22':international22,'international31':international31,'international32':international32,'international41':international41,'international42':international42,'international51':international51,'international52':international52,'international61':international61,'international62':international62,'international71':international71,'international72':international72,'international81':international81,'international82':international82,'international91':international91,'international92':international92,'international101':international101,'international102':international102}
	return render(request,'international.html',context=international_news)
	
	
def local(request):
	localnews=newsinfo.objects.all().filter(newscategory='local')
	local11=localnews.order_by('-datetime')[:1]
	local12=localnews.order_by('-datetime')[1:2]
	local21=localnews.order_by('-datetime')[2:3]
	local22=localnews.order_by('-datetime')[3:4]
	local31=localnews.order_by('-datetime')[4:5]
	local32=localnews.order_by('-datetime')[5:6]
	local41=localnews.order_by('-datetime')[6:7]
	local42=localnews.order_by('-datetime')[7:8]
	local51=localnews.order_by('-datetime')[8:9]
	local52=localnews.order_by('-datetime')[9:10]
	local61=localnews.order_by('-datetime')[10:11]
	local62=localnews.order_by('-datetime')[11:12]
	local71=localnews.order_by('-datetime')[12:13]
	local72=localnews.order_by('-datetime')[13:14]
	local81=localnews.order_by('-datetime')[14:15]
	local82=localnews.order_by('-datetime')[15:16]
	local91=localnews.order_by('-datetime')[16:17]
	local92=localnews.order_by('-datetime')[17:18]
	local101=localnews.order_by('-datetime')[18:19]
	local102=localnews.order_by('-datetime')[19:20]
	leftadvfil=adv.objects.all().filter(advside='left')
	leftadv1=leftadvfil.order_by('-datetime')[:1]
	leftadv2=leftadvfil.order_by('-datetime')[1:2]
	leftadv3=leftadvfil.order_by('-datetime')[2:3]
	leftadv4=leftadvfil.order_by('-datetime')[3:4]
	leftadv5=leftadvfil.order_by('-datetime')[4:5]
# rightadvdata(request):
	rightadvfil=adv.objects.all().filter(advside='right')
	rightadv1=rightadvfil.order_by('-datetime')[:1]
	rightadv2=rightadvfil.order_by('-datetime')[1:2]
	rightadv3=rightadvfil.order_by('-datetime')[2:3]
	rightadv4=rightadvfil.order_by('-datetime')[3:4]
	rightadv5=rightadvfil.order_by('-datetime')[4:5]
	local_news={'leftadv1':leftadv1,'leftadv2':leftadv2,'leftadv3':leftadv3,'leftadv4':leftadv4,'leftadv5':leftadv5,'rightadv1':rightadv1,'rightadv2':rightadv2,'rightadv3':rightadv3,'rightadv4':rightadv4,'rightadv5':rightadv5,'local11':local11,'local12':local12,'local21':local21,'local22':local22,'local31':local31,'local32':local32,'local41':local41,'local42':local42,'local51':local51,'local52':local52,'local61':local61,'local62':local62,'local71':local71,'local72':local72,'local81':local81,'local82':local82,'local91':local91,'local92':local92,'local101':local101,'local102':local102}
	return render(request,'local.html',context=local_news)
	
def cinema(request):
	cinemanews=newsinfo.objects.all().filter(newscategory='cinema')
	cinema11=cinemanews.order_by('-datetime')[:1]
	cinema12=cinemanews.order_by('-datetime')[1:2]
	cinema21=cinemanews.order_by('-datetime')[2:3]
	cinema22=cinemanews.order_by('-datetime')[3:4]
	cinema31=cinemanews.order_by('-datetime')[4:5]
	cinema32=cinemanews.order_by('-datetime')[5:6]
	cinema41=cinemanews.order_by('-datetime')[6:7]
	cinema42=cinemanews.order_by('-datetime')[7:8]
	cinema51=cinemanews.order_by('-datetime')[8:9]
	cinema52=cinemanews.order_by('-datetime')[9:10]
	cinema61=cinemanews.order_by('-datetime')[10:11]
	cinema62=cinemanews.order_by('-datetime')[11:12]
	cinema71=cinemanews.order_by('-datetime')[12:13]
	cinema72=cinemanews.order_by('-datetime')[13:14]
	cinema81=cinemanews.order_by('-datetime')[14:15]
	cinema82=cinemanews.order_by('-datetime')[15:16]
	cinema91=cinemanews.order_by('-datetime')[16:17]
	cinema92=cinemanews.order_by('-datetime')[17:18]
	cinema101=cinemanews.order_by('-datetime')[18:19]
	cinema102=cinemanews.order_by('-datetime')[19:20]
	
	leftadvfil=adv.objects.all().filter(advside='left')
	leftadv1=leftadvfil.order_by('-datetime')[:1]
	leftadv2=leftadvfil.order_by('-datetime')[1:2]
	leftadv3=leftadvfil.order_by('-datetime')[2:3]
	leftadv4=leftadvfil.order_by('-datetime')[3:4]
	leftadv5=leftadvfil.order_by('-datetime')[4:5]
# rightadvdata(request):
	rightadvfil=adv.objects.all().filter(advside='right')
	rightadv1=rightadvfil.order_by('-datetime')[:1]
	rightadv2=rightadvfil.order_by('-datetime')[1:2]
	rightadv3=rightadvfil.order_by('-datetime')[2:3]
	rightadv4=rightadvfil.order_by('-datetime')[3:4]
	rightadv5=rightadvfil.order_by('-datetime')[4:5]
	cinema_news={'leftadv1':leftadv1,'leftadv2':leftadv2,'leftadv3':leftadv3,'leftadv4':leftadv4,'leftadv5':leftadv5,'rightadv1':rightadv1,'rightadv2':rightadv2,'rightadv3':rightadv3,'rightadv4':rightadv4,'rightadv5':rightadv5,'cinema11':cinema11,'cinema12':cinema12,'cinema21':cinema21,'cinema22':cinema22,'cinema31':cinema31,'cinema32':cinema32,'cinema41':cinema41,'cinema42':cinema42,'cinema51':cinema51,'cinema52':cinema52,'cinema61':cinema61,'cinema62':cinema62,'cinema71':cinema71,'cinema72':cinema72,'cinema81':cinema81,'cinema82':cinema82,'cinema91':cinema91,'cinema92':cinema92,'cinema101':cinema101,'cinema102':cinema102}
	return render(request,'cinema.html',context=cinema_news)
	
def sports(request):
	sportsnews=newsinfo.objects.all().filter(newscategory='sports')
	sports11=sportsnews.order_by('-datetime')[:1]
	sports12=sportsnews.order_by('-datetime')[1:2]
	sports21=sportsnews.order_by('-datetime')[2:3]
	sports22=sportsnews.order_by('-datetime')[3:4]
	sports31=sportsnews.order_by('-datetime')[4:5]
	sports32=sportsnews.order_by('-datetime')[5:6]
	sports41=sportsnews.order_by('-datetime')[6:7]
	sports42=sportsnews.order_by('-datetime')[7:8]
	sports51=sportsnews.order_by('-datetime')[8:9]
	sports52=sportsnews.order_by('-datetime')[9:10]
	sports61=sportsnews.order_by('-datetime')[10:11]
	sports62=sportsnews.order_by('-datetime')[11:12]
	sports71=sportsnews.order_by('-datetime')[12:13]
	sports72=sportsnews.order_by('-datetime')[13:14]
	sports81=sportsnews.order_by('-datetime')[14:15]
	sports82=sportsnews.order_by('-datetime')[15:16]
	sports91=sportsnews.order_by('-datetime')[16:17]
	sports92=sportsnews.order_by('-datetime')[17:18]
	sports101=sportsnews.order_by('-datetime')[18:19]
	sports102=sportsnews.order_by('-datetime')[19:20]
	leftadvfil=adv.objects.all().filter(advside='left')
	leftadv1=leftadvfil.order_by('-datetime')[:1]
	leftadv2=leftadvfil.order_by('-datetime')[1:2]
	leftadv3=leftadvfil.order_by('-datetime')[2:3]
	leftadv4=leftadvfil.order_by('-datetime')[3:4]
	leftadv5=leftadvfil.order_by('-datetime')[4:5]
# rightadvdata(request):
	rightadvfil=adv.objects.all().filter(advside='right')
	rightadv1=rightadvfil.order_by('-datetime')[:1]
	rightadv2=rightadvfil.order_by('-datetime')[1:2]
	rightadv3=rightadvfil.order_by('-datetime')[2:3]
	rightadv4=rightadvfil.order_by('-datetime')[3:4]
	rightadv5=rightadvfil.order_by('-datetime')[4:5]
	sports_news={'leftadv1':leftadv1,'leftadv2':leftadv2,'leftadv3':leftadv3,'leftadv4':leftadv4,'leftadv5':leftadv5,'rightadv1':rightadv1,'rightadv2':rightadv2,'rightadv3':rightadv3,'rightadv4':rightadv4,'rightadv5':rightadv5,'sports11':sports11,'sports12':sports12,'sports21':sports21,'sports22':sports22,'sports31':sports31,'sports32':sports32,'sports41':sports41,'sports42':sports42,'sports51':sports51,'sports52':sports52,'sports61':sports61,'sports62':sports62,'sports71':sports71,'sports72':sports72,'sports81':sports81,'sports82':sports82,'sports91':sports91,'sports92':sports92,'sports101':sports101,'sports102':sports102}
	return render(request,'sports.html',context=sports_news)