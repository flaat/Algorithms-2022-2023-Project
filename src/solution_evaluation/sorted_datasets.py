from os.path import join
from math import isclose
from typing import List, Tuple

import pandas as pd

class SortingEvaluator:
    
    def __init__(self, dataset_size, student_data_struct=None):
        self.student_data_struct = student_data_struct
        self.dataset_size = dataset_size
        
        self.BASE_PATH_TO_SOLUTION = join('solutions','sorted_datasets',
                                          f'{self.dataset_size}', 'test.csv')
        
        
    def eval(self) -> bool:
        if not self.__check_correct_student_solution_format():
            print('Test failed.\nThe return type of sorted_data must be '\
                + 'List[Tuple[str, float]]\n'\
                    + 'example: [("algorand",0.1),("bitcoin",0.2),("etherium",3.4)]')
            
            return False
                    
        correct_solution = self.__read_solution()
        
        divergence_index = self.__first_divergence(correct_solution, self.student_data_struct)
        if divergence_index != -1:
            print(f'Test failed.\nYou correctly sorted the data up until index={divergence_index}.\n'\
                + f'{self.student_data_struct[divergence_index]} does not come before {correct_solution[divergence_index]}')
            
            return False
        
        print(f'Test passed on dataset_{self.dataset_size}.')    
        return True
    
    def __read_solution(self) -> List[Tuple[str, float]]:
        df = pd.read_csv(self.BASE_PATH_TO_SOLUTION, sep=',')
        values = df.values
        return list(map(lambda elem: tuple(elem), values))


    def __check_correct_student_solution_format(self) -> bool:      
        if not self.student_data_struct or type(self.student_data_struct) is not list:
            return False
        return all(type(item) is tuple and len(item) == 2 and type(item[0]) is str and type(item[1]) is float 
                for item in self.student_data_struct)


    def __first_divergence(self, a: List[Tuple[str, float]], b: List[Tuple[str, float]]) -> int:
        assert len(a) == len(b), f"The length of the sorted dataset must be {len(a)}"
        for i in range(len(a)):
            # this is necessary because when saving the solutions dataframe to csv
            # we lose the decimal digits after the 13th decimal point
            if a[i][0] != b[i][0] or not isclose(a[i][1], b[i][1], rel_tol=1e-13, abs_tol=1e-13):
                return i
        return -1
        
