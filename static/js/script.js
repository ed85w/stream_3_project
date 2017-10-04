/**
 * Created by Ed on 25/09/2017.
 */
$(document).ready(function() {


    $(".nav-item").click(function(){

        var pageId = $(this).attr("id").substring(0,9); //gets class name of element clicked
        alert(pageId + "hello");
        $('#home-back').removeClass();
        $('#home-back').addClass(pageId);

    });

});