$('#admin-product-search-button').click(function (e) {
    e.preventDefault();
    var searchVal = document.getElementById("admin-product-search-field").value;

    location.href="/admin/products/search/" + searchVal;
});