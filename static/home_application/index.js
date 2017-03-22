$(document).ready(function(){
    $("#demo").change(function(){
        var demo = $("#demo").find('option:selected').text();
        $.get('option', function(response){alert(response)});
    });
    $("#upload").click(function(){
        $.ajax({
            url: '/upload',
            type: 'POST',
            cache: false,
            data: new FormData($('#fileForm')[0]),
            processData: false,
            contentType: false,
            success: function(data){
                alert(data);
            },
            error: function(data){
                alert('Please retry');
            }
        });

    });
});