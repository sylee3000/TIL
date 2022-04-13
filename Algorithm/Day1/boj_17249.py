taebo=input()
face_start=taebo.find("(")
face_end=taebo.find(")")
print(taebo[:face_start].count("@"), taebo[face_end:].count("@"))