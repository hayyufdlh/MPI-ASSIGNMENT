from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

start = 1
end = 1000

range_size = (end - start + 1) // size

local_start = start + rank * range_size
local_end = local_start + range_size - 1

local_sum = sum(range(local_start, local_end + 1))

total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

if rank == 0:
    print(f"Total penjumlahan dari {start} sampai {end} adalah {total_sum}")
