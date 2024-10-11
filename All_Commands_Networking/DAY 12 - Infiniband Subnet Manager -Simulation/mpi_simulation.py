#pip3 install mpi4py
#############################################
# sudo apt update
#sudo apt install libopenmpi-dev openmpi-bin openmpi-common


#mpiexec -n 4 python3 mpi_simulation.py
####################################################
from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if size != 4:
        print("This simulation requires exactly 4 processes.")
        return

    # Define the data each process will send
    data_to_send = rank * 10  # Just an example: each process sends its rank multiplied by 10

    # Define the neighbors for a 2x2 mesh topology
    neighbors = {
        0: [1, 2],  # Node 1
        1: [0, 3],  # Node 2
        2: [0, 3],  # Node 3
        3: [1, 2],  # Node 4
    }

    # Each process sends data to its neighbors and receives data from them
    received_data = {}
    for neighbor in neighbors[rank]:
        comm.send(data_to_send, dest=neighbor)
        received_data[neighbor] = comm.recv(source=neighbor)

    print(f"Process {rank} received data: {received_data}")

if __name__ == "__main__":
    main()
