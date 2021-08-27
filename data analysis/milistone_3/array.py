from _estagios_5_data import carrega_lista_domain , calcula_gasto_eth  , sumariza_gasto_por_estagio , gera_grafico_custo_processamento_execucao , gera_grafico_custo_processamento_execucao_sumarizacao

if __name__ == '__main__':
    lista_domain = carrega_lista_domain("../../results/milestone_3/crude/array",123)
    calcula_gasto_eth(lista_domain)
    # captura_identificacao(lista_domain)
    sumariza_gasto_por_estagio(lista_domain)
    gera_grafico_custo_processamento_execucao(lista_domain,"../../results/milestone_3/generate/2.array.png")
    gera_grafico_custo_processamento_execucao_sumarizacao(lista_domain,"../../results/milestone_3/generate/2.array-sum.png")