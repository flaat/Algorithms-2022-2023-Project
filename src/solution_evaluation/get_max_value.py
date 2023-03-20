from os.path import join
from typing import Tuple

import pandas as pd

class MaxValueInAMonthEvaluator:      
    
    def __init__(self, dataset_size, student_data_struct=None):
        self.student_data_struct = student_data_struct
        self.dataset_size = dataset_size
        self.test_num = 0       
                
        self.BASE_PATH_TO_SOLUTION = join('solutions', 'get_max_value',
                                           f'{self.dataset_size}', 'results.csv')         
        
    def eval(self) -> bool:
        if not self.__check_correct_student_solution_format():
            print('Test failed.\nThe return type of get_max_value must be '\
                + 'Tuple[int, float]\n'\
                    + 'example: (1, 0.432)')
            
            return False
                
        correct_solution, _ = self.__read_solution()

        divergence_index = self.__first_divergence(correct_solution, self.student_data_struct)
        if divergence_index != -1:
            print(f'Test failed.\nYou correctly returned the data up until index={divergence_index}.\n'\
                + f'{self.student_data_struct[divergence_index]} is not equal to {correct_solution[divergence_index]}')
            
            return False
        
        print(f'Test passed on dataset_{self.dataset_size}.')    
        return True
            
    def __check_correct_student_solution_format(self) -> bool: 
        if not self.student_data_struct or type(self.student_data_struct) is not tuple:
            return False
        return len(self.student_data_struct) == 2\
            and type(self.student_data_struct[0]) is int\
                and type(self.student_data_struct[1]) is float
    
    
    def __read_solution(self):
        df = pd.read_csv(self.BASE_PATH_TO_SOLUTION, sep=',')
        temp = df.drop(columns=['crypto_name','month'])
        return tuple(float(x) for x in temp.values[self.test_num]), df.iloc[self.test_num][['crypto_name','month']]
    
    
    def __first_divergence(self, a: Tuple[int, float], b: Tuple[int, float]) -> int:
        assert len(a) == len(b), f"The length must be {len(a)}"
        for i in range(len(a)):
            if round(a[i], 4) != round(b[i], 4):
                return i
        return -1
    
    
    def set_test_num(self, test_num: int):
        self.test_num = test_num
        
    def set_student_data_struct(self, student_data_struct: any):
        self.student_data_struct = student_data_struct
        

        
        
    