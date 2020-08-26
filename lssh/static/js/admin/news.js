/**
 * Deletes the article specified by id
 * @param {number} id 
 */
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
/**
 * Publishes, respectively unpublishes the article specified by id.
 * @param {number} id 
 * @param {bool} value 
 */
function setPublishedNews(id, value) {

    $.ajax({
        url: '/news/api/' + id,
        type: 'PUT',
        data: {"published" : value},
        dataType: 'json',
        success: function (response) {
           window.location.reload()
        },
        error: function (response) {
            if(value) {
                alert("Couldn't publish article")

            } else {
                alert("Couldn't retract article")
            }
        }
    })
}