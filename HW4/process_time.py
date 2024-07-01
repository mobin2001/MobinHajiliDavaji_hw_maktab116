from time import perf_counter

fibo_fac_dict = {}

def cache(func):
    
    def inner(n):
        
        # with open('e:/newtext2.txt','r') as fin:
        #     fin = fin.readlines()
        #     fin = fin[0].split('\n')
        if n in fibo_fac_dict:
                #index_n = fin.index(n)
            return fibo_fac_dict[n]
            
        else:
            value = func(n)
            fibo_fac_dict[n] = value
        # with open('e:/newtext2.txt','w') as fout:
        #     for key in fibo_fac_dict:
        #         fout.writelines(f"{key}={fibo_fac_dict[key]}\n")
        return value
        

    return inner



def process_timer(func):
    def inner(*args):
        start = perf_counter()
        value = func(*args)
        end = perf_counter()
        process_time = end - start
        
        print('process run time = ',process_time)
        return value
    return inner
@cache
def fibo(x):
    if x == 1 or x == 0:
        return x
    else:
        return fibo(x-2) + fibo(x-1)
@cache
def fac(x):
    if x == 0:
        return 1
    else:
        return x * fac(x-1)
start = perf_counter()
print(fac(100))
end = perf_counter()
print(end-start)
#print(fibo(35))

#print(fibo_fac_dict)