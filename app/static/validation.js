function checkPass()
{
	var pass1 = document.getElementById("password");
	var pass2 = document.getElementById("confirm_password");
	var message = document.getElementById("message")

	var goodColor = "#66ff66"
	var badColor = "#ff6666"


	if(pass1.value == pass2.value)
	{
		message.innerHTML = "Passwords Match !";
		pass2.style.backgroundColor = goodColor;
		return true;
	}
	else
	{
		message.innerHTML = "Passwords Do Not Match!";
		pass2.style.backgroundColor = badColor;
		return false;
	}
}