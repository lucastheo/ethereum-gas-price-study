module.exports = async function(callback) {
    console.log("Inicio")
    
    try{
        teste1_Escrita = await artifacts.require("Teste1Escrita").deployed();  //captura o contrato

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

            write( "./teste_resultado/teste_1/escrita/" + i + ".dat" , resultados );
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
    teste.estagio_2_execucao_resultado = await testeEscrevendoAdicionandoElemento()
    
    teste.estagio_3_eth = await getBalance()
    teste.estagio_3_execucao_resultado = await testeEscrevendoCalculandoTask()    
    
    teste.estagio_4_eth = await getBalance()
    return teste 
   
}

async function testeEscrevendoAdicionandoElemento(){
    try{
        await teste1_Escrita.createTask("Teste 1")
    }catch(error){
        console.log(error)
        return false
    }
    return true
}

async function testeEscrevendoCalculandoTask(){
    taskCount = await teste1_Escrita.taskCount()
    return taskCount.toNumber()
}

/*
    Loga a quantidade de ETH presente na conta
*/

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

    fs.writeFile( path, JSON.stringify(json_result, null , 2) , (err) => {
        // In case of a error throw err.
        if (err) throw err;
    })
}