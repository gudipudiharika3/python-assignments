"""
HW      # 1
Problem # 2 Bioinformatics
Author  # Gudipudi HarikaPadmini
"""
import re


def find_genes(genome_string):
    """
    Takes input string and search for gene pattern using regular expression.
    :param genome_string:
    :return: List of matches for above pattern
    """
    gene_pattern = re.compile(r'ATG((?:[ACTG]{3})+?)(?:TAG|TAA|TGA)')
    gene_groups = re.findall(gene_pattern, genome_string)
    return gene_groups


if __name__ == '__main__':
    genome = input("Enter a genome string: ")
    gene_groups = find_genes(genome)
    if gene_groups:
        for gene in gene_groups:
            print(gene)
    else:
        print("no gene is found")
