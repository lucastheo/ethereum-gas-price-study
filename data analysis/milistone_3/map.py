import json
import multiprocessing.dummy
import matplotlib.pyplot as plt

pool = multiprocessing.dummy.Pool(1)

def carrega_lista_domain():
    estagio_ordem = ['estagio_inserir_elemento' , 'estagio_contar_elemento' , 'estagio_percorre' , 'estagio_percorre_conta' , 'estagio_final']
    def carregar_arquivos():
        lista_dto_arquivo = list()
        for i in range(188):
            arq = open(f"../../results/milestone_3/map/{i}.dat")
            lista_dto_arquivo += json.load(arq)
        return lista_dto_arquivo
    def mapping_lista_dto_arquivo_to_lista_domain(lista_dto_arquivo):
        return pool.map(mapping_dto_arquivo_to_domain , lista_dto_arquivo)

    def mapping_dto_arquivo_to_domain(dto_arquivo):
        domain = dict()
        domain['estagio_ordem'] = estagio_ordem
        for estagio in domain['estagio_ordem']:
            domain[estagio] = dict() 

        domain['estagio_inserir_elemento']['eth'] = int(dto_arquivo['estagio_1_eth'])
        domain['estagio_inserir_elemento']['resultado'] = dto_arquivo['estagio_1_resultado']

        domain['estagio_contar_elemento']['eth'] = int(dto_arquivo['estagio_2_eth'])
        domain['estagio_contar_elemento']['resultado'] = dto_arquivo['estagio_2_resultado']

        domain['estagio_percorre']['eth'] = int(dto_arquivo['estagio_3_eth'])
        domain['estagio_percorre']['resultado'] = dto_arquivo['estagio_3_resultado']
        
        domain['estagio_percorre_conta']['eth'] = int(dto_arquivo['estagio_4_eth'])
        domain['estagio_percorre_conta']['resultado'] = dto_arquivo['estagio_4_resultado']

        domain['estagio_final']['eth'] = int(dto_arquivo['estagio_5_eth'])

        return domain

    lista_dto_arquivo = carregar_arquivos()
    return mapping_lista_dto_arquivo_to_lista_domain(lista_dto_arquivo)

def calcula_gasto_eth( lista_domain ):
    def calcula_gasto_eth_estagio_atual_proximo( domain , estagio_i ):
        estagio_atual = domain[domain['estagio_ordem'][estagio_i]]
        estagio_proximo = domain[domain['estagio_ordem'][estagio_i+1]]
        estagio_atual['gasto'] = int(estagio_atual['eth'])/10**9 - int(estagio_proximo['eth'])/10**9

    def calcula_gasto_eth_estagio( domain ):
        for estagio_i in range( len( domain['estagio_ordem'] ) - 1 ):
            calcula_gasto_eth_estagio_atual_proximo( domain , estagio_i )

    def calcula_gasto_eth_total( domain ):
        estagio_inicial = domain[domain['estagio_ordem'][0]]
        estagio_final = domain[domain['estagio_ordem'][-1]]
        domain['gasto_total'] = (estagio_inicial['eth'])/10**9 - (estagio_final['eth'])/10**9    
    
    pool.map( calcula_gasto_eth_total , lista_domain)
    pool.map( calcula_gasto_eth_estagio , lista_domain)
    

def captura_identificacao( lista_domain ):
    def captura_identificacao( domain ):
        domain['identificacao'] = domain['estagio_contar_elemento']['resultado']
    pool.map( captura_identificacao , lista_domain)


def sumariza_gasto_por_estagio( lista_domain ):
    def calcula_gasto_por_estagio_separa_dados( domain ):
        contagem = list()
        for estagio in domain['estagio_ordem'][:-1]:
            contagem.append( domain[estagio]['gasto'] )
        return contagem
    
    def calcula_gasto_por_estagio( lista_estagios ):
        toda_contagem = list()
        for _ in range( len( lista_estagios[0] )):
            toda_contagem.append(0)
        
        for contagem in lista_estagios:
            for i in range( len( toda_contagem ) ):
                toda_contagem[ i ] += contagem[ i ] 
        return toda_contagem
    
    def merge_estagios_contagem( toda_contagem , estagios):
        merge = dict()
        for i in range( len( estagios)-1):
            merge[estagios[i]] = toda_contagem[i]
        return merge

    toda_contagem = pool.map( calcula_gasto_por_estagio_separa_dados , lista_domain )
    print("gasto de gas para cada estágio:" , merge_estagios_contagem ( calcula_gasto_por_estagio( toda_contagem ) , lista_domain[0]['estagio_ordem'] ) ) 

def gera_grafico_custo_processamento_execucao(lista_domain):
    def get_gasto_total(domain): 
        return domain['gasto_total']
    
    def get_identificacao(domain): 
        return domain['identificacao']

    def map_gasto_total(lista_domain):
        return pool.map(get_gasto_total , lista_domain)
    
    def map_identificacao(lista_domain):
        return pool.map(get_identificacao , lista_domain)

    def normalizador_gasto_total( maximo , gasto_total ):
        return float(gasto_total)/float(maximo)

    def normaliza_gasto_total( lista_gasto_total ):
        max_lista_gasto_total = max( lista_gasto_total )
        return pool.map(lambda gasto_total:normalizador_gasto_total( max_lista_gasto_total , gasto_total ) , lista_gasto_total )

    def construir_grafico( x, y ):
        plt.scatter(x,y)
        plt.show()

    lista_gasto_total = map_gasto_total(lista_domain)
    #lista_normalizada_gasto_total = normaliza_gasto_total(lista_gasto_total)
    lista_identificacao = map_identificacao(lista_domain)

    construir_grafico(lista_identificacao,lista_gasto_total)

if __name__ == '__main__':
    lista_domain = carrega_lista_domain()
    calcula_gasto_eth(lista_domain)
    captura_identificacao(lista_domain)
    sumariza_gasto_por_estagio(lista_domain)
    gera_grafico_custo_processamento_execucao(lista_domain)