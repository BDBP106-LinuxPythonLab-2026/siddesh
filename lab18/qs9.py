def extract_codons(sequence, start_pos):
    start_idx = start_pos - 1

    return [
        sequence[i : i + 3]
        for i in range(start_idx, len(sequence) - 2, 3)
    ]


dna = "AGTCTTATATCT"

print("1st position:", extract_codons(dna, 1))
print("3rd position:", extract_codons(dna, 3))
