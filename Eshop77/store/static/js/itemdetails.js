

$(document).ready(function () {
  

  //code to bring back main image in modal main image
  var viewimg = $('.viewitem').attr('src');
  $('.card-img-top').click(function () {
    
    var img_prodid = $(this).attr('src');
    
 
    $('.viewitem').attr('src', img_prodid);
    
    $('.offertxtdetails').attr('style', 'display:none');
    $('.returnpoldetails').attr('style', 'display:none');
    $('.proddescdetails').attr('style', 'display:none');
   

  });

  // size guide .. **change it to new image** //
  $('.itemsize-text').click(function () {

   $('.viewitem').attr('src', "https://cdn.shopify.com/s/files/1/2374/2011/files/Cortazu_sizechart_Mens_CM_df704e89-0803-4a3b-aa02-d01b4c30c582.png?v=1594990748");


  });


  $('.thumbimg').hover(function () {
    $('.viewitem').attr('src', $(this).attr('src'));
  });

  $('.thumbimg').click(function () {
    $('.viewitem').attr('src', $(this).attr('src'));
  });


  /* 5 start Rating to be added later */
  
  //   $('.rating').click(function () {
  //     var star_rating = []
  //     star_rating = $(this).attr('class');


  //     if (!star_rating.includes('checked')) {
  //       $(this).attr('class', 'fa fa-star rating checked');

  //     } else {

  //       $(this).attr('class', 'fa fa-star rating uncheck');
  //     }
  //   });



  //in the search pincode remove old text 'item available'

  $('.checkavailtext').keyup(function (event) {
    var avail_txt = $(this).attr('id');
    prod_id = avail_txt.split('-')[1];

    $('#availibilitytext-' + prod_id).text('');

    $('#addcitytext-' + prod_id).text('');


  });




  //   //code to expand the prod description , return policy and offers on click

    $('.returnpolicon').click(function () {

      var returnpolid = $(this).attr('id');
      prod_id = returnpolid.split('-')[1];


      if ($('#returnpolicon-'+prod_id).text() == '-') {
        $('.returnpoldetails').attr('style', 'display:none');
        $('.returnpolicon').text('+');
      }
      else {
        $('#returnpolicon-'+prod_id).text('-');
        $('.proddescicon').text('+');
        $('.offertxticon').text('+');


        $('.offertxtdetails').attr('style', 'display:none');
        $('.proddescdetails').attr('style', 'display:none');
        $('.offersrow').attr('style', 'heigth:2rem');
        $('.proddesrow').attr('style', 'heigth:2rem');
        $('.returnrow').attr('style', 'heigth:5em');
        $('.returnpoldetails').attr('style', 'display:block');
        $('.returnpoldetails').attr('class', 'returnpoldetails collapsedetails');

      }

    });

    $('.proddescicon').click(function () {

      var proddescid = $(this).attr('id');
      prod_id = proddescid.split('-')[1];

      if ($('#proddescicon-'+prod_id).text() == '-') {
        $('.proddescdetails').attr('style', 'display:none');
        $('.proddescicon').text('+');

      }
      else {
        $('#proddescicon-'+prod_id).text('-');
        $('.offertxticon').text('+');
        $('.returnpolicon').text('+');
        $('.offertxtdetails').attr('style', 'display:none');
        $('.returnpoldetails').attr('style', 'display:none');
        $('.offersrow').attr('style', 'heigth:2rem');
        $('.returnrow').attr('style', 'heigth:2rem');
        $('.proddesrow').attr('style', 'heigth:5em');
        $('.proddescdetails').attr('style', 'display:block');
       // $('.proddescdetails').attr('class', 'proddescdetails collapsedetails');

      }
    });

    $('.offertxticon').click(function () {
      var offertxtid = $(this).attr('id');
      prod_id = offertxtid.split('-')[1];
      

       
      if ($('#offertxticon-'+prod_id).text() == '-') {
        $('.offertxtdetails').attr('style', 'display:none');
        $('.offertxticon').text('+');

      }
      else {
        $('#offertxticon-'+prod_id).text('-');
        $('.returnpolicon').text('+');
        $('.proddescicon').text('+');
        $('.proddescdetails').attr('style', 'display:none');
        $('.returnpoldetails').attr('style', 'display:none');
        $('.proddesrow').attr('style', 'heigth:2rem');
        $('.returnrow').attr('style', 'heigth:2rem');
        $('.offersrow').attr('style', 'heigth:5em');
        $('.offertxtdetails').attr('style', 'display:block');
        //$('.offertxtdetails').attr('class', 'offertxtdetails collapsedetails');
      }


    });

});


 
// js to calculate distance between pincode and the nearest store  

$('.checkavailbutn').click(function () {
  var avail_id = $(this).attr('id');
  prod_id = avail_id.split('-')[1];



  if ($('#checkavailtext-' + prod_id).val().trim().length == 6) {

    var pincode = $('#checkavailtext-' + prod_id).val().trim();


    //////////////////
    $.ajax(
      {
        url: 'searchloc',
        type: 'get',
        data: {
          zipcode: pincode
        },
        success: function (response) {
          console.log(response);
          place = response.split('-')[0];

          state = response.split('-')[1];
          d = response.split('-')[2];
          city = response.split('-')[3];

          if (d < 20) {
            $('#availibilitytext-' + prod_id).text('Item is available');
            $('#addcitytext-' + prod_id).text(place + ', ' + city + ',' + state);
            $('#availibilitytext-' + prod_id).attr('style', 'color:green');

            
            
          }
          else {
            $('#addcitytext-' + prod_id).text(place + ', ' + state);
            $('#availibilitytext-' + prod_id).text('Item not available');
            $('#availibilitytext-' + prod_id).attr('style', 'color:red');
            
            // disable the add to cart button

          }


        }
      }
    );
    ///////////////



  }
  else {
    $('#availibilitytext-' + prod_id).text('pincode length should be 6');
    $('#availibilitytext-' + prod_id).attr('style', 'color:red');
    // addcartclasses=$('#prod-'+prod_id).attr('class');
    // $('#prod-'+prod_id).attr('class',addcartclasses+' disabled');

  }

});

