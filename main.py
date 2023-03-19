# python3

def parallel_processing(n, m, data):
    output = []
    thread_times =[0]*n

    for i in range(m):
        min_time = min(thread_times)
        thread_index = thread_times.index(min_time)

        output.append((thread_index, min_time))
        if i<len(data):
            thread_times[thread_index]+=data[i]
    return output
    return output

def main():
    n,m =map(int,input().split())
    data = list(map(int,input().split()))
    result = parallel_processing(n,m,data)
    
    for thread_index, start_time in result:
        print(thread_index, start_time)
        
if __name__ == "__main__":
    main()
