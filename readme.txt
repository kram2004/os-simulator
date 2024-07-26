OS Simulator
Overview
The OS Simulator is a command-line application designed to test and demonstrate understanding of various operating system concepts. This project implements several algorithms used in process handling within the CPU, including process synchronization and scheduling algorithms.

Features
Process Synchronization: Implements algorithms to manage the execution of processes in a way that ensures they do not interfere with each other.
Scheduling Algorithms: Includes various scheduling algorithms such as First-Come-First-Served (FCFS), Shortest Job Next (SJN), Priority Scheduling, and Round Robin.
Command-Line Interface: Provides a user-friendly interface to input commands and view the status of processes.
Technologies Used
Programming Language: Python
Development Tools: GitHub for version control
Getting Started
Clone the Repository:
 
git clone https://github.com/kram2004/os-simulator.git
Navigate to the Project Directory:
 
cd os-simulator
Run the Simulator:
 
python os_simulator.py
Usage
The OS Simulator accepts various commands to manage processes. Below are some example commands:

Add a Process:
 
add_process <process_name> <burst_time> <priority>
View Process List:
 
view_processes
Execute Scheduling Algorithm:
 
run_scheduling <algorithm_name>
Example
To add a process with a burst time of 10 units and a priority of 1:


add_process Process1 10 1
To view all the processes:


view_processes
To run the Round Robin scheduling algorithm:

 
run_scheduling round_robin
Contributions
Contributions are welcome! Please fork the repository and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or issues, please contact ramreddyk2105@gmail.com.