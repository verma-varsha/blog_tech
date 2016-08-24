$(document).ready(function(){
    $(".comment_div").hide();
   
	$(".comment_btn").click(function(){
		$(".comment_div").toggle();
	});
    
	$(function() {
    var div = $(".image");
    var width = div.width();
    
    div.css("height", width*0.7);
    });
});

$(".read_comments_btn").click(function(){
		$(".previous_comments").toggle();
	});
	
