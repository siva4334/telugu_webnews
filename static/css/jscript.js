
$('a').slice(0,5).on('mouseover',function(){
	$(this).css({color:'rgb(250,5,5)'})
});

$('a').slice(0,5).on('mouseout',function(){
	$(this).css({color:'white'})
});



$('a').slice(5,1000).on('mouseover',function(){
	$(this).css({color:'red'})
});

$('a').slice(5,1000).on('mouseout',function(){
	$(this).css({color:'black'})
});

