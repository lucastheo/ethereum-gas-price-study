import json
import multiprocessing.dummy
import matplotlib.pyplot as plt

pool = multiprocessing.dummy.Pool(24)

def carrega_lista_domain():
    def carregar_arquivos():
        lista_dto_arquivo = list()
        for i in range(22):
            arq = open(f"./data/ler_escrever/{i}.teste_para_escrever_ler.dat")
            lista_dto_arquivo += json.load(arq)
        return lista_dto_arquivo


    def mapping_lista_dto_arquivo_to_lista_domain(lista_dto_arquivo):
        return pool.map(mapping_dto_arquivo_to_domain , lista_dto_arquivo)

    def mapping_dto_arquivo_to_domain(dto_arquivo):
        domain = dict()
        domain['gasto_total'] = (int(dto_arquivo['estagio_4_eth'] ) - int(dto_arquivo['estagio_1_eth'] ))*-1
        domain['gasto_escrita'] = (int(dto_arquivo['estagio_3_eth'] ) - int(dto_arquivo['estagio_2_eth'] )) *-1
        domain['identificacao'] = int(dto_arquivo['estagio_1_execucao_resultado'])
        return domain
    lista_dto_arquivo = carregar_arquivos()
    return mapping_lista_dto_arquivo_to_lista_domain(lista_dto_arquivo)


def leitura_custou(lista_domain):
    def calcula_diferenca(domain): # calcula o quanto gastou para processar e o quanto gastou para processar
        var = domain['gasto_total'] - domain['gasto_escrita']
        if var >= 0: return var
        return -var

    def map_calcula_diferenca(lista_domain):
        return pool.map(calcula_diferenca , lista_domain)
    
    lista_diferenca = map_calcula_diferenca(lista_domain)
    max_lista_diferenca = max(lista_diferenca)
    print("Maior diferença", max_lista_diferenca)
    return max_lista_diferenca

def metricas_de_custou(lista_domain):
    def calcula_gasto(domain): 
        return domain['gasto_total']

    def map_calcula_gasto(lista_domain):
        return pool.map(calcula_gasto , lista_domain)
    
    lista_gasto = map_calcula_gasto(lista_domain)
    
    max_lista_gasto = max(lista_gasto)
    min_lista_gasto = min(lista_gasto)
    sum_lista_gasto = sum(lista_gasto)
    avg_lista_gasto = int(sum(lista_gasto)/len(lista_gasto))

    print("Maior gasto", max_lista_gasto)
    print("Menor gasto", min_lista_gasto)
    print("Media gasto", avg_lista_gasto)
    print("Total de gasto", sum_lista_gasto)
    
    return [max_lista_gasto,min_lista_gasto,sum_lista_gasto,avg_lista_gasto]


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
    leitura_custou(lista_domain)
    metricas_de_custou(lista_domain)
    gera_grafico_custo_processamento_execucao( lista_domain)