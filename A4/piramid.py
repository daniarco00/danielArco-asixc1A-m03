

"""
S'imprimeix una piràmide d'altura N de #
input 5
output
#
# #
# # #
# # # #
# # # # #

"""

variable = int(input())

for x in range(1,variable+1):
# Quitar linea final
    if x==variable:
        print("#" * x,end="")
    else:
        print("#" * x)

