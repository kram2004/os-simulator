import queue

class Process:
    def __init__(self, pid, burst_time, priority):
        self.pid = pid
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time

def fcfs(processes):
    processes.sort(key=lambda x: x.pid)
    print("FCFS Scheduling:")
    for process in processes:
        print(f"Process {process.pid}: Burst Time = {process.burst_time}")

def sjn(processes):
    processes.sort(key=lambda x: x.burst_time)
    print("SJN Scheduling:")
    for process in processes:
        print(f"Process {process.pid}: Burst Time = {process.burst_time}")

def priority_scheduling(processes):
    processes.sort(key=lambda x: x.priority)
    print("Priority Scheduling:")
    for process in processes:
        print(f"Process {process.pid}: Priority = {process.priority}, Burst Time = {process.burst_time}")

def round_robin(processes, quantum):
    queue = processes[:]
    time = 0
    print("Round Robin Scheduling:")
    while queue:
        process = queue.pop(0)
        if process.remaining_time > quantum:
            time += quantum
            process.remaining_time -= quantum
            queue.append(process)
        else:
            time += process.remaining_time
            process.remaining_time = 0
            print(f"Process {process.pid} finished at time {time}")

def add_process(processes, pid, burst_time, priority):
    processes.append(Process(pid, burst_time, priority))

def view_processes(processes):
    print("Processes List:")
    for process in processes:
        print(f"Process {process.pid}: Burst Time = {process.burst_time}, Priority = {process.priority}")

def main():
    processes = []
    quantum = 2  # Time quantum for Round Robin scheduling

    while True:
        command = input("Enter command: ").strip().split()
        if command[0] == "add_process":
            add_process(processes, int(command[1]), int(command[2]), int(command[3]))
        elif command[0] == "view_processes":
            view_processes(processes)
        elif command[0] == "run_scheduling":
            if command[1] == "fcfs":
                fcfs(processes)
            elif command[1] == "sjn":
                sjn(processes)
            elif command[1] == "priority":
                priority_scheduling(processes)
            elif command[1] == "round_robin":
                round_robin(processes, quantum)
        elif command[0] == "exit":
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
