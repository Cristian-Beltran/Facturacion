let grupo_select = document.getElementById('grupo');
let cliente_select = document.getElementById('cliente');

grupo_select.onchange = function() {
    grupo = grupo_select.value;
    fetch('/_get_cliente/'+ grupo).then(function(response){
        response.json().then(function(data){
            let optionHTML = '';
            for (let cliente of data.clientes){
                optionHTML += '<option value="'+ cliente.id + '">'+ cliente.name+ '</option>';
            }
            cliente_select.innerHTML = optionHTML;
        });
    });
}
