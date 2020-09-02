var serverUrl = 'http://localhost:5000'

function login() {
    data = {
        "username": $("#login-form-username").val(),
        "password": $("#login-form-password").val()
    }

    $.ajax({
        url: serverUrl + '/users/login', 
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function (res) {
            sessionStorage.setItem('auth', JSON.stringify(res.token))
            document.cookie = JSON.stringify(res.token)
        }
    });


}

function headertest() {

    $.ajax({
        url: serverUrl + 'users/protected',
        type: 'GET',
        headers: {'Authorization' : 'bearer ' + sessionStorage.getItem('auth')},
        success: function (){
            alert('success in header')
        }
    });
}