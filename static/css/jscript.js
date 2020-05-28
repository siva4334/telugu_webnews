
$('a').slice(0,6).on('mouseover',function(){
	$(this).css({color:'rgb(250,5,5)'})
});

$('a').slice(0,6).on('mouseout',function(){
	$(this).css({color:'white'})
});



$('a').slice(6,1000).on('mouseover',function(){
	$(this).css({color:'red'})
});

$('a').slice(6,1000).on('mouseout',function(){
	$(this).css({color:'black'})
});


