$(document).ready(function() {
	const host = $(location).attr('hostname') + ':5000'

	const get_new_word = function() {
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
			},
			timeout: 3000
		})
	}

	const level_incr = function() {
		$.ajax({
			type: 'GET',
			url: `http://${host}/level_incr/${window.shit[0]}/${window.shit[3]}`,
			async: false,
		})
	}

	const level_drop = function() {
		$.ajax({
			type: 'GET',
			url: `http://${host}/level_drop/${window.shit[0]}`,
			async: false,
		})
	}

	$('#words_submit').click(function() {
		word1 = $('#word1').val()
		word2 = $('#word2').val()
		theme = $('#theme').val()

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
		db = $('#db').val()

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
		if ($('#wft').text() == "") {
			get_new_word()
		} else if ($('#translate').val().toLowerCase() == window.shit[2]) {
			M.toast({html: 'Right!', classes: 'light-green-text text-accent-2'})
			level_incr()
			get_new_word()
		} else {
			M.toast({html: 'Wrong!', classes: 'red-text text-accent-2'})
			level_drop()
			get_new_word()
		}
	})
})