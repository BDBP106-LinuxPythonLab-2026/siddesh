



def analyse_dna(sequence):
    sequence = sequence.upper()

    def gc_content():
        gc = sequence.count("G") + sequence.count("C")
        return gc / len(sequence) * 100

    gc = gc_content()
    print(f"GC content = {gc:.2f}%")
    if gc > 50:
        print("GC rich sequence")
    elif gc < 50:
        print("AT rich sequence")
    else:
        print("Equal AT and GC")
    return gc


analyse_dna("ATGCGCGTAGCCGATA")