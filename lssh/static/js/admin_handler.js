

function login() {
    data = {
        "username": $("#login-form-username").val(),
        "password": $("#login-form-password").val()
    }
    

    $.ajax({
        url: '/admin_login', 
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function (res) {
            sessionStorage.setItem('auth', JSON.stringify(res.token))
            document.cookie = JSON.stringify(res.token)
            window.location = "admin/";
        }
    });


}

/*function headertest() {

    $.ajax({
        url: serverUrl + 'users/protected',
        type: 'GET',
        headers: {'Authorization' : 'bearer ' + sessionStorage.getItem('auth')},
        success: function (){
            alert('success in header')
        }
    });
}*/