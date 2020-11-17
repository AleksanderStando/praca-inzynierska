def downsampling_convolution(self, data, filter, step, mode):
    output = []
    i = step - 1
    N = len(data)
    F = len(filter)
    while i < F and i < N:
        sum = 0
        j = 0
        while j < i:
            sum = sum + filter[j]*data[i-j]
            j = j + 1
        if mode == "SYMMETRIC":
            while j < F:
                k = 0
                while k < N and j < F:
                    sum = sum + filter[j]*data[k]
                    k = k+1
                    j = j+1
                k = 0
                while k < N and j < F:
                    sum = sum + filter[j]*data[N-1-k]
                    k = k+1
                    j = j+1
        if mode == "PERIODIC":
            while j < F:
                k = 0
                while k < N and j < F:
                    sum += filter[j]*data[N-1-k]
                    k = k + 1
                    j = j + 1
        i = i + step
        output.append(sum)

    #center if N >= F
    while i < len(data):
        sum = 0
        j = 0
        while j < F:
            sum += data[i-j]*filter[j]
            j = j + 1
        i = i + step
        output.append(sum)
    # center if F > N
    while i < F:
        sum = 0
        j = 0
        if mode == "SYMMETRIC":
            while i - j >= len(data):
                k = 0
                while k < len(data) and i - j >= len(data):
                    sum = sum + filter[i-N-j]*data[N-1-k]
                    k = k+1
                    j = j+1
                k = 0
                while k < len(data) and i - j >= len(data):
                    sum = sum + filter[i-N-j]*data[k]
                    k = k+1
                    j = j+1
        if mode == "PERIODIC":
            while j < F:
                k = 0
                while k < len(data) and j < F:
                    sum += filter[j]*data[N-1-k]
                    k = k+1
                    j = j+1

        while j < i:
            sum = sum + filter[j]*data[i-j]

        if mode == "SYMMETRIC":
            while j < F:
                k = 0
                while k < len(data) and i - j >= len(data):
                    sum = sum + filter[j]*data[k]
                    k = k+1
                    j = j+1
                k = 0
                while k < len(data) and i - j >= len(data):
                    sum = sum + filter[j]*data[N-1-k]
                    k = k+1
                    j = j+1
        if mode == "PERIODIC":
            while j < F:
                k = 0
                while k < N and j < F:
                    sum = sum + filter[j]*data[N-1-k]
        output.append(sum)
        i = i + step

    #right boundry
    while i < N + F - 1:
        sum = 0
        j = 0
        if mode == "SYMMETRIC":
            while i - j >= N:
                k = 0
                while k < N and i - j >= N:
                    sum = sum + filter[i-N-j]*data[N-1-k]
                    k = k+1
                    j = j+1
                k = 0
                while k < N and j < F:
                    sum = sum + filter[i-N-j]*data[k]
                    k = k+1
                    j = j+1
        if mode == "PERIODIC":
            while i - j >= N:
                k = 0
                while k < N and i-j >= N:
                    sum = sum + filter[i-N-j]*data[k]
                    k = k+1
                    j = j+1
        while j < F:
            sum = sum + filter[j]*data[i-j]
            j = j+1
        output.append(sum)
        i = i + step
    return output
