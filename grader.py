# This file checks if your solutions are correct. It also use python stopwatch to 
# give the execution time. If your solution exceed the maximum allowed time the test
# will be FAILED.
# If your implementation ends before the maximum allowed time and it returns the correct
# result the test will be PASSED.
import os
import time
from typing import Tuple

import numpy as np

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
    
    
    DATA_PATH = "data/"
    
    scores, average_time = [], []
    
    dataset_file_paths = __get_dataset_filepaths(DATA_PATH)
    #############################################################################
    # tests for the small dataset
    filepath = f'{DATA_PATH}{dataset_file_paths[-1]}'
    data = student_solution.read_file(filepath)
    
    dataset_size = __get_dataset_size(filepath)
    # test 1
    score, seconds = perform_test(dataset_size=dataset_size,
                 test_num=0,
                 crypto_stats_args={
                     'data': data,
                     'crypto_name': 'Algorand',
                     'interval': (1,5)
                 })
    scores.append(score)
    average_time.append(seconds)
    # test 2
    score, seconds = perform_test(dataset_size=dataset_size,
                 test_num=1,
                 crypto_stats_args={
                     'data': data,
                     'crypto_name': 'Algorand',
                     'interval': (200,1000)
                 })
    scores.append(score)
    average_time.append(seconds)
    # test 3
    score, seconds = perform_test(dataset_size=dataset_size,
                 test_num=2,
                 crypto_stats_args={
                     'data': data,
                     'crypto_name': 'Elrond',
                     'interval': (15,18)
                 })
    scores.append(score)
    average_time.append(seconds)
    # test 4
    score, seconds = perform_test(dataset_size=dataset_size,
                 test_num=3,
                 crypto_stats_args={
                     'data': data,
                     'crypto_name': 'tether',
                     'interval': (20,20)
                 })
    scores.append(score)
    average_time.append(seconds)
    # test 5
    score, seconds = perform_test(dataset_size=dataset_size,
                 test_num=4,
                 crypto_stats_args={
                     'data': data,
                     'crypto_name': 'TrueUSD',
                     'interval': (1,3)
                 })
    scores.append(score)
    average_time.append(seconds)
    # test 6
    score, seconds = perform_test(dataset_size=dataset_size,
                 test_num=5,
                 crypto_stats_args={
                     'data': data,
                     'crypto_name': '1inch',
                     'interval': (0,149)
                 })
    scores.append(score)
    average_time.append(seconds)
    # test 7
    score, seconds = perform_test(dataset_size=dataset_size,
                 test_num=6,
                 crypto_stats_args={
                     'data': data,
                     'crypto_name': 'Kusama',
                     'interval': (12,47)
                 })
    scores.append(score)
    average_time.append(seconds)
    # test 8
    score, seconds = perform_test(dataset_size=dataset_size,
                 test_num=7,
                 crypto_stats_args={
                     'data': data,
                     'crypto_name': '1inch',
                     'interval': (12,56)
                 })
    scores.append(score)
    average_time.append(seconds)
    # test 9
    score, seconds = perform_test(dataset_size=dataset_size,
                 test_num=8,
                 crypto_stats_args={
                     'data': data,
                     'crypto_name': 'IOTA',
                     'interval': (9,18)
                 })
    scores.append(score)
    average_time.append(seconds)
    # test 10
    score, seconds = perform_test(dataset_size=dataset_size,
                 test_num=9,
                 crypto_stats_args={
                     'data': data,
                     'crypto_name': 'bitcoin',
                     'interval': (1,1000)
                 })
    scores.append(score)
    average_time.append(seconds)
    ###############################################################################
    print(f"Elapsed time: {np.mean(average_time):.6f} seconds for dataset {dataset_size}")        
    print(f"Score: {sum(scores)}/{len(scores)}")
    ###############################################################################

    
def sorting_test():
    """
        This function checks if the sorting function works correctly.
    """
    score = 0
    DATA_PATH = "data/"
    
    dataset_file_paths = __get_dataset_filepaths(DATA_PATH)
    
    for file in dataset_file_paths:
        data = student_solution.read_file(f'{DATA_PATH}{file}')
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
                
        print(f"Elapsed time: {toc-tic:.6f} seconds for dataset {dataset_size}")        
        print(f"Score: {score}/{len(dataset_file_paths)}")

def __get_dataset_filepaths(directory):
    return [f for f in os.listdir(directory) if f.endswith(".txt") and f.startswith("dataset")]

def __get_dataset_size(filename):
    return filename[filename.index('_') + 1: filename.index('.')]
            
if __name__ == "__main__":

    crypto_stats_test()