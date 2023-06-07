import networkx as nx

class KCorrsEvaluator:      
    
    def __init__(self,
                 dataset_size,
                 student_data_struct=None,
                 level=0,
                 source='Algorand'):
        self.student_data_struct = student_data_struct
        self.dataset_size = dataset_size
        self.test_num = 0
        self.level = level
        self.source_crypto = source
        
    def eval(self) -> bool:
        if not self.__check_correct_student_solution_format():
            print('Test failed.\nThe return type of correlated_cryptos_at_lvl_k must be '\
                + 'Tuple[Dict[str, List[str]], List[str]]\n'\
                    + 'example: ({"john": ["jack", "michael"], "michael": ["jack"]}, ["john","jack","michael"])')
            print('Did you return both the minimum correlation pathways and the correlated cryptos at level k?')
            return False
          
        if self.__bfs():
            print(f'Test passed on dataset_{self.dataset_size}.')    
            return True
            
            
    def __bfs(self):
        graph_dict = self.student_data_struct[0]
        g = nx.DiGraph(graph_dict)
        visit = nx.single_source_shortest_path_length(g, self.source_crypto.lower())
        res = [crypto.lower() for crypto in visit if visit[crypto] == self.level]
        return set(res) == set(self.student_data_struct[1])
    
    
    def __check_correct_student_solution_format(self) -> bool:
        if len(self.student_data_struct) != 2:
            return False   
        
        if not self.student_data_struct[1] or type(self.student_data_struct[1]) is not list:
            return False
        
        return all(type(elem) is str for elem in self.student_data_struct[1])
    
    def set_test_num(self, test_num: int):
        self.test_num = test_num
        
    def set_student_data_struct(self, student_data_struct: any):
        self.student_data_struct = student_data_struct
        

        
        
    