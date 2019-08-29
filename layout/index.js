function get_new_word() {
	$.ajax({
		type: 'GET',
		url: `http://${host}/repeat`,
		async: true,
		success: function(text) {
			window.shit = JSON.parse(text)
			$('#wft').text(window.shit[1])
			$('#theme_badge').text(window.shit[5])
		},
		error: function(error) {
			M.toast({html: 'Fail!'})
		}
	})
}

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
				$('#word1').val('')
				$('#word2').val('')
				$('#theme').val('')
				M.toast({html: 'Success!'})
			},
			error: function(error) {
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
				$('#dbn').text(db)
				$('#db').val('')
				M.toast({html: 'Success!'})
			},
			error: function(error) {
				M.toast({html: 'Fail!'})
			}
		})
	})

	$('#repeat_submit').click(function() {
		host  = $(location).attr('hostname') + ':5000'
		if ($('#wft').text() == "") {
			get_new_word()
		} else if ($('#translate').val() == window.shit[2]) {
			M.toast({html: 'Right!', classes: 'light-green-text text-accent-2'})
			get_new_word()
		} else {
			M.toast({html: 'Wrong!', classes: 'red-text text-accent-2'})
			get_new_word()
		}
	})
})