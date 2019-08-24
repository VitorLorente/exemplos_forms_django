$(".excluir-item").click(function(){
    var item_pk = $(this).attr("value");
    console.log(item_pk)
    $.post("/pedido/remover-item",
    {
        'pk': item_pk,
        'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value
    },
    );
    location.reload();
});