$(document).ready(function(){

    // alert('gre');
    ProductDeleteConfirm();
    CloseAlertAfterSeconds();

    viewcontent();
    description();
});


function ProductDeleteConfirm(){
    $('.delete-product').click(function(){
        var id = $(this).data('id');

        // alert(id);
        $('#confirm_delete_product').val(id);
    });
}

function description(){
    $('.description').click(function(){
        var message = $(this).data('info');
        $('#LargeContent .modal-body').html(message);
        // alert(id)
    });
}
function viewcontent(){
    $('.largemessage').click(function(){
        var msg = $(this).data('message');
        $('#LargeContent .modal-body').text(msg);
        // $.ajax({
        //     url: 'product/content/'+id+' ',
            
        //     dataType: 'json',
        //     success: function (response) {
        //         $('#LargeContent .modal-body').text(response.description);
                
        //     }
        // });
    }); 
}

function CloseAlertAfterSeconds(){
    // $("#success-alert").fadeTo(3000, 1000).slideUp(1000, function(){
    //     // $("#success-alert").slideUp(800);
    // });

    $('#success-alert').slideDown(1000,'swing',function(){
        setTimeout(function() {
            $('#success-alert').slideUp(1000);
        }, 4000);
    })
    
}
