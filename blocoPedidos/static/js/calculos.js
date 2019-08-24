$("select").on("change", function(){
    var preco = $(this).find("option:selected").attr("preco");
    var preco_antigo = $(this).parent().next().next().children(".item-valor-final").val()
    console.log(preco_antigo)
    if(!preco_antigo){
        preco_antigo = 0;
    }
    if(!preco){
        preco = 0;
    }
    $(this).parent().next().children(".item-preco").val(preco);

    var quantidade = $(this).parent().prev().children("input[type=text]").val();

    if(quantidade && quantidade > 0){
        var preco_total = quantidade * preco;
        $(this).parent().next().next().children(".item-valor-final").val((preco_total).toFixed(2))
        var total = $("#total-pedido").html()
        $("#total-pedido").html((parseFloat(total)+parseFloat(preco_total)-parseFloat(preco_antigo)).toFixed(2))
    }
})

$(".input-quantidade").on("keyup", function(){
    var quantidade = $(this).val();
    console.log("quantidade", quantidade)
    var preco_antigo = $(this).parent().next().next().next().children(".item-valor-final").val()
    if(!preco_antigo){
        preco_antigo = 0
    }
    console.log(preco_antigo)
    var preco = $(this).parent().next().find("option:selected").attr("preco");
    console.log(preco)
    if(preco && preco > 0){
        var total = $("#total-pedido").html()
        console.log(total)
        var preco_total = quantidade * preco
        console.log(preco_total)
        $(this).parent().next().next().next().children(".item-valor-final").val((preco_total).toFixed(2))
        $("#total-pedido").html((parseFloat(total)+parseFloat(preco_total)-parseFloat(preco_antigo)).toFixed(2))
    }
})