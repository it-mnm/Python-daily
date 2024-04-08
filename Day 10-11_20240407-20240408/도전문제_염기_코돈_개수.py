dna = "ctacaatgtcagtatacccattgcattagccgg"
output = {}
print(len(dna)) # 33

for i in range(0,len(dna),3):
    # 3글자씩 추출
    codon = dna[i:i+3]
    # 딕셔너리에 키가 없을 경우에 추가
    if codon not in output:
        output[codon] = 0
    output[codon] += 1
print(output)