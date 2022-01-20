$(document).ready(function(){

    // alert('gre');
    increment_value();
    decreament_value();
    remote_cart();
    getTotal();
    checkout_totals();

    // $('.ClickedMessage').on('click', function(){
    //     const message = $('.m').attr('value');

    //     alert(message);
    // });

    // // $(this).click(function(){
    // //     alert('yh');
    // // });

    
    
});


function increment_value(){
    $('.up').click(function (){
        var id = $(this).data('id');

        var price = $(this).data('price');
        
        var quantity = $('#'+id+'').val();
        quantity = parseInt(quantity) + 1;
        
        $('#'+id+'').val(quantity);
        // alert(quantity);
        


        increment_cart(id);
        var total = price * quantity

        $('#total'+id+'').html(total.toLocaleString());

        getTotal();
    });
}
function decreament_value(){
    $('.down').click(function (){
        var id = $(this).data('id');
        var price = $(this).data('price');

        var quantity = $('#'+id+'').val();
        if (quantity > 1){
            quantity = parseInt(quantity) - 1;
            $('#'+id+'').val(quantity);
            
        }
        
        decrement_cart(id);
        var total = price * quantity
        $('#total'+id+'').html(total.toLocaleString());
        getTotal();
        
    });
}

function increment_cart(id){
    $.ajax({
        url: '/cart/increment/'+id+' ',
        
        dataType: 'json',
        success: function (response) {
            var msg = response.message
            if (msg == "success"){
                // getTotal();
                // alert('success');
            }
            
        }
    });
}


function decrement_cart(id){
    $.ajax({
        url: '/cart/decrement/'+id+' ',
        
        dataType: 'json',
        success: function (response) {
            if (response.message = 's') {
            
            }
        }
    });
}


function remote_cart(){
    $('.clear-cart').click(function (){
        if ( confirm("are you sure?") ){

            var id = $(this).data('id');
    
            $.ajax({
                url: '/cart/clear/'+id+' ',
                
                dataType: 'json',
                success: function (response) {
                    if (response.message = 'success') {
                        location.reload();
                    }
                }
            });
        }

    });

}


function getTotal(){
    var total_amount = 0
    $('.total_amount').each(function(i, obj) {
        var total =$(this).html();
        var a = parseInt(total.replace(/,/g, ""))
        var b = parseInt(total_amount)
        var t = b + a;
        total_amount = t;
        // alert(total_amount);
        
    });
    
    $('#subtotal').html(total_amount.toLocaleString());
    $('#totals').html(total_amount.toLocaleString());

    // alert(total_amount);

}

function checkout_totals(){
    var total_amount = 0
    $('.checkout_totals').each(function(i, obj) {
        var total =$(this).html();
        var a = parseInt(total.replace(/,/g, ""))
        var b = parseInt(total_amount)
        var t = b + a;
        total_amount = t;
        
        // alert(total_amount.toLocaleString());
        
    });

    // $('#subtotal').html(total_amount);
    // $('#totals').html(total_amount);
    $('#checkout_total').html(total_amount.toLocaleString());

    // alert(total_amount);
}

