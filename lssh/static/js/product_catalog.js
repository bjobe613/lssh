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

let possibleCategories = ['category', 'color', 'condition', 'paymentMethod'];

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
          filter+'<input class="filter-checkbox" type="checkbox" onchange="updateFilter('+'&apos;'+filter+'&apos;'+')" id="'+replaceSpaces(typeOfCategory)+'-'+attrID+'"></label>');        
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
  updateVisualActivatedFilters();
}

function updateVisualActivatedFilters() {
  
  for(cat of possibleCategories) {
    if(activeCategories.includes(cat)) {
      document.getElementById('line-'+cat).style = 'background-color:lightgreen;'
    } else {
      document.getElementById('line-'+cat).style = 'background-color:rgb(240,240,240);'
    }
  }
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
      } else {
        document.getElementById('product-card-hs-'+prod['articleNumber']).classList.remove('d-none');
      }
    }
  } else {
    for(prod of prodListGlob) {
      document.getElementById('product-card-hs-'+prod['articleNumber']).classList.remove('d-none');
    }
  }
  updatePages();
}

function updatePages() {
  var pageProducts = [];
  var pageProductsElements = [];
  var pageID = 1;
  var tempI = 0;
  
  for(prod of prodListGlob){
    if (!document.getElementById('product-card-hs-'+prod['articleNumber']).classList.contains('d-none')) {
      pageProducts.push(prod);
      pageProductsElements.push(document.getElementById('product-card-hs-'+prod['articleNumber']));
    }
    if (tempI < 47) {
      tempI++;
    } else {
      createPage(pageProducts, pageProductsElements, pageID);
      tempI = 0;
      pageProducts = [];
      pageID++;
    }

    if (prodListGlob.pop() == prod && !(tempI == 47)) {
      createPage(pageProducts, pageProductsElements, pageID);
      tempI = 0;
      pageProducts = [];
      pageID++;
    }
    
  }
}

function createPage(pageProducts, pageProductsElements, pageID) {
  for(prod in pageProducts) {
    if($('#product-card-hs-'+pageProducts[prod]['articleNumber']).parent().is(".product-page-wrapper")) {
      console.log("DEL");
      $('#product-card-hs-'+pageProducts[prod]['articleNumber']).unwrap();
      //$('#page-'+pageID).remove();
      console.log(pageID);
    }
  }
  console.log("WRap");
  $(pageProductsElements).wrapAll('<div class="product-page-wrapper" id="page-'+pageID+'"></div>'); 
}


listFilters('category');
listFilters('color');
listFilters('condition');
listFilters('paymentMethod');
