# import pysam 
import re 
from collections import defaultdict

## Rosalind Problems:
## Problem Set: Python Village 

#Q1: Conditions and Loops
#Given: Two positive integers a and b (a<b<10000).
#Return: The sum of all odd integers from a through b, inclusively.

# a = 4880
# b = 9500
# c = 0 

# for i in range(a,b+1):
#     if i%2 != 0:
#         c += i
# print(c)

#Q2: Working with files
# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
# i = 1
# file = open("rosalind_ini5.txt", "r")
# file_out = open("out_file_even_lines.txt", "w")

# for line in file:
#     # print(line.strip())
#     if i%2 == 0:
#         file_out.write(line)
#     i += 1

#Q3: Python Dictionaries
#Given: A string s of length at most 10000 letters.
#Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

# s = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
# s = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
# string_list = s.split()
# counts_dict = {}
# for i in string_list:
#     if i not in counts_dict:
#         counts_dict[i] = 1
#     else:
#         counts_dict[i] += 1 

# print(counts_dict)

# for key, value in counts_dict.items():
#     print(key, value)

#Problem Set: Bioinformatics Stronghold
#Q1: Counting DNA Nucleotides
# s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
# s = "TACGTGCTGTGTCATGTGTTACCGAATGGCGAATGATCCGACAGTCGCATTGTCGTCCTTAAATACGTGGGTGCCGTAGTAGAGTCCGTATTTTTCCAGTGCACTTATAAAGCTTCACCATGTATCCTGAAGTAGACGATAGTCGTCTAAGTCCAACGGCGTGACGATCCAAGCGTACTAGCACACTACGACCCTAACAAGATTATGACAGCCTGCGGAGCTGTAACATTGCATAGCCTCATGACATTTTGTTTATAATGTCTACTCGAACGCGCCGACGACGTAAAACCGAACGCCGGTGAGTACAACCTGAAGTCTTCCTAGGTCCAACTTTCCTAGATTAGCACGGTCTCGGGTCAATACGTTTGTGGATGACTAACAGACCGCTACCCCGTATAGGAAAGCCGATTACATCGCGTTAGGAACGACCACCAAACGTATAAACTTAATAATCCTTAAGCAGTCCTTCTGGAGCACGTCTGGCACAGAGCACGCTAGGCACTTTTGGAGCTAGTAGGCTAGAATTAGCCAGCTGTCATTCTCAATAATCCTATCACAGACTCCCTCAAACGTACTACGGAAGACTTGAACCCAAGAACCCCACACCGGACCAGGAATGACTCAGACTTAGGGTAACCTATTTTTTCCGCAGGGGTTATCGCGGCCTAGACGTAGTCAATAGAGTATAGAGGGTGTACAGGACTCCCTCAGGGAGACGCTATAAGTTGATTGTTCGGAGACTATTGTTTTGTAGTCTGTGGACGGTTGTGCAATTGTTTGATACACATGATAAAAGTGTCTCTCACGCTAGTTTTAGTACAACAATGCCTTCTAGGTTGTTAGGTTAGCCCCATTGCCCGTGAATATTGGTACGACGATACCTCAAAGCGCGTGGCGTCTGTGGAACACGTGGAAAGT"

# all_caps = s.upper()
# print(all_caps.count("A"))
# print(all_caps.count("C"))
# print(all_caps.count("G"))
# print(all_caps.count("T"))

#Q2: Transcribing DNA into RNA   
## Return RNA string given DNA string (replace T with U)

# t = "ATGCGTTGGGCAAAAGGTTAGACTCCTTGCTATCTGACGGACCCCACTAAGATGTGTCTCGTCATACAGACTTCTGTCCTACAAGACTAGAATAAAGGAAATCTGATGGGCCAATTAGGACATTACAGACGCGACTTTAGTTAAAATACTGTGTGGGGCCCACTCCTCGTCTCCCCGTAAAGGACTGAGTCCCGGAGTTGGTGTTGGCCAGACGATGCCTATCTAAGCCAGACAGTTATAGAAGGCAAGTAAGACGGCCCTTCACATAGTGGACGCGATGCCATTGGGTAGAACCGTATCGCTTGAAGGGAGATCATAGCTGGTTCAAGCAAGATTACAAGTCGTGGATCAGGAGGTGATGGGGGACTCAAATCACCCTCGGGTGGAGGCCGTTCTACTCGGTCATCAGTCAGCTTGGACTATCCTTAATTGGTTCGATAATCTCGGAACAGGACGGCCGGACAGGCGGGTACCCCCCCAGATATAAGTACGACTTCACTCCCAACTAACAGCTCCCCTCTAATGCGTCGCCGTGATCGTGAGTTCTGAGTATCAGGCCATCTCAACGAAGTATATTCATAACTAAGCGTGCTATCTAGGGCCCCAGGTAATGTTGCTATGGTCACGGTTCTTAAAGTCTCCAGTGATGAGAGACTCCCTGGTGCCAGGTGGAAAAACCGTAGTATGAGAAATAACTATTCTGTGTTACCGAGCCGGGATACTTCTGTGATGACATTCTACCGGAGGGGCGCTATGCATTGGCAAACCGCATTTGACACGAACATGTTGCCCTATGTGGTTCGGTATGCAAACAGAGCAGGCGGGACCAGAGTTCCCAGCAGTCATGGCGAGGTGTGAGCACGGTCACATTGGAAACAACAAAAATTGAAAGGCTTGTAGGGGTGGTCTAGAGCGGGTTGAAGCATCATGCGAGTTCTGCTCTCCAAGTGCACCTCAGCCC"
# u = t.upper().replace("T", "U")
# print(u)

