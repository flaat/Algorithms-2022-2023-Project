# This file checks if your solutions are correct. It also use python stopwatch to 
# give the execution time. If your solution exceed the maximum allowed time the test
# will be FAILED.
# If your implementation ends before the maximum allowed time and it returns the correct
# result the test will be PASSED.
import os
import time
from os.path import join
from typing import Tuple

import numpy as np
import pandas as pd

import src.group0 as student_solution
from src.solution_evaluation.crypto_stats import CryptoStatsEvaluator
from src.solution_evaluation.sorted_datasets import SortingEvaluator


def crypto_stats_test():
    """
        This functions checks if the crypto_stats function works correctly.
    """
    def perform_test(dataset_size, test_num, crypto_stats_args) -> Tuple[int, float]:
        tic = time.time()
        retr = student_solution.crypto_stats(**crypto_stats_args)
        toc = time.time()
        # instantiate the evaluator
        evaluator = CryptoStatsEvaluator(dataset_size=dataset_size,
                                        student_data_struct=retr)
        evaluator.set_test_num(test_num)
        score = 1 if evaluator.eval() else 0
        
        return (score, toc-tic)
    
    
    DATA_PATH, TEST_PATH = "data", "tests"
    
    scores, average_time = [], []
    
    dataset_file_paths = __get_dataset_filepaths(DATA_PATH)
    #############################################################################
    # tests for the small dataset
    filepath = join(DATA_PATH, dataset_file_paths[-1])
    dataset_size = __get_dataset_size(filepath)
    
    data = student_solution.read_file(filepath)

    test_file = join(TEST_PATH, 'crypto_stats', dataset_size, 'test.csv')
    df = pd.read_csv(test_file)
    
    for i, value in enumerate(df.values):
        score, seconds = perform_test(dataset_size=dataset_size,
                                      test_num=i,
                                      crypto_stats_args={
                                          'data': data,
                                          'crypto_name': value[0],
                                          'interval': (value[1], value[-1])
                                      })
        scores.append(score)
        average_time.append(seconds)
    ###############################################################################
    print(f"crypto_stats ---- Elapsed time: {np.mean(average_time):.6f} seconds for dataset {dataset_size}")        
    print(f"Score: {sum(scores)}/{len(scores)}")
    ###############################################################################

def reading_data_test():
    """
        This functions measures the time of the reading function.
    """
    DATA_PATH = "data/"    
    dataset_file_paths = __get_dataset_filepaths(DATA_PATH)
    for data_file_path in dataset_file_paths:
        tic = time.time()
        _ = student_solution.read_file(join(DATA_PATH, data_file_path))
        toc = time.time()
        data_size = __get_dataset_size(data_file_path)
   
        print(f'reading_file --- Elapsed time: {toc-tic:6f} seconds for dataset {data_size}')
    
def sorting_test():
    """
        This function checks if the sorting function works correctly.
    """
    score = 0
    DATA_PATH = "data"
    
    dataset_file_paths = __get_dataset_filepaths(DATA_PATH)
    
    for file in dataset_file_paths:
        data = student_solution.read_file(join(DATA_PATH, file))
        # start measuring exec time
        tic = time.time()
        retr = student_solution.sort_data(data)
        # end measuring exec time
        toc = time.time()
        # instantiate the evaluator
        dataset_size = __get_dataset_size(file)
        evaluator = SortingEvaluator(dataset_size=dataset_size,
                                     student_data_struct=retr)
        # evaluate the test
        score += 1 if evaluator.eval() else 0
                
        print(f"sort_data --- Elapsed time: {toc-tic:.6f} seconds for dataset {dataset_size}")        
        print(f"Score: {score}/{len(dataset_file_paths)}")

def __get_dataset_filepaths(directory):
    return [f for f in os.listdir(directory) if f.endswith(".txt") and f.startswith("dataset")]

def __get_dataset_size(filename):
    return filename[filename.index('_') + 1: filename.index('.')]
            
if __name__ == "__main__":
    reading_data_test()
    crypto_stats_test()