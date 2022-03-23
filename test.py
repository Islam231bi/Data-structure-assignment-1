from GenerateArray import Generate

gen = Generate()
list_samples_quick = [gen.generate(1000), gen.generate(10000), gen.generate(25000), gen.generate(50000),
                      gen.generate(75000), gen.generate(100000)]
list_samples_merge = list_samples_quick[:]
list_samples_insertion = list_samples_quick[:]
list_samples_bubble = list_samples_quick[:]
