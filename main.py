import core.chromosome
def main():
    chr = core.chromosome.Chromosome((-5, 5), 6)
    print(chr.get_chromosome())
    print(chr.decode_chromosome())

if __name__ == "__main__":
    main()