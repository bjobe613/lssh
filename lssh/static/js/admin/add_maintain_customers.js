


$('#liu-id-button').click(function (e) {
    e.preventDefault();
    var searchVal = document.getElementById("liu-id-field").value;

    location.href="/admin/add_maintain_customers/" + searchVal;
});


$('#email-button').click(function (e) {
    e.preventDefault();
    var searchVal = document.getElementById("email-field").value;

    location.href="/admin/add_maintain_customers/email/" + searchVal;
});



function deleteCustomer(liuID) {

    

    if (confirm("Are you sure you want to delete this customer?")) {

        data = {
            "liuID": liuID
        }

        $.ajax({
            url: '/admin/add_maintain_customers/delete',
            type: 'POST',
            contentType: "application/json",
            data: JSON.stringify(data),
            success: function (res) {
    
                location.reload();
    
            },
            error: function (error) {
    
            }
        });
      } else {
        
      }

    


}