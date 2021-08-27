module.exports = async function(callback) {
    web3.eth.defaultAccount = ( await ( web3.eth.personal.getAccounts() ) )[0];
    console.log("Inicio")
    try{
        initBalance()
        
        _deploy_milestone_3_ArrayReturnArray = await artifacts.require("Milestone3ArrayReturnArray").deployed();
        
        var i, j;
        for( i = 0; i < 250; i++ ){
            let resultados = Array()
            for( j = 0; j < 20 ; j++ ){
                resultados.push( await run() )
            }
            console.log("execução de numero: " + i )
            write( "../results/milestone_3/crude/array_return_array/" + i + ".dat" , resultados );
        }
    }catch (error) {
        console.log(error)
    }
    console.log("fim")
}

async function run(){
    var result = {}
    result.estagio_1_eth        = await getBalance()
    result.estagio_1_resultado  = await inserirElemento()
    result.estagio_2_eth        = await getBalance()
    result.estagio_2_resultado  = await contarElemento()
    result.estagio_3_eth        = await getBalance()
    result.estagio_3_resultado  = await percorre()
    result.estagio_4_eth        = await getBalance()
    result.estagio_4_resultado  = await percorreConta()
    result.estagio_5_eth        = await getBalance()
    return result
}

async function initBalance(){
    accounts = await web3.eth.getAccounts()
    account = accounts[0]
}

async function getBalance(){
    var result = await web3.eth.getBalance(account) 
    return result
}

async function write( path , json_result ){
    const fs = require('fs')

    fs.writeFile( path, JSON.stringify(json_result, null , 2) , (err) => {
        if (err) throw err;
    })
}

async function inserirElemento(){
    var flag = Math.random() > 0.5 ? true : false 
    await _deploy_milestone_3_ArrayReturnArray.inserirElemento(flag)
    return flag
}

async function contarElemento(){
    await _deploy_milestone_3_ArrayReturnArray.contaElemento()
    return null
}

async function percorre(){
    await _deploy_milestone_3_ArrayReturnArray.percorre()   
    return null
}

async function percorreConta(){
    await _deploy_milestone_3_ArrayReturnArray.percorreConta()
    return null
}
