import json
import matplotlib.pyplot as plt

from matplotlib.pyplot import cla
# import multiprocessing.dummy
# import matplotlib.pyplot as plt

class DomainExecution:
    def __init__(self , crude_execution:dict) -> None:
        #self.block_number = crude_execution['result']['receipt']['blockNumber']
        self.gas_used = crude_execution['result']['receipt']['gasUsed']
        self.function_name = crude_execution['function_name']


class LoadCrudeData:
    #Crude data is a list of list, second list is a trace of cyclo and first list is a ordenable set of cyclos
    def __init__(self , path , size ) -> None:
        self.path = path
        self.size = size
    
    def get(self):
        elements = list()
        for i in range(self.size):
            arq = open(f'{self.path}/{i}.dat', "r")
            elements += json.load(arq)
            arq.close()
        return elements

class Filter:
    @staticmethod
    def domain_filter(list_domain_cyclos:list, set_function_name:set)->list:
        list_filter_domain_cyclos = list()
        
        for list_domain_execution in list_domain_cyclos:
            list_filter_domain_execution = list()
        
            for domain_execution in list_domain_execution:
                if domain_execution.function_name in set_function_name:
                    list_filter_domain_execution.append(domain_execution)
        
            list_filter_domain_cyclos.append(list_filter_domain_execution)

        return list_filter_domain_cyclos

class Summarize:
    class DataSummarize:
        def __init__(self , number , value ) ->None:
            self.value = value
            self.number = number

    def get_list_value( list_summarize ):
        list_value = list()
        for summarize in list_summarize:
            list_value.append( summarize.value)
        return list_value

    def get_list_sum_value( list_summarize ):
        list_value = list()
        sum = 0
        for summarize in list_summarize:
            sum += summarize.value
            list_value.append( sum )
        return list_value

class Categorize:
    class DataCategorize :
        def __init__(self , number , value , group ) ->None:
            self.value = value
            self.number = number
            self.group = group
    
    class DatasetCategorize :
        def __init__(self ) ->None:
            self.data = dict()
            self._len = 0
        
        def add(self,categorize):
            if categorize.group not in self.data.keys():
                self.data[categorize.group] = list()
            self.data[categorize.group].append(categorize.value)
            self._len += 1
        
        def normalize(self)->None:
            if len( self.keys()) == 0:
                return
            
            for i in range(int(self._len/len(self.keys()))):
                sum = 0
                for key in self.data:
                    sum += self.data[key][i]
                
                for key in self.data:
                    self.data[key][i] /= sum                      
        
        def keys(self):
            return self.data.keys()

        def values(self):
            return self.data.values()

        def __len__(self) -> int:
            return int(self._len/len(self.keys()))
            

    def get_dataset_categorize( list_categorize ):
        data_set_categorize = Categorize.DatasetCategorize()

        for cyclo in list_categorize:
            for categorize in cyclo:
               data_set_categorize.add(categorize)
        return data_set_categorize

    def get_dataset_categorize_normalize( list_categorize ):
        data_set_categorize = Categorize.DatasetCategorize()

        for cyclo in list_categorize:
            for categorize in cyclo:
               data_set_categorize.add(categorize)
        data_set_categorize.normalize()
        return data_set_categorize

class Plot:
    @staticmethod
    def graph_value(list_value , path):
        plt.clf()
        plt.plot(list_value)     
        plt.savefig(path)

    @staticmethod
    def graph_subplot(dataset_categorize , path):
        fig, ax = plt.subplots()
        ax.stackplot(list(range(len(dataset_categorize))), dataset_categorize.values(),labels=dataset_categorize.keys())  
        ax.legend(loc='upper left')
        plt.savefig(path)


class Mapping:
    @staticmethod
    def crude_to_domain(list_crude_cyclos:list)->list:
        list_domain_cyclos = list()

        for list_crude_cyclo in list_crude_cyclos:
            list_domain_execution = list()
        
            for crude_execution in list_crude_cyclo:
                list_domain_execution.append( DomainExecution(crude_execution))
        
            list_domain_cyclos.append(list_domain_execution)
        return list_domain_cyclos
    
    @staticmethod
    def domain_summarize(list_domain_cyclos:list):
        list_summarize = list()

        for i , list_domain_execution in enumerate(list_domain_cyclos):
            var_sum = 0
            for domain_execution in list_domain_execution:
                var_sum += domain_execution.gas_used

            list_summarize.append(Summarize.DataSummarize(i,var_sum))
        return list_summarize
    
    @staticmethod
    def domain_categorize(list_domain_cyclos:list):
        list_cyclo_categorize = list()

        for i , list_domain_execution in enumerate(list_domain_cyclos):
            list_categorize = list()
            for domain_execution in list_domain_execution:
                list_categorize.append(Categorize.DataCategorize(i,domain_execution.gas_used,domain_execution.function_name))

            list_cyclo_categorize.append(list_categorize)
        return list_cyclo_categorize