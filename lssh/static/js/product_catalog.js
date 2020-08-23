/* All possible filters */
let possibleFilters = [];

/* All active filters */
let checkedFilters = [];

/* KEY: All filters from possibleFilters. VALUE: The corresponding category */
let possibleConn = {};

/* KEY: All filters from checkedFilters. VALUE: The corresponding category */
let checkedConn = {};

function listFilters(typeOfCategory) {
  $.ajax({
    url: "/products/products_content",
    type: "GET",
    success: function(prodList) {
      for (prod of prodList){
        if (prod[typeOfCategory] && !possibleFilters.includes(prod[typeOfCategory])){
          possibleFilters.push(prod[typeOfCategory]);
          possibleConn[prod[typeOfCategory]] = typeOfCategory;
        }
      }
      possibleFilters.sort();
      for (filter of possibleFilters) {
        attrID = replaceSpaces(filter);
        if(possibleConn[filter] == typeOfCategory) {  
          $('#collapse-'+typeOfCategory).append('<p>'+filter+'</p>');
        }
      }
    },
    error:function() {
      console.log("Error while GET filter information")
    }

  });
};

/* function to replace spaces with '-' be usable in html.*/
function replaceSpaces(str) {
  strNoSpaces = str.toString().replace(/\s+/g, '');
  return strNoSpaces;
}

listFilters('category');
listFilters('color');
listFilters('condition');
listFilters('paymentMethod');

