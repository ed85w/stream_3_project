/**
 * Created by Ed on 25/09/2017.
 */
$(document).ready(function(){

    // function to update basket subtotals and total when number of items changes
    $('table tr td input').on('input', function() {
        var id = $(this).attr('id').substring(16,17);
        var price = parseFloat($('#' + 'basket-itm-price' + id).text().substring(1,7));
        var quantity = $('#' + 'basket-qty-input' + id).val();
        var currSubtotal = parseFloat($('#' + 'basket-itm-subtotal' + id).text().substring(1,7));
        var newSubtotal = parseFloat(price * quantity).toFixed(2);
        var difference = parseFloat(newSubtotal - currSubtotal);
        var currTotal = parseFloat($('#basket-total').text().substring(1,7));
        var newTotal = parseFloat(currTotal + difference).toFixed(2);
        $('#' + 'basket-itm-subtotal' + id).html('£'+ newSubtotal);
        $('#basket-total').html('£' + newTotal);
        console.log("current total is" + currTotal);
        console.log("diff is" + difference);
        console.log("new total is" + newTotal);
    });

    //function for remove from basket button
    $('table tr td button').on('click', function(){
        var id = $(this).attr('id').substring(3,4);
        var row = $('#row'+id);
        var currSubtotal = parseFloat($('#' + 'basket-itm-subtotal' + id).text().substring(1,7));
        var currTotal = parseFloat($('#basket-total').text().substring(1,7));
        var newTotal = parseFloat(currTotal - currSubtotal).toFixed(2);
        row.remove();
        $('#basket-total').html('£' + newTotal);
    });

    $('#checkout-btn').on('click', function() {


    });


});