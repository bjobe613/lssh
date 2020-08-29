/* All possible filters */
let possibleFilters = [];

/* All active filters */
let checkedFilters = [];

/* KEY: All filters from possibleFilters. VALUE: The corresponding category */
let possibleConn = {};

/* KEY: All filters from checkedFilters. VALUE: The corresponding category */
let checkedConn = {};

let prodListGlob = [];

let activeCategories = [];

function listFilters(typeOfCategory) {
  $.ajax({
    url: "/products/products_content",
    type: "GET",
    success: function(prodList) {
      prodListGlob = prodList;
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
          $('#collapse-'+typeOfCategory).append('<label class="filter-categories-label">'+
          filter+'<input type="checkbox" onchange="updateFilter('+'&apos;'+filter+'&apos;'+')" id="'+replaceSpaces(typeOfCategory)+'-'+attrID+'"></label>');        
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
  strNoSpaces = str.toString().replace(/\s+/g, '-');
  return strNoSpaces;
}

function updateFilter(filter) {
  i = checkedFilters.indexOf(filter);
  if (i>-1){
    checkedFilters.splice(i, 1);
    delete checkedConn[filter];
  } else {
    checkedConn[filter] = possibleConn[filter];
    checkedFilters.push(filter);
  }
  calculateActiveCategories();
  updateVisualCatalog();
}

function calculateActiveCategories() {
  activeCategories = [];
  for (var key in checkedConn) {
    if(!activeCategories.includes(checkedConn[key]) && checkedConn[key]) {
      activeCategories.push(checkedConn[key])
    }
  }
}

function updateVisualCatalog() {
  if(checkedFilters.length > 0) {
    for(prod of prodListGlob){
      //Try at new solution
      var difCat = 0;
      for(cat of activeCategories) {
        for(filt of checkedFilters) {
          if(checkedConn[filt]==cat && prod[checkedConn[filt]] == filt) {
            difCat++;
            break;
          }
        }
      }

      if(difCat < activeCategories.length) {
        document.getElementById('product-card-hs-'+prod['articleNumber']).classList.add('d-none');
        //document.getElementById('product-card-hs-'+prod['articleNumber']).style = "display:none;position:absolute;";
      } else {
        document.getElementById('product-card-hs-'+prod['articleNumber']).classList.remove('d-none');
        
        //document.getElementById('product-card-hs-'+prod['articleNumber']).style = "display:block;position:relative;";
      }
    }
  } else {
    for(prod of prodListGlob) {
      document.getElementById('product-card-hs-'+prod['articleNumber']).classList.remove('d-none');
    }
  }
}

//$(".filter-checkbox").on("change", function() {
//  filterID = $(this).attr('id');
//  console.log("hej");
//  console.log(filterID);
//})

listFilters('category');
listFilters('color');
listFilters('condition');
listFilters('paymentMethod');
