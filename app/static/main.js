(function() {
	function getOTP() {
		var xmlhttp;
		console.log('here')

		xmlhttp = new XMLHttpRequest();

		xmlhttp.onreadystatechange = function() {
			if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
				document.getElementById("otp").innerHTML = xmlhttp.responseText;
			}
		}
		xmlhttp.open("POST", "/otp", true);
		xmlhttp.send();
	}
}());