never_heard, never_seen = map(int, input().split())
dict = {}
off_brand_list = []
off_brand_count = 0
for i in range(never_heard):
    name = input().strip()
    dict[name] = "never_heard"
for i in range(never_seen):
    name = input().strip()
    if name in dict.keys():
        dict[name] = "off_brand"
        off_brand_count += 1
    else:
        dict[name] = "never_seen"
print(off_brand_count)
for k, v in dict.items():
    if v == "off_brand":
        off_brand_list.append(k)

for i in sorted(off_brand_list):
    print(i)

        