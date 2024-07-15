function Validateform() {
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const phone = document.getElementById("phone").value;
  const password = document.getElementById("password").value;
  const name_error = document.getElementById("nameError");
  const email_error = document.getElementById("emailError");
  const phone_error = document.getElementById("phoneError");
  const password_error = document.getElementById("passwordError");

  var phonecheck = /^[0-9]{10}$/;
  var emailcheck = /[A-Za-z0-9\._%+\-]+@[A-Za-z0-9\.\-]+\.[A-Za-z]{2,}/;
  var pswcheck = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9@#$%^&*]{8,15}$/;

  name_error.textContent = "";
  email_error.textContent = "";
  phone_error.textContent = "";
  password_error.textContent = "";

  let isValid = true;

  if(name === ""){
    document.getElementById("nameError").innerHTML = "Enter Username"
  }
  if (emailcheck.test(email)) {
    document.getElementById("emailError").innerHTML = "";
  } else {
    document.getElementById("emailError").innerHTML = "**Email-id is invalid";
    isValid = false;
  }

  if (phonecheck.test(phone)) {
    document.getElementById("phoneError").innerHTML = "";
  } else {
    document.getElementById("phoneError").innerHTML =
      "**Phone Number is invalid";
    isValid = false;
  }

  if (pswcheck.test(password)) {
    document.getElementById("passwordError").innerHTML = "";
  } else {
    document.getElementById("passwordError").innerHTML =
      "**Should not contain digits and special characters";
    isValid = false;
  }
  return isValid;
}

function LoginValidateform(){
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const email_error = document.getElementById("emailError");
    const password_error = document.getElementById("passwordError");
  
    var emailcheck = /[A-Za-z0-9\._%+\-]+@[A-Za-z0-9\.\-]+\.[A-Za-z]{2,}/;
    var pswcheck = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9@#$%^&*]{8,15}$/;
  
    email_error.textContent = "";
    password_error.textContent = "";
  
    let isValid = true;
  
    if (emailcheck.test(email)) {
      document.getElementById("emailError").innerHTML = "";
    } else {
      document.getElementById("emailError").innerHTML = "**Email-id is invalid";
      isValid = false;
    }
  
    if (pswcheck.test(password)) {
      document.getElementById("passwordError").innerHTML = "";
    } else {
      document.getElementById("passwordError").innerHTML =
        "**Should not contain digits and special characters";
      isValid = false;
    }
    return isValid;   
}
