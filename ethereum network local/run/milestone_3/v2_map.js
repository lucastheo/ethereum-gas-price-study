module.exports = async function(callback) {

    try{
        
        _deploy_milestone_3_Map = await artifacts.require("Milestone3Map").deployed();
        
        var i, j;
        for( i = 0; i < 500; i++ ){
            let resultados = Array()
            for( j = 0; j < 20; j++ ){
                resultados.push( await run() )
            }
            console.log("execução de numero: " + i )
            write( "../results/milestone_3/crude/map/" + i + ".dat" , resultados );
        }
    }catch (error) {
        console.log(error)
    }
    console.log("fim")
}

async function run(){
    var result = Array()
    var estagio_1 = {}
    
    estagio_1.result = await inserirElemento()
    estagio_1.function_name = "inserirElemento"
    result.push( estagio_1 )

    var estagio_2 = {}
    estagio_2.result = await contarElemento()
    estagio_2.function_name = "contarElemento"
    result.push( estagio_2 )

    var estagio_3 = {}
    estagio_3.result = await percorre()
    estagio_3.function_name = "percorre"
    result.push( estagio_3 )

    var estagio_4 = {}
    estagio_4.result = await percorreConta()
    estagio_4.function_name = "percorreConta"
    result.push( estagio_4 )

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
    await _deploy_milestone_3_Map.inserirElemento(flag )
    return flag
}

async function contarElemento(){
    var result;
    await _deploy_milestone_3_Map.contaElemento()
    return null
}

async function percorre(){
    await _deploy_milestone_3_Map.percorre()
    return null
}

async function percorreConta(){
    await _deploy_milestone_3_Map.percorreConta()
    return null
}
