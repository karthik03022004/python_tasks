# #     *        1 i  1 j  4 space
# #    * *       2   2   3
# #   * * *      3   3   2
# #  * * * *     4   4   1
# # * * * * *    5   5   0
# rows=5
# for i in range(1,rows+1):
#     pattern=""
#     for space in range(1,rows-i+1):
#         pattern+=" "
#     for j in range(1,i+1):
#         pattern+="*"+" "
#     print(pattern)

# # * * * * *     1   5    0
# #  * * * *      2   4    1
# #   * * *       3   3    2
# #    * *        4   2    3
# #     *         5   1    4

# for i in range(rows,0,-1):
#     pattern=""
#     for space in range(1, rows-i+1):
#         pattern+=" "
#     for j in range(1,i+1):
#         pattern+="*"+" "
#     print(pattern)



# homework task


# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
rows=5
for i in range(rows,1,-1):
    pattern=" "
    for space in range(1,rows-i+1):
        pattern+=" "
    for j in range(1,i+1):
        pattern+="*"+" "
    print(pattern)


for i in range(1,rows+1):
    pattern=" "
    for space in range(1,rows-i+1):
        pattern+=" "
    for j in range(1,i+1):
        pattern+="*"+" "
    print(pattern)


    