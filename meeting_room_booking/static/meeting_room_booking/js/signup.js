
function formValidation()
{
var passid = document.registration.password1;
var repassid = document.registration.repassword;
var fname = document.registration.First_name;
var lname = document.registration.Last_name;
var uadd = document.registration.address;
var phone1 = document.registration.phone;
var designation = document.registration.designation;
var department = document.registration.department;
var uemail = document.registration.email;

if(passid_validation(passid,repassid,7,12))
{
if(passvalidation())
{
if(allLetter(fname))
{
if(allLetter(lname))
{
if(allNumber(phone1))
{
if(alphanumeric(uadd))
{ 
if(allLetter(department))
{
if(allLetter(designation))
{
if(ValidateEmail(uemail))
{
} 
}
} 
}
}
}
}
}
}
return false;
} 

function passid_validation(passid,repassid,mx,my)
{
var passid_len = passid.value.length;
var repassid_len = repassid.value.length;

if (passid_len == 0 || passid_len >= my || passid_len < mx) 
{
alert("Password should not be empty / length be between "+mx+" to "+my);
document.registration.password.focus();
return false;
}
if (repassid_len == 0 || repassid_len >= my || repassid_len < mx) 
{
alert("Password should not be empty / length be between "+mx+" to "+my);
document.registration.repassword.focus();
return false;
}
return true;
}

function passvalidation()
{
var passid_val = document.registration.password1.value;
var repassid_val = document.registration.repassword.value;
console.log("Hello");
if (passid_val == repassid_val)
{
	return true;
}
else
{
	alert("Passwords do not match");
	return false;
}
}

function allLetter(uname)
{ 
var letters = /^[A-Za-z]+$/;
if(uname.value.match(letters))
{
return true;
}
else
{
alert('Name must have alphabet characters only');
uname.focus();
return false;
}
}
function allNumber(phone1)
{ 
var numbers = /^[0-9]+$/;
if(phone1.value.match(numbers))
{
return true;
}
else
{
alert('Phone no. must have numbers only');
uname.focus();
return false;
}
}
function alphanumeric(uadd)
{ 
var letters = /^[0-9a-zA-Z]+$/;
if(uadd.value.match(letters))
{
return true;
}
else
{
alert('User address must have alphanumeric characters only');
uadd.focus();
return false;
}
}

function ValidateEmail(uemail)
{
	var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	if(uemail.value.match(mailformat))
	{
	return true;
	}
	else
	{
	alert("You have entered an invalid email address!");
	uemail.focus();
	return false;
	}
}

