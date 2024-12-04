
$(document).ready( function () {
  
   $(".addtofav").click(function(){

  
   var productid = $(this).attr("id").split('-')[1];
  
    // make it one function in js and one class and id in index.html
   $.ajax(
    {
      url: 'add_favourite',
      type: 'get',
      data: {
        productid: productid
    
      },
     
      success: function (response) {
      console.log(response['login_error']);
      if (response['login_error'] == 'none'){
        $('#fav-' + productid).attr("src","static/undofav.svg");
        $('#fav-' + productid).attr("class","remfromfav");
        $('#fav-' + productid).attr("id","rfav-"+productid);
        $('#addfavtext-' + productid).html('In Wishlist');
      }
      else{
        //addfavtext

        $('#addfavtext-' + productid).html('<b>Not logged in</b>');

      }
       
      
         
        
      }

    }
  );
 


   });

   $(".remfromfav").click(function(){
    
    var productid = $(this).attr("id").split('-')[1];
  
    $.ajax(
     {
       url: 'rem_favourite',
       type: 'get',
       data: {
         productid: productid
     
       },
      
       success: function (response) {
         //console.log('/#' + productid, response);
         $('#rfav-' + productid).attr("src","static/favorite.svg");
         $('#rfav-' + productid).attr("class","addtofav");
         $('#rfav-' + productid).attr("id","fav-"+productid);
         $('#addfavtext-' + productid).html('Wishlist');
         
         
       }
 
     }
   );
  
 
 
    });


});

 