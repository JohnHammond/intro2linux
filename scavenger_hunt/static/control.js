$(document).ready(function(){

	$('input').first().focus();

	show_messages('.error');
	show_messages('.message');
	show_messages('.success');

	$('.challenge_title').click(function(){
		
		$(this).next().slideToggle();

	});

});

function check_answer( challenge_id ){

	var given_answer = $('#'+challenge_id+' input[name="answer"]').val();

	$.ajax(
		{ 	url:"/check_answer",
			method: "POST",
			data: { 
					"challenge_id": challenge_id,
					"answer": given_answer
				  },
			dataType: "json",

			success:(function(response){

				if ( response['correct'] == 1){
					var new_score = response['new_score'];

					say_correct( new_score );
					correct_challenge( challenge_id );
					$('#'+ challenge_id + ' #challenge_body').slideUp();


				}
				if ( response['correct'] == 0){
					$.notify('Incorrect!', 'error');
					// say_wrong();
				}
				if ( response['correct'] == -1){
				$.notify('You have already solved this challenge!', 'warn');
					//say_already();
				}
	})});
	
	return false;
};

function say_correct( new_score ){

	// $('.success').text("You are correct! Nice work!");
	// show_message('success');
	
	$.notify('You are correct! Nice work!', 'success');

	$('#score').text( String(new_score) );

}

function correct_challenge(challenge_id){

	$("#" + challenge_id + " h3").css({
		'background-color': '#eeFFee',
		'color': '#348017',
		'border': '1px solid #254117;'
	});
}

function say_wrong(){

	$('.error').text("Incorrect!");
	show_message('error');
}


function say_already(){

	$('.message').text("You have already solved this challenge!");
	show_message('message');
}

function show_message(name){

	$('.' + name).slideDown();

	window.setTimeout( hide_messages, 2000 );
}

function show_messages(name){

	if ( $(name).text() != '' ){
		show_message(name.slice(1));
	}
	
}

function hide_messages( ){

	$('.message').slideUp();
	$('.error').slideUp();
	$('.success').slideUp();
}