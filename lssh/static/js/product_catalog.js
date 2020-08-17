/* All possible filters */
let possibleFilters = [];

/* All filters from possibleFilters that are checked in their checkbox */
let checkedFilters = [];

/* KEY: All filters from possibleFilters. VALUE: The corresponding category */
let possibleDict = {};

/* KEY: All filters from checkedFilters. VALUE: The corresponding category */
let checkedDict = {};

function listFilters(typeOfCategory) {
  $.ajax({
    url: "/products/products_content",
    type: "GET",
    success: function(prodList) {
      for (prod of prodList){
        if (prod[typeOfCategory] && !possibleFilters.includes(prod[typeOfCategory])){
          possibleFilters.push(prod[typeOfCategory]);
        }
      }

      console.log(possibleFilters);

      possibleFilters.sort();
      for (i of possibleFilters) {
        $('#collapse-'+typeOfCategory).append('<p>'+i+'</p>');
      }
    },
    error:function() {
      console.log("Error while GET filter information")
    }

  });
};

listFilters('category');
