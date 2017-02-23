def to_rna(dna):
  
  dna_to_rna = {"G": "C", "C": "G", "T": "A", "A": "U"}
  
  try:
    return "".join(dna_to_rna[x] for x in dna)
  except KeyError:
    return ""
