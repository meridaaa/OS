
# Function to find the need of each process
def calculateNeed(need, maxm, allot, P, R):
    # Calculating Need of each P
    for i in range(P):
        for j in range(R):
            # Need of instance = maxm instance -
            # allocated instance
            need[i][j] = maxm[i][j] - allot[i][j]

        # Function to find the system is in


# safe state or not
def isSafe(avail, maxm, allot, P, R):
    need = []
    for i in range(P):
        l = []
        for j in range(R):
            l.append(0)
        need.append(l)

    # Function to calculate need matrix
    calculateNeed(need, maxm, allot, P, R)

    # Mark all processes as infinish
    finish = [0] * P

    # To store safe sequence
    safeSeq = [0] * P

    # Make a copy of available resources
    work = [0] * R
    for i in range(R):
        work[i] = avail[i]

    # While all processes are not finished
    # or system is not in safe state.
    count = 0
    while (count < P):

        # Find a process which is not finish
        # and whose needs can be satisfied
        # with current work[] resources.
        found = False
        for p in range(P):

            # First check if a process is finished,
            # if no, go for next condition
            if (finish[p] == 0):
                executing = True
                # Check if for all resources
                # of current P need is less
                # than work

                for j in range(R):
                 if (need[p][j] > work[j]):
                     executing = False
                     break
                # If all needs of p were satisfied.
                 if (j == R - 1 and executing):

                    # Add the allocated resources of
                    # current P to the available/work
                    # resources i.e.free the resources
                    for k in range(R):
                        work[k] += allot[p][k]

                    # Add this process to safe sequence.
                    safeSeq[count] = p
                    count += 1

                    # Mark this p as finished
                    finish[p] = 1

                    found = True

        # If we could not find a next process
        # in safe sequence.
        if (found == False):
            print("System is not in safe state")
            return False

    # If system is in safe state then
    # safe sequence will be as below
    print("System is in safe state.",
          "\nSafe sequence is: ", end=" ")
    print(*safeSeq)

    return True

# Driver code
if __name__ == "__main__":
    p = int(input("number of process: "))
    r = int(input("number of resources: "))


    # Available instances of resources
    avail = []
    print('Enter the available : ')
    for i in range(r):
      x = int(input())
      avail.append(x)

    # Maximum R that can be allocated
    # to processes
    maxm =[]
    print("Max[{}][{}]: ".format(p, r))
    for i in range(p):  # A for loop for row entries
        a = []
        for j in range(r):  # A for loop for column entries
            a.append(int(input()))
        maxm.append(a)
    # Resources allocated to processes
    allot = []
    print("A[{}][{}]: ".format(p, r))
    for i in range(p):  # A for loop for row entries
        a = []
        for j in range(r):  # A for loop for column entries
            a.append(int(input()))
        allot.append(a)

    # Check system is in safe state or not
    isSafe(avail, maxm, allot, p, r)

