



class DNAError(Exception):
    """Base class for all DNA-related errors."""


class EmptySequenceError(DNAError):
    """Raised when a sequence is empty."""


class InvalidBaseError(DNAError):
    """Raised when a sequence contains characters other than A, T, G, C."""

    def __init__(self, bad_chars):
        self.bad_chars = sorted(set(bad_chars))
        super().__init__(f"Invalid base(s) in sequence: {', '.join(self.bad_chars)}")


class InvalidSiteError(DNAError):
    """Raised when a search site is empty or not made of A, T, G, C."""




class DNASequence:
    PAIRS = {"A": "T", "T": "A", "G": "C", "C": "G"}

    def __init__(self, seq_id, sequence):
        sequence = sequence.upper().strip()
        if not sequence:
            raise EmptySequenceError("Sequence cannot be empty")
        bad = [b for b in sequence if b not in self.PAIRS]
        if bad:
            raise InvalidBaseError(bad)
        self.id = seq_id
        self.sequence = sequence

    def complement(self):
        """New DNASequence with each base paired; ID gets '_comp'."""
        comp = "".join(self.PAIRS[b] for b in self.sequence)
        return DNASequence(self.id + "_comp", comp)

    def reverse_complement(self):
        """Complement, reversed; ID gets '_revcomp'."""
        rev = self.complement().sequence[::-1]
        return DNASequence(self.id + "_revcomp", rev)

    def transcribe(self):
        """mRNA string: every T replaced by U."""
        return self.sequence.replace("T", "U")

    def find_site(self, site):
        """List of 1-based positions where site occurs (overlaps included)."""
        site = site.upper().strip()
        if not site or any(b not in self.PAIRS for b in site):
            raise InvalidSiteError(f"Invalid site: {site!r}")
        positions = []
        start = self.sequence.find(site)
        while start != -1:
            positions.append(start + 1)
            start = self.sequence.find(site, start + 1)
        return positions

    def __repr__(self):
        return f"DNASequence({self.id!r}, {self.sequence!r})"



if __name__ == "__main__":
    s2 = DNASequence("seq2", "ATGGAATTCTAG")
    print("Original:          ", s2.sequence)
    print("Complement:        ", s2.complement().sequence)
    print("Reverse complement:", s2.reverse_complement().sequence)
    print("mRNA:              ", s2.transcribe())
    print("GAATTC at:", s2.find_site("GAATTC"))
    print("TTT at:", s2.find_site("TTT"))


    print()
  
