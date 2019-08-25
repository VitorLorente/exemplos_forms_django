$(".excluir-item").click(function(){
    var item_pk = $(this).attr("value");
    $.post("/pedido/remover-item/",
    {
        'pk': item_pk,
        'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value
    },
    );
    location.reload();
});

$("#lancar-desconto").click(function(){
    var pedido_pk = $("input[name='id-pedido']").val();
    var desconto = $("input[name='desconto']").val();
    $.post("/pedido/lancar-desconto/",
    {
        'pk': pedido_pk,
        'desconto': desconto,
        'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value
    },
    );
    location.reload();
});