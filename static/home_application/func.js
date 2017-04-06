






$(document).ready(function(){
    function renderTpl1(str, cfg) {
        var re = /#(.+?)#/g;
        return str.replace(re, function() {
            var val = '';
            if (arguments[1] == 'pk'){
               val = val + cfg['pk'] + '';

            }
            if (arguments[1] == 'link') {
                val = val + cfg['fields']['link'] + '';

            }
            if (arguments[1] == 'title') {
                val = val + cfg['fields']['title'] + '';
            }
            return val
        });
    }




    $('#refresh').click(function(){
        $.ajax({
            url: '/refresh',
            type: 'get',
            cache: true,
            success: function(res){
                var _html = ' ';
                var list = res;
                var header_tpl = $('#header_tpl').html();
                var tpl = $('#tpl').html();
                res.length = 10;
                for (var i=0, len=res.length; i < len; i++){
                    var item = res[i];
                    _html += renderTpl1(tpl, item);
                }
                $('.ranger-box2 tbody').html(_html);
            }

        });
    });


    $('#search').click(function(){
        var title = $('#searchTitle').val()
        $.ajax({
            url: '/search',
            type: 'get',
            cache: true,
            data: {'title':title},
            success: function(res){
                alert('There are '+res.length+' records matched');

            }
        });
    });


})

function submit(e){
    var pk = e.id;
    pk = pk.replace(/s/g, '');
    var level = $("#"+pk+'l').val();
    $.ajax({
        url: '/fav',
        type: 'post',
        cache: true,
        data: {'pk':pk, 'level':level},
        success: function(res){
            $('#'+pk+'t').attr('color','red');
        }
    });
};

function rem(e){
    var pk = e.id;
    pk = pk.replace(/r/g, '');
    var level = $("#"+pk+'l').val();
    $.ajax({
        url: '/rem',
        type: 'post',
        cache: true,
        data: {'pk':pk},
        success: function(res){
            $('#'+pk+'l').val('');
        }
    });
};

