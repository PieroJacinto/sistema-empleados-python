const btnsConfirm = document.querySelectorAll('#btnBorrar') 

if (btnsConfirm.length) {
    for ( const btn of btnsConfirm ) {
        btn.addEventListener("click", event => {
            const resp = confirm("Esta opcion no tiene marcha atrás. ¿Confirma?")
            if (!resp) event.preventDefault()
        })
    }
}