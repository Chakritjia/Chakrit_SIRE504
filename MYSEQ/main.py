from seqbio.calculation.SeqCal import *
from seqbio.pattern.SeqPattern import *
from seqbio.seqMan.dnaconvert import *

def argparserLocal():
    from argparse import ArgumentParser
    '''Argument parser for the commands'''
    parser = ArgumentParser(prog='myseq', description='Work with seqeunce')

    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:',
        dest='command'
    )
    subparsers.required = True

    cgc_command = subparsers.add_parser('gcContent', help='Calcalate GC content')
    cgc_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide seqence")
    
    cb_command = subparsers.add_parser('countBases', help='Count number of each base')
    cb_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide seqence")
    cb_command.add_argument("-r", "--revcomp", action='store_true',
                             help="Convet DNA to reverse-complementary")
    
    transc_command = subparsers.add_parser('transcription', 
                                          help='Convert DNA->RNA')
    transc_command.add_argument("-s", "--seq", type=str, default=None, 
                               help="Provide sequence")
    transc_command.add_argument("-r", "--revcomp", action='store_true', 
                               help="Convert DNA to reverse-complementary")
    
    transl_command = subparsers.add_parser('translation', 
                                          help='Convert DNA->Protein')
    transl_command.add_argument("-s", "--seq", type=str, default=None, 
                               help="Provide sequence")
    transl_command.add_argument("-r", "--revcomp", action='store_true', 
                               help="Convert DNA to reverse-complementary")
    
    enz_command = subparsers.add_parser('enzTargetsScan', help='Find restriction enzyme')
    enz_command.add_argument("-s", "--seq", type=str, default=None, 
                             help="Provide sequence")
    enz_command.add_argument("-e", "--enz", type=str, default=None, 
                             help="Enzyme name")
    enz_command.add_argument("-r", "--revcomp", action='store_true', 
                             help="Convert DNA to reverse-complementary")
    
    #parser.print_help()
    return parser

def main():
    parser = argparserLocal()
    args = parser.parse_args()
    
    
    if args.seq is None:
        print("error please put your command")
        return
    
    print('Input', args.seq)
    seq = args.seq.upper()

    if args.command == 'gcContent':
        print("GC Content =", gcContent(seq))
    
    elif args.command == 'countBases':
        if args.revcomp:
            rev_seq = reverseComplementSeq(seq)
            print("Count Bases =", countBasesDict(rev_seq))
        else:
            print("Count Bases =", countBasesDict(seq))

    elif args.command == 'enzTargetsScan':
        if args.revcomp:
            print("EcoRI sites =", enzTargetsScan(reverseComplementSeq(seq), 'EcoRI'))
        else:
            print("EcoRI sites =", enzTargetsScan(seq, 'EcoRI'))

    elif args.command == 'transcription':
        if args.revcomp:
            print("Transcription =", dna2rna(reverseComplementSeq(seq)))
        else:
            print("Transcription =", dna2rna(seq))

    elif args.command == 'translation':
        if args.revcomp:
            print("Translation =", dna2protein(reverseComplementSeq(seq)))
        else:
            print("Translation =", dna2protein(seq))

if __name__ == "__main__":
    main()
