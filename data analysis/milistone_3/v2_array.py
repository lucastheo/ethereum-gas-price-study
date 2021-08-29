from v2__estagios_5_data import LoadCrudeData, Mapping, Filter, Summarize, Plot ,Categorize

def summarize(domain_data , path):
    summarize_data = Mapping.domain_summarize(domain_data)
    value_data = Summarize.get_list_value(summarize_data)
    Plot.graph_value(value_data,path)

def summarize_sum( domain_data , path):
    summarize_data = Mapping.domain_summarize(domain_data)
    value_sum_data = Summarize.get_list_sum_value(summarize_data)
    Plot.graph_value(value_sum_data,path)

def categorize(domain_data,path):
    categorize_data = Mapping.domain_categorize(domain_data)
    value_dict_list = Categorize.get_dataset_categorize(categorize_data)
    Plot.graph_subplot(value_dict_list,path)

def categorize_normalize(domain_data,path):
    categorize_data = Mapping.domain_categorize(domain_data)
    value_normalize_dict_list = Categorize.get_dataset_categorize_normalize(categorize_data)
    Plot.graph_subplot(value_normalize_dict_list,path)

load_crude_data = LoadCrudeData('../../results/milestone_3/crude/v2_array' , 123 )
crude_data = load_crude_data.get()

domain_data = Mapping.crude_to_domain(crude_data)

summarize(domain_data,'../../results/milestone_3/generate/v2.2.array.geral.png')
summarize_sum(domain_data, '../../results/milestone_3/generate/v2.2.array.geral-sum.png')

categorize(domain_data,'../../results/milestone_3/generate/v2.2.array.subplot.geral.png')
categorize_normalize(domain_data,'../../results/milestone_3/generate/v2.2.array.subplot-normalize.geral.png')

for filter in {'inserirElemento','contarElemento','percorre','percorreConta'}:
    
    filter_data_inserir_elemento = Filter.domain_filter(domain_data, {filter})
    summarize(filter_data_inserir_elemento,f'../../results/milestone_3/generate/v2.2.array.{filter}.png')
    summarize_sum(filter_data_inserir_elemento, f'../../results/milestone_3/generate/v2.2.array.{filter}-sum.png')

