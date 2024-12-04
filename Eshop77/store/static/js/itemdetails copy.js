

    $(document).ready(function () {
      
      // add to cart

      $('.adddcartbutn').click(function(){
      //submit form
       item_rating=$('.checked').length
       

      });

      var viewimg = $('.viewitem').attr('src')
      
      // size guide .. **change it to new image**
      $('.itemsize-text').click(function(){
        $('.viewitem').attr('src', "https://cdn.shopify.com/s/files/1/2374/2011/files/Cortazu_sizechart_Mens_CM_df704e89-0803-4a3b-aa02-d01b4c30c582.png?v=1594990748");

        // 
       })


      $('.thumbimg').hover(function () {
        $('.viewitem').attr('src', $(this).attr('src'));
      }


      );

      $('.rating').click(function () {
        var star_rating = []
        star_rating = $(this).attr('class');
       
        
        if (!star_rating.includes('checked')) {
          $(this).attr('class', 'fa fa-star rating checked');
          
        } else {
          
          $(this).attr('class', 'fa fa-star rating uncheck');
        }
      });

      /* $('.thumbimg').click(function(){
        $('.viewitem').attr('src',$(this).attr('src'));
    
    
       });*/

      //in the search pincode remove old text 'item available'
      const rem_availtxt = document.querySelector('.checkavailtext');
      rem_availtxt.onkeyup = (e) => {

        $('#availibilitytext').text('');
        $('#addcitytext').text('');
      }


      //code to expand the prod description , return policy and offers on click

      $('.returnpolicon').click(function () {

         
        if ($('.returnpolicon').text() == '-') {
          $('.returnpoldetails').attr('style', 'display:none');
          $('.returnpolicon').text('+');
        }
        else {
          $('.returnpolicon').text('-');
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
        if ($('.proddescicon').text() == '-') {
          $('.proddescdetails').attr('style', 'display:none');
          $('.proddescicon').text('+');

        }
        else {
          $('.proddescicon').text('-');
          $('.offertxticon').text('+');
          $('.returnpolicon').text('+');
          $('.offertxtdetails').attr('style', 'display:none');
          $('.returnpoldetails').attr('style', 'display:none');
          $('.offersrow').attr('style', 'heigth:2rem');
          $('.returnrow').attr('style', 'heigth:2rem');
          $('.proddesrow').attr('style', 'heigth:5em');
          $('.proddescdetails').attr('style', 'display:block');

        }
      });

      $('.offertxticon').click(function () {
        if ($('.offertxticon').text() == '-') {
          $('.offertxtdetails').attr('style', 'display:none');
          $('.offertxticon').text('+');

        }
        else {
          $('.offertxticon').text('-');
          $('.returnpolicon').text('+');
          $('.proddescicon').text('+');
          $('.proddescdetails').attr('style', 'display:none');
          $('.returnpoldetails').attr('style', 'display:none');
          $('.proddesrow').attr('style', 'heigth:2rem');
          $('.returnrow').attr('style', 'heigth:2rem');
          $('.offersrow').attr('style', 'heigth:5em');
          $('.offertxtdetails').attr('style', 'display:block');
        }


      });

    });





    //js to calculate distance



    // $('#checkavaildis').click(get_distance);
    $('#checkavaildis').click(function () {

      if ($('.checkavailtext').val().trim().length == 6) {

        var pincode = $('.checkavailtext').val().trim();


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
              city=response.split('-')[3];

              if (d < 20) {
                $('#availibilitytext').text('Item is available');
                $('#addcitytext').text(place + ', ' + city+','+state);
                $('#availibilitytext').attr('style', 'color:green');
              }
              else {
                $('#addcitytext').text(place + ', ' + state);
                $('#availibilitytext').text('Item not available');
                $('#availibilitytext').attr('style', 'color:red');
              }


            }
          }
        );
        ///////////////



      }
      else {
        $('#availibilitytext').text('pincode length should be 6');
        $('#availibilitytext').attr('style', 'color:red');

      }
    });

 