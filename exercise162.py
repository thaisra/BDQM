def print_even(string_in):
    try:
        if len(string_in) == 0:
            raise ValueError("The string is empty")
        even_chars = [string_in[i] for i in range(len(string_in)) if i%2 == 1]
        print(" ".join(even_chars))
    except ValueError as e:
        print(e)
print_even("Python")
print_even("")

S = ["Gojackets", "Call me Ishmael", "ILoveChBE"]
results = {n: print_even(n) for n in S}
print(results)
        