#Q3: Complementing a Strand of DNA 
# s = "TTGGTACGCCAGACCCCAGACATTTGCACAACGGCCATCGACGCACTCGAATGGACTTATCGATTGGCAGCTTCGCGCAGCCTCGACCCCAGTTCGGACCCAAATTTCTCGGTGTCGTGAGTGAGTACAACTGCCGGGAGGTTGTTGGCATTGGATTGACGGTGACGGGTATGCATGACCTGAGTAGCACCCCCGTATAGAGTTATTGCGATAGGCGATCGTCGCATTTCTACGATTTGCTGAACTTTCTCGGACGTCACTGCAACGAAGTTTTGGAATACATCATCACGTGTCCAAACAGAGAACTTAGACGGCCTTAGGAGATAGACCACACGCCCCAGTATGGGCGTCAATAAATAGGAGTTAACAAGATTAATTGAGCAAGCGTAAGTCCCTGCCGACTGCTGGAGAGTCGAGACGAGAGTTCTCGGGATTGTGTTCTCCAGCTGTGTCATGAGGTTGCCCCGACCTACGCCACGGCGTCTTTAGGGCAATTCGCAGTTTCGGTGTACATCTATGGCACCGACATGCGTCTAGCGGGCGGCTTTCCGTGAAATAGGCATAGTGTTAGCAGAGTCGCGATAAGTAATTGCCCAACCCCTGTCAGACACGGAATCATCGCTAGTTTAGCGCAGTCTTTACCAGCGTTACAACAATCACTAATCTTTCTCTTTCGGTGCGGCACGACCCATAGCATGTTACCACCACAGGACAAACTCCTTACTCACAAGGTATTGAGCGTGGGCAAATATGACCATTTACTAATTGTATAGGACACTACGAATGAGCTACTACGTAGCGCCCTGGCCGGGTCACCTGCTTCGTGTCACTTCGTACCTAGACGAGCATCTATGATCATAACCCTCTCCCAGCCGGGCGGGCCACCCGGATTTCGTTATATCTTACTTACCCCGTTAGCTTACCCCCGGTTTTCCTGCGGGAACAACTCCTTGTAGCAGTGTCACGACTATAATATAGC"
# # print(s)
# rev_s = s[::-1]
# complement = {"A":"T", "T":"A", "G":"C", "C":"G"}
# compl_list = [complement[i] for i in rev_s]
# print("".join(compl_list))


#Q4: Rabbits and Recurrence Relations:

def fib(n,k):
    f = [1] * n
    for i in range(2,n):
        f[i] = f[i-1] + f[i-2] * k
    return f[n-1]

def fib2(n, k):
    return 1 if n < 3 else fib(n-1, k) + fib(n-2, k)*k

# print(fib2(30,2))

#Q5: Mortal Fibonacci Rabbits
def mortal_rabbits(n,m):
    f = [0,1,1] 
    for i in range(3,n + 1):
        if i <= m:
            total = f[i-1] + f[i-2]
        elif i == m + 1:
            total = f[i-1] + f[i-2] - 1
        else:
            total = f[i-1] + f[i-2] - f[i-m-1]
        f.append(total)
    return f[n]
    # print(f[n-1])

# print(mortal_rabbits(88,17))

#Q6: Computing GC content
##Parse Fasta properly:
filename = "rosalind_gc.txt"
sequences = defaultdict(str)
with open(filename) as f:
    lines = f.readlines()

current_tag = None
for line in lines:
    m = re.match('^>(.+)', line)

    if m:
        current_tag = m.group(1)
    else:
        seq = line.strip()
        sequences[current_tag] += seq
        
another_dict = {}

for k,v in sequences.items():
    g = v.upper().count("G")
    c = v.upper().count("C")
    tot_gc = g+c
    percent_gc = (tot_gc / len(v))*100
    another_dict[k] = percent_gc

# print(another_dict)
max_val = max(another_dict.values())
max_keys = [k for k, v in another_dict.items() if v == max_val]
print(max_keys[0])
print(max_val)
