

print("----------------INDEX---------------------")
index = int(input("Input the weight:"))
if index == 25:
    import weight25
elif index == 50:
    import weight50
elif index == 75:
    import weight75
elif index == 100:
    import weight100
elif index == 666:
    print("Copyright(c) MORI LAB")
else:
    print("---\033[1;35m bad command \033[0m!---")
print("----------------OVER----------------------")