function displayError(event, message) {
    event.preventDefault();
    const error_message = document.querySelector(".error_message");
    const message_content = document.getElementById("message_content");
    error_message.style.display = 'block';
    message_content.textContent = message;
    setTimeout(() => {
        error_message.style.display = 'none';
    }, 3000);
}
document.getElementById('SignupForm')?.addEventListener('submit', function (event) {
    const uname = document.getElementById("name")?.value;
    const utel = document.getElementById("phone")?.value;
    const uemail = document.getElementById("email")?.value;
    const upassword = document.getElementById("password")?.value;
    const ucpassword = document.getElementById("cpassword")?.value;

    const regex_pswd = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    const regex_email = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    if (!uname || !utel || !uemail || !upassword || !ucpassword) {
        displayError(event, "Fill All The Data");
        return;
    }
    if (utel.length !== 10) {
        displayError(event, "Phone Number Should Contain 10 Digits");
        return;
    }
    if (!regex_pswd.test(upassword)) {
        displayError(event, "Invalid Password!! Please Enter a Strong Password");
        return;
    }
    if (!regex_email.test(uemail)) {
        displayError(event, "Invalid Email!!");
        return;
    }
    if (upassword !== ucpassword) {
        displayError(event, "Password and Confirm Password Don't Match");
        return;
    }
});
