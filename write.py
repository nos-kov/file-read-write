###################################### Write to File

import os

sorting = {}

for filename in os.listdir(os.getcwd()):
    if filename.endswith('.txt') and filename != "recipes.txt":
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            for count, line in enumerate(f):
                pass
            sorting[filename] = count + 1


sorted_sorting = sorted(sorting.items(), key=lambda x:x[1])
print(sorted_sorting)
for element in sorted_sorting:
    with open(os.path.join(os.getcwd(), element[0]), 'r') as f, open(os.path.join(os.getcwd(), "result.txt"), 'a') as result:

        result.write(element[0] + '\n')
        result.write(str(element[1]) + '\n')
        for line in f:
            result.write(line.strip() + '\n')



            