let grupo_select = document.getElementById('grupo');
let cliente_select = document.getElementById('cliente');
let cedula = document.getElementById('no_ruc');
let nombre = document.getElementById('nbr_cliente');


grupo_select.onchange = function() {
    grupo = grupo_select.value;
    cedula.value = "";
    nombre.value = "";
    fetch('/_get_clientes/' + grupo).then(function(response){
        response.json().then(function(data){
            let optionHTML = '';
            for (let cliente of data.clientes){
                optionHTML += '<option value="'+ cliente.id + '">'+ cliente.name+ '</option>';
            }
            cliente_select.innerHTML = optionHTML;
        });
    });
}

cliente_select.onchange = function(){
    cedula.value = "";
    nombre.value = "";
}

cedula.onfocus = function(){
    cliente = cliente_select.value;
    fetch('/_get_cliente/' + cliente ).then(function(response){
        response.json().then(function(data) {
            cedula.value = data.cedula;
            nombre.value = data.nombre;
        });
    });
}

