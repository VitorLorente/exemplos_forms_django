$(".item-preco").mask('000.000.000.000.000,00', {reverse: true});
$(".item-valor-final").mask('000.000.000.000.000,00', {reverse: true});
$("#total-pedido").mask('000.000.000.000.000,00', {reverse: true});
$("#id_desconto").mask('##0,00%', {reverse: true});
$("#id_desconto").click(function(){
    $(this).val("")
})
$('#id_cliente_rg').mask('00.000.000-0', {reverse: true});
$("#id_preco").mask('000.000.000.000.000,00', {reverse: true});

