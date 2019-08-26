$(document).ready(function() { 
	$('body').bootstrapMaterialDesign(); 

	$('#words_submit').click(function() {
		word1 = $('#word1').val()
		word2 = $('#word2').val()
		theme = $('#theme').val()

		$.ajax(`http://localhost:5000/add/${word1}/${word2}/${theme}`)
	})

	$('#db_submit').click(function() {
		db = $('#db').val()
		$.ajax(`http://localhost:5000/db/${db}`)
	})
})