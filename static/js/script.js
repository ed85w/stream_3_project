/**
 * Created by Ed on 25/09/2017.
 */

 $(document).ready(function(){

    // sidebar button toggle
    $('.sidebarBtn').click(function(){
        $('.sidebar').toggleClass('active')
        $('.sidebarBtn').toggleClass('toggle')
    })

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


    $('#checkout-btn').click(confirmBasket);

    $('#shop-rtn-btn').click(continueShopping);



});

// function to create JSON copy of current basket
function getBasketJson(){

    // get values of each cell in table
    var things = [];
    $('#basket-table .input-value').each(function() {
        var tableVal = $( this ).val();
        var tableData = $( this ).text();
        // remove £ sign if required
        tableData = tableData.replace('£','');
        things.push(tableVal);
        things.push(tableData)
    });

    // filter out blanks from things array
    things = things.filter(function(e){return e});

    //get length of array and calcullate number of products in basket
    var arrayLen = things.length;
    // var numProducts = arrayLen/5;

    var basket = {};
    for (var i=0; i < arrayLen; i+=5){
        // var productObject = {};
        var prodID = things[i];
        basket[prodID] = {
            product_title: things[i+1],
            product_price: things[i+2],
            quantity: things[i+3],
            subtotal: things[i+4],
        };

    }

    // console.log(basket);
    var jsonDATA = JSON.stringify(basket);
    return jsonDATA

};

function confirmBasket() {
    var basket = getBasketJson();
    $.post("/confirm_basket/", basket)
        .done(function goToURL() {
            location.href = '/confirm_basket/';
    });
}

function continueShopping() {
    var basket = getBasketJson();
    $.post("/continue_shopping/", basket)
        .done(function goToURL() {
            location.href = '/continue_shopping/';
    });
}

