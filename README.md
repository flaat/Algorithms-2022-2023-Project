# Algorithms-2022-2023-Project
Group project work - ALGORITHMS 2022/2023 course, Management and Computer Science Bachelor's degree, LUISS

<h2>The tools we'll use</h2>
<ul>
  <li><a href="https://desktop.github.com/">GitHub Desktop<a> - to help you clone the repository with a UI, instead of installing the git command and going through basic bash instructions (out of scope for Algorithms).</li>
  <li><a href="https://code.visualstudio.com/Download">VSCode</a> - The IDE that we'll use throughout the programming classes. It gives the opportunity to manage git commands from the UI.</li>
  <li>Extension packs for VSCode:
    <ul>
      <li>Git Extension Pack - popular VSCode extension for Git</li>
      <li>Python - Code formatting, refactoring, debugging</li>
    </ul>
  </li>
</ul>
<h2>Environment setup</h2>
Use the environment.yml file to get all the necessary packages to execute <b>grader.py</b>

To create the environment, follow these steps:
```console

39348@DESKTOP-R63USTJ MINGW64:~$ conda env create -f environment.yml
Collecting package metadata (repodata.json): done
Solving environment: done

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate cryptos
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```
To activate the environment, follow these steps:
```console
39348@DESKTOP-R63USTJ MINGW64:~$ conda activate cryptos
```
You should see a prefix (cryptos) appaear in front of your bash user.

<h2>Using the grader</h2>
We provide you with a automatic partial grading system to assess the correctness of your implemented algorithms. It is partial since we provide you only with some cases of testing. The overall testing, and scoring, will be performed by the TAs on May's deadline.

To use the grader, follow these steps on the main directory of the project:
```console

39348@DESKTOP-R63USTJ MINGW64:~$ python grader.py
```
In this way, for each function you implement you'll have some metrics of passed/failed tests. 
The directory <b>solutions</b> contains the correct output for each test input in the <b>tests</b> directory.

For example, for the first row in file <b>tests/crypto_stats/small</b>, the correct output corresponds to the content of the first row in file <b>solutions/crypto_stats/small/results.csv</b> according to the return type specified in function <b>crypto_stats</b> in <b>src/group0.py</b>. 
