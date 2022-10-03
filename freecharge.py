dependency=[("math.c","algeb.c"),("math.c","geo.c"),("geo.c","p.c"),("algeb.c","p.c")]


def get_dependency(dependency):
    dep = {}
    all=[]
    for i in dependency:
        if i[0] not in dep:
            dep[i[0]] = []
        dep[i[0]].append(i[1])
        if i[0] not in all:
            all.append(i[0])
        if i[1] not in all:
            all.append(i[1])
    return dep,all

def get_dependency_order(dependency):
    dep,all = get_dependency(dependency)
    order = []
    while len(all) > 0:
        for i in all:
            if i not in dep:
                order.append(i)
                all.remove(i)
                for j in dep:
                    if i in dep[j]:
                        dep[j].remove(i)
                break
    return order

#print(get_dependency(dependency))
print(get_dependency_order(dependency))