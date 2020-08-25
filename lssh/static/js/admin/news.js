function deleteNews(id) {
    $.ajax({
        url: '/news/api/' + id,
        type: 'DELETE',
        dataType: 'json',
        success: function (response) {
           window.location.reload()
        },
        error: function (response) {
            alert("Couldn't remove article")
        }
    })
}