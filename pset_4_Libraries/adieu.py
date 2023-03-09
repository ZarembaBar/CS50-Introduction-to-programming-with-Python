import inflect

p = inflect.engine()
name_list = []
while True:
    try:
        x = input("Input: ")
        name_list.append(x)
    except EOFError:
        name_list = p.join(name_list)
        break
print("Adieu, adieu, to " + p.inflect(name_list))
