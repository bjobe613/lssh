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

function listFilters() {
  $.ajax({
    url: "/products/categories",
    type: "GET",
    success: function(categories) {
      for(cat of categories){
        possibleFilters.push(cat['name']);
        possibleConn[cat] = 'category';
      }
    },
    error:function() {
      console.log("Error while GET categories information")
    }
  });

  $.ajax({
    url: "/products/conditions",
    type: "GET",
    success: function(conditions) {
      for(con of conditions){
        possibleFilters.push(con['name']);
        possibleConn[con] = 'condition';
      }
    },
    error:function() {
      console.log("Error while GET categories information")
    }
  });

  $.ajax({
    url: "/products/paymentMethods",
    type: "GET",
    success: function(paymentMethods) {
      for(pay of paymentMethods){
        possibleFilters.push(pay['name']);
        possibleConn[pay] = 'paymentMethods';
      }
    },
    error:function() {
      console.log("Error while GET categories information")
    }
  });

  console.log(typeof possibleFilters);
  console.log(typeof ['asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd'])

  for (typeOfCategory of possibleCategories){
    console.log("ONCE");
    //console.log(possibleFilters)
    //console.log([{"asdf": "123", "123": "asdf"}, {"asdf": "123", "123": "asdf"}, {"asdf": "123", "123": "asdf"}, {"asdf": "123", "123": "asdf"}, {"asdf": "123", "123": "asdf"}, {"asdf": "123", "123": "asdf"}, {"asdf": "123", "123": "asdf"}, {"asdf": "123", "123": "asdf"}, {"asdf": "123", "123": "asdf"}, {"asdf": "123", "123": "asdf"}])
    //for (filter of possibleFilters){
    for(filter of possibleFilters){
      console.log("TWICE");
      attrID = replaceSpaces(filter);
      
      if(possibleConn[filter] == typeOfCategory) {
        $('#collapse-'+typeOfCategory).append('<label class="filter-categories-label">'+
        filter+'<input class="filter-checkbox" type="checkbox" onchange="updateFilter('+'&apos;'+filter+'&apos;'+')" id="'+replaceSpaces(typeOfCategory)+'-'+attrID+'"></label>');        
      }
    }
  }
  
/*
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

  });*/
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

listFilters();

