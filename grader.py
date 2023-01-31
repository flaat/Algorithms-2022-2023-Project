# This file checks if your solutions are correct. It also use python stopwatch to 
# give the execution time. If your solution exceed the maximum allowed time the test
# will be FAILED.
# If your implementation ends before the maximum allowed time and it returns the correct
# result the test will be PASSED.
import os
import time

import src.group0 as student_solution
import src.solution_evaluation.sorted_datasets as evaluate_sorting


def sorting_test():
    """
    This function checks if the sorting function works correctly.
    """
    def __get_dataset_filepaths(directory):
        return [f for f in os.listdir(directory) if f.endswith(".txt") and f.startswith("dataset")]

    def __get_dataset_size(filename):
        return filename[filename.index('_') + 1: filename.index('.')]

    score = 0
    DATA_PATH = "data/"
    
    dataset_file_paths = __get_dataset_filepaths(DATA_PATH)
    
    for file in dataset_file_paths:
        data = student_solution.read_file(f'{DATA_PATH}{file}')
        # start measuring exec time
        tic = time.time()
        student_sorted_data = student_solution.sort_data(data)
        # end measuring exec time
        toc = time.time()
        # instantiate the evaluator
        evaluator = evaluate_sorting.SortingEvaluator(student_sorted_struct=student_sorted_data)
        # evaluate the test
        dataset_size = __get_dataset_size(file)
        if evaluator.eval(dataset_size):
            score += 1
        
        print(f"Elapsed time: {toc-tic:.6f} seconds for dataset {dataset_size}")        
        print(f"Score: {score}/{len(dataset_file_paths)}")

        
            
if __name__ == "__main__":

    sorting_test()