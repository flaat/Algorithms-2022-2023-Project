# This file checks if your solutions are correct. It also use python stopwatch to 
# give the execution time. If your solution exceed the maximum allowed time the test
# will be FAILED.
# If your implementation ends before the maximum allowed time and it returns the correct
# result the test will be PASSED.
import time
import src.group0 as student_solution
import src.solutions.sorted_datasets as sol_dataset

def sorting_test():
    """
    This function checks if the sorting function works correctly.
    """

    DATA_PATH = "data/"

    solution_datasets = {"small":sol_dataset.DATASET_250, 
                        "medium":sol_dataset.DATASET_500, 
                        "large":sol_dataset.DATASET_750, 
                        "full":sol_dataset.DATASET_FULL}

    for size in ["small", "medium", "large", "full"]:

        failed = False

        data = student_solution.read_file(DATA_PATH+f"dataset_{size}.txt")

        tic = time.time()

        sorted_data = student_solution.sort_data(data)

        toc = time.time()

        if sorted_data is None:

            raise Exception("sorted_data is None!")

        for index, element in enumerate(sorted_data):
        
            if element !=  solution_datasets[size][index]:

                print(f"TEST \033[91m FAILED \033[0m: sorting with the {size} dataset")
                print(f"    Error: your solution at position {index} have element {element}, it should be instead {solution_datasets[size][index]}")
                failed = True
                break

        if not failed:
            print(f"TEST \033[92m PASSED \033[0m: it took {toc-tic} seconds to sort the {size} dataset.")


if __name__ == "__main__":

    sorting_test()