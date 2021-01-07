const checkbox1 = document.querySelectorAll('.checkbox1')
        for (d = 0; d < checkbox1.length; d++){
            const checked = checkbox1[d]
            checked.onchange = function (e) {
                console.log(e,'event')
                const check_id = e.target.dataset['id']
                const checking = e.target.checked
                fetch('/check/'+check_id,{
                    method : "POST",
                    body : JSON.stringify({
                        'completed' : checking
                    }),
                    headers : {
                        'Content-type' : 'application/json'
                    }
                })

            }
        }