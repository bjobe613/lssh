var serverUrl = 'http://localhost:5000'
function login() {
    data = {
        "username": $("#login-form-username").val(),
        "password": $("#login-form-password").val()
    }

    var email = "test";

    $.ajax({
        url: serverUrl + '/users/login', 
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(email),
        success: function (res) {
            sessionStorage.setItem('auth', JSON.stringify(res.token))
        }
    });


}