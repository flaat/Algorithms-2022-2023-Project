class MSTEvaluator:      
    
    def __init__(self, dataset_size, student_data_struct=None):
        self.student_data_struct = student_data_struct
        self.dataset_size = dataset_size
        self.test_num = 0       
        
    def eval(self) -> bool:
        if not self.__check_correct_student_solution_format():
            print('Test failed.\nThe return type of min_correlation_pathways must be '\
                + 'Dict[str, List[str]]\n'\
                    + 'example: {"john": ["jack", "michael"], "michael": ["jack"]}')
            
            return False
          
        if self.__has_cycle():
            print(f'Test failed.\nYou incorrectly returned a cyclic data structure.\nMSTs do not have cycles')
            return False
                
        print(f'Test passed on dataset_{self.dataset_size}.')    
        return True
            
    def __check_correct_student_solution_format(self) -> bool:   
        if not self.student_data_struct or type(self.student_data_struct) is not dict:
            return False
        keys = list(self.student_data_struct.keys())
        vals = self.student_data_struct.values()
        keys_are_strs = all(type(key) is str for key in keys)
        values_are_strs = True
        for val_list in vals:
            if type(val_list) is not list:
                values_are_strs = values_are_strs & False
                break
            else:
                for child in val_list:
                    if type(child) is not str:
                        values_are_strs = values_are_strs & False
                        break
                    
        return keys_are_strs & values_are_strs
      
      
    def __has_cycle(self):
        visited = set()
        stack = set()

        def dfs(node):
            visited.add(node)
            stack.add(node)

            for neighbor in self.student_data_struct.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in stack:
                    return True

            stack.remove(node)
            return False

        for node in self.student_data_struct:
            if node not in visited:
                if dfs(node):
                    return True

        return False
    
    
    def set_test_num(self, test_num: int):
        self.test_num = test_num
        
    def set_student_data_struct(self, student_data_struct: any):
        self.student_data_struct = student_data_struct
        

        
        
    