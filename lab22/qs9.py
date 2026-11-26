

from functools import wraps



def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Running DNA analysis....")
        result = func(*args, **kwargs)
        print("Analysis complete!")
        return result
    return wrapper

def analyse_dna(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100


@log_function_call
def analyse_dna_logged(sequence):
    return analyse_dna(sequence)


gc_percent = analyse_dna_logged("ATGCGCGTAGCCGATA")
print(f"Returned GC%: {gc_percent:.2f}")



