$(function(){
	$("#info-txt-decr").hide();
	$("#info-txt-cr").hide();
	$("#info-txt-key").hide();
	$("#info-txt-btncr").hide();
	$("#info-txt-btndecr").hide();
	$("#info-txt-btnclr").hide();


	$("#decrypted").mouseenter(function(){
		$("#info-txt-decr").show(200)
	});
	$("#decrypted").mouseleave(function(){
		$("#info-txt-decr").hide(200)
	});
	$("#crypted").mouseenter(function(){
		$("#info-txt-cr").show(200)
	});
	$("#crypted").mouseleave(function(){
		$("#info-txt-cr").hide(200)
	});
	$("#key").mouseenter(function(){
		$("#info-txt-key").show(200)
	});
	$("#key").mouseleave(function(){
		$("#info-txt-key").hide(200)
	});
	$("#btncrypt").mouseenter(function(){
		$("#info-txt-btncr").show(200)
	});
	$("#btncrypt").mouseleave(function(){
		$("#info-txt-btncr").hide(200)
	});
	$("#btndecrypt").mouseenter(function(){
		$("#info-txt-btndecr").show(200)
	});
	$("#btndecrypt").mouseleave(function(){
		$("#info-txt-btndecr").hide(200)
	});
	$("#btnclear").mouseenter(function(){
		$("#info-txt-btnclr").show(200)
	});
	$("#btnclear").mouseleave(function(){
		$("#info-txt-btnclr").hide(200)
	});

	$("#btnclear").click(function(){
		$("#decrypted").val(null);
		$("#key").val(null);
		$("#crypted").val(null);
		$('#bar-chart').empty();
	});
	$("#btndecrypt").click(function(){
		var data = {
			word: $("#decrypted").val(),
			key: $("#key").val(),
			}
		var jsondata = JSON.stringify(data);
		$.ajax({
			url: 'http://127.0.0.1:8000/CesarApp/d/',
			type: 'POST',
			data : jsondata,
			success: function(data){
				$("#crypted").val(data.result);	
			}
		});
	});	  
	$("#btncrypt").click(function(){
			var data = {
				word: $("#decrypted").val(),
				key: $("#key").val(),
				}
			var jsondata = JSON.stringify(data);
			$.ajax({
				url: 'http://127.0.0.1:8000/CesarApp/c/',
				type: 'POST',
				data : jsondata,
				success: function(data){
					$("#crypted").val(data.result);
				s}
			});
							
	});

	$("#decrypted").change(function(){
		$('#bar-chart').empty();
		var data = {
			word: $("#decrypted").val()
			}
		var jsondata = JSON.stringify(data);
		$.ajax({
			url:'http://127.0.0.1:8000/CesarApp/i/',
			type: 'POST',
			data: jsondata,
			success: function(data){
				window.number = data.number;
				window.word = data.word;
				var BarChartData = {
					"datasets": {
						"values": number,
						"labels": word,
						"color": "blue"
					},
					"title": "Количество введенных символов",
					"noY": true,
					"height": "300px",
					"width": "1200px",
					"background": "#FFFFFF",
					"shadowDepth": "1"
				};
				MaterialCharts.bar("#bar-chart", BarChartData)
			}
		});
	});

});