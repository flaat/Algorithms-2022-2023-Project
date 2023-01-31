import os
from math import isclose
from typing import List, Tuple

import pandas as pd


class SortingEvaluator:
    
    def __init__(self, student_sorted_struct=None):
        self.student_sorted_struct = student_sorted_struct
        
        self.SIZE_TO_SORTED_DATASET_PATH = {
            'full': os.path.join('solutions', 'sorted_datasets','dataset_full.csv'),
            'large': os.path.join('solutions', 'sorted_datasets','dataset_large.csv'),
            'medium': os.path.join('solutions', 'sorted_datasets','dataset_medium.csv'),
            'small': os.path.join('solutions', 'sorted_datasets','dataset_small.csv')
        }
        
        
    def eval(self, dataset_size: str) -> bool:
        if not self.__check_correct_student_solution_format():
            print('Test #2 failed.\nThe return type of sorted_data must be '\
                + 'List[Tuple[str, float]]\n'\
                    + 'example: [("algorithms",0.1),("databases",0.2),("networking",3.4)]')
            
            return False
        
        sorted_dataset_path = self.__get_sorted_dataset_path(dataset_size)
            
        correct_solution = self.__read_sorted_datasets(sorted_dataset_path)
        
        divergence_index = self.__first_divergence(correct_solution, self.student_sorted_struct)
        if divergence_index != -1:
            print(f'Test #2 failed.\nYou correctly sorted the data up until index={divergence_index}.\n'\
                + f'{self.student_sorted_struct[divergence_index]} does not come before {correct_solution[divergence_index]}')
            
            return False
        
        print(f'Test #2 passed on dataset_{dataset_size}.')    
        return True
    
    
    def __get_sorted_dataset_path(self, size: str) -> str:
        return self.SIZE_TO_SORTED_DATASET_PATH.get(size.lower(), None)
    
    def __read_sorted_datasets(self, filepath: str) -> List[Tuple[str, float]]:
        df = pd.read_csv(filepath, sep=',')
        values = df.values
        return list(map(lambda elem: tuple(elem), values))


    def __check_correct_student_solution_format(self) -> bool:
        checker: bool = False
        
        if self.student_sorted_struct:
            if type(self.student_sorted_struct) is list:
                for item in self.student_sorted_struct:
                    if not type(item) is tuple\
                        or len(item) != 2\
                            or not type(item[0]) is str\
                                or not type(item[1]) is float:
                            return False
                checker = True
                
        return checker


    def __first_divergence(self, a: List[Tuple[str, float]], b: List[Tuple[str, float]]) -> int:
        assert len(a) == len(b), f"The length of the sorted dataset must be {len(a)}"
        for i in range(len(a)):
            # this is necessary because when saving the solutions dataframe to csv
            # we lose the decimal digits after the 13th decimal point
            if a[i][0] != b[i][0] or not isclose(a[i][1], b[i][1], rel_tol=1e-13, abs_tol=1e-13):
                return i
        return -1
        
