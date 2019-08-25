$(".item-preco").mask('000.000.000.000.000,00', {reverse: true});
$(".item-valor-final").mask('000.000.000.000.000,00', {reverse: true});
$("#total-pedido").mask('000.000.000.000.000,00', {reverse: true});
$("#id_desconto").mask('##0,00%', {reverse: true});
$("#id_desconto").click(function(){
    $(this).val("")
})