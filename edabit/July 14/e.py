def to_array(n):
    return [i.strip() for i in n.split(',')]
print(to_array('watermelon,     rasberry,   orange'))