print('NOTE: do not enter U values into the DNA triplet input.')
print('\n')
DNA = input('DNA triplet: ').upper()

mrna_table = str.maketrans({'A': 'U', 'G': 'C', 'C': 'G', 'T': 'A'})
trna_table = str.maketrans({'T': 'U'})
MRNA = DNA.translate(mrna_table)
print('mRNA codon: ' + MRNA)

print('tRNA anticodon: ' + DNA.translate(trna_table))

MRNA_LIST = MRNA.lower().split()

codon_dict = {
    'uuu': 'phe',
    'uuc': 'phe',
    'uua': 'leu',
    'uug': 'leu',
    'ucu': 'ser',
    'ucc': 'ser',
    'uca': 'ser',
    'ucg': 'ser',
    'uau': 'tyr',
    'uac': 'tyr',
    'uaa': 'stop',
    'uag': 'stop',
    'ugu': 'cys',
    'ugc': 'cys',
    'uga': 'stop',
    'ugg': 'trp',
    'cuu': 'leu',
    'cuc': 'leu',
    'cua': 'leu',
    'cug': 'leu',
    'ccu': 'pro',
    'ccc': 'pro',
    'cca': 'pro',
    'ccg': 'pro',
    'cau': 'his',
    'cac': 'his',
    'caa': 'gln',
    'cag': 'gln',
    'cgu': 'arg',
    'cgc': 'arg',
    'cga': 'arg',
    'cgg': 'arg',
    'auu': 'ile',
    'auc': 'ile',
    'aua': 'ile',
    'aug': 'met',
    'ggg': 'gly',
    'ggc': 'gly',
    'gga': 'gly',
    'ggu': 'gly',
    'gag': 'glu',
    'gaa': 'glu',
    'gac': 'asp',
    'gau': 'asp',
    'gcg': 'ala',
    'gcc': 'ala',
    'gca': 'ala',
    'gcu': 'ala',
    'gug': 'val',
    'guc': 'val',
    'gua': 'val',
    'guu': 'val',
    'agg': 'arg',
    'aga': 'arg',
    'agc': 'ser',
    'agu': 'ser',
    'aag': 'lys',
    'aaa': 'lys',
    'aac': 'asn',
    'aau': 'asn',
    'acg': 'thr',
    'aca': 'thr',
    'acc': 'thr',
    'acu': 'thr'
}

print('amino acid: ' + ' '.join(codon_dict[MRNA]
                                for MRNA in MRNA_LIST).upper())
