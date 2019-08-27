$(document).ready(function() { 
	$('#words_submit').click(function() {
		word1 = $('#word1').val()
		word2 = $('#word2').val()
		theme = $('#theme').val()
		host  = $(location).attr('hostname') + ':5000'

		$.ajax({
			type: 'GET',
			url: `http://${host}/add/${word1}/${word2}/${theme}`,
			async: true,
			success: function(text) {
				if (text == "OK") 
					M.toast({html: 'Success!'})
				else
					M.toast({html: 'Fail!'})
			}
		})
	})

	$('#db_submit').click(function() {
		db   = $('#db').val()
		host = $(location).attr('hostname') + ':5000'

		$.ajax({
			type: 'GET',
			url: `http://${host}/db/${db}`,
			async: true,
			success: function(text) {
				if (text == "OK") 
					M.toast({html: 'Success!'})
				else
					M.toast({html: 'Fail!'})
			}
		})
	})
})