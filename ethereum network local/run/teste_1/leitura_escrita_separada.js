module.exports = async function(callback) {
    console.log("Inicio")
    
    try{
        teste1_LeituraEscritaJunta = await artifacts.require("Teste1EscritaLeituraEscritaSeparada").deployed();  //captura o contrato

        accounts = await web3.eth.getAccounts()
        account = accounts[0]
        
        var i, j;
        for( i = 0; i < 25; i++ ){
            
            let resultados = Array()
            for( j =0; j < 200 ; j++){
                if( j % 25 == 0){
                    console_log("Valor de i " + i + " e j " + j )
                }
                resultados.push( await testeEscrevendo() )
            }

            write( "./teste_resultado/teste_1/leitura_escrita_separada/" + i + ".dat" , resultados );
        }
    }catch (error) {
        console.log(error)
    }

    console.log("Fim")
    await log_balance(acs)
    process.exit()
    
}

async function testeEscrevendo(){
    var teste = {}; 
    teste.estagio_1_eth = await getBalance()
    teste.estagio_1_execucao_resultado = await testeEscrevendoCalculandoTask()
    
    teste.estagio_2_eth = await getBalance()
    teste.estagio_2_execucao_resultado = await testeCalculandoJ()

    teste.estagio_3_eth = await getBalance()
    teste.estagio_3_execucao_resultado = await testeEscrevendoAdicionandoElemento3(teste.estagio_2_execucao_resultado)

    teste.estagio_4_eth = await getBalance()
    teste.estagio_5_execucao_resultado = await testeEscrevendoCalculandoTask()    
    
    teste.estagio_4_eth = await getBalance()
    return teste 
   
}
async function testeCalculandoJ(){
    return await teste1_LeituraEscritaJunta.contJ()
}


async function testeEscrevendoAdicionandoElemento3( j ){
    try{
        await teste1_LeituraEscritaJunta.createTask3("Teste 1" , j )
    }catch(error){
        console.log(error)
        return false
    }
    return true
}

async function testeEscrevendoCalculandoTask(){
    taskCount = await teste1_LeituraEscritaJunta.taskCount()
    return taskCount.toNumber()
}


async function testeCalculandoJ(){
    var result;
    var v = await teste1_LeituraEscritaJunta.contJ.call(
        function(err, res){ 
            result = res 
        } 
    )
    return result
}

async function getBalance(){
    return web3.eth.getBalance(account) 
}

async function log_balance(){
    return ("\t(Quantidade de ETH: " + await getBalance() + ")")
}

async function console_log( str ){
    b = await log_balance()
    console.log( b + " " +  str )
}

async function write( path , json_result ){
    const fs = require('fs')
    console.log(path)
    fs.writeFile( path , JSON.stringify(json_result, null , 2) , (err) => {
        // In case of a error throw err.
        if (err) throw err;
    })
}