module.exports = async function(callback) {
    web3.eth.defaultAccount = ( await ( web3.eth.personal.getAccounts() ) )[0];
    console.log("Inicio")
    try{
        initBalance()
        
        _deploy_milestone_3_MapReturnArray = await artifacts.require("Milestone3MapReturnArray").deployed();
        
        var i, j;
        for( i = 0; i < 500; i++ ){
            let resultados = Array()
            for( j = 0; j < 20; j++ ){
                resultados.push( await run() )
            }
            console.log("execução de numero: " + i )
            write( "../results/milestone_3/map_return_array/" + i + ".dat" , resultados );
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
    await _deploy_milestone_3_MapReturnArray.inserirElemento(flag)
    return flag
}

async function contarElemento(){
    var result;
    await _deploy_milestone_3_MapReturnArray.contaElemento.call(
        function(err, res){ result = res } 
    )
    return result
}

async function percorre(){
    await _deploy_milestone_3_MapReturnArray.percorre.call(
        function(err, res){ result = res }
    )
    return result
}

async function percorreConta(){
    await _deploy_milestone_3_MapReturnArray.percorreConta.call(
        function(err, res){ 
            result = res
        }
    )
    return result
}