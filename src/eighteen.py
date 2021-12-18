from math import floor, ceil

class pair:
    def __init__(self, left, right, parent, left_or_right):
        self.left = left # another Pair or regular num
        self.right = right # another Pair or regular num
        self.parent = parent # None for root, otherwise another Pair
        self.left_or_right = left_or_right # True for left, False for right, None for root

class regular:
    # regular num
    def __init__(self, val, parent, left_or_right):
        self.val = val
        self.parent = parent # None for root, otherwise Pair
        self.left_or_right = left_or_right # True for left, False for right, None for root

def convert_to_pair_or_regular(s, parent, left_or_right):
    # converts string to a Pair
    if s[0] == "[":
        s = s[1:]
        (left, s) = convert_to_pair_or_regular(s, None, True)
        assert(s[0] == ",")
        s = s[1:]
        (right, s) = convert_to_pair_or_regular(s, None, False)
        assert(s[0] == "]")
        s = s[1:]
        cur = pair(left=left, right=right, parent=parent, left_or_right=left_or_right)
        left.parent = cur
        right.parent = cur
        return (cur, s)
    
    elif s[0].isdigit() == True:
        i = 0
        while s[i].isdigit():
            i += 1
        d = s[0:i]
        d = int(d)
        s = s[i:]
        cur = regular(val=d, parent=parent, left_or_right=left_or_right)
        return (cur, s)
    
    else:
        raise("Unexpected case in convert_to_pair, s is ", s)



def is_depth_4(num, depth):
    # print(f"in is_depth_4, depth is {depth} and type(num) is {type(num)} and type(num.left) is {type(num.left)} and type(num.rigth) is {type(num.right)}")
    assert(type(num) == pair)
    if depth == 4 and type(num) == pair and type(num.left) == regular and type(num.right) == regular:
        return (num, True)
    else:
        if type(num.left) == pair:
            l_num, l_d_4 = is_depth_4(num.left, depth+1)
            if l_d_4 == True:
                return (l_num, l_d_4)
        if type(num.right) == pair:
            r_num, r_d_4 = is_depth_4(num.right, depth+1)
            if r_d_4 == True:
                return (r_num, r_d_4)
        return (num, False)






def get_rightmost(num):
    if type(num) == regular:
        return num
    elif type(num) == pair:
        while type(num) != regular:
            num = num.right
        return num
    else:
        raise("unexpected case in get_rightmost")

def get_leftmost(num):
    if type(num) == regular:
        return num
    elif type(num) == pair:
        while type(num) != regular:
            num = num.left
        return num
    else:
        raise("unexpected case in get_leftmost")

def find_first_left(num):
    # returns first pair/regular to the left of num; returns none if nothing exists to the left of num
    while num != None and num.left_or_right == True:
        num = num.parent
    if num == None or num.left_or_right == None:
        return None
    elif num.left_or_right == False:
        return get_rightmost(num.parent.left)
    else:
        raise("unexpected case in find_first_left, num is :", num, " and num.left_or_right is :", num.left_or_right)

def find_first_right(num):
    # returns first pair/regular to the right of num; returns none if nothing exists to the right of num
    while num != None and num.left_or_right == False:
        num = num.parent
    if num == None or num.left_or_right == None:
        return None
    elif num.left_or_right == True:
        return get_leftmost(num.parent.right)
    else:
        raise("unexpected case in find_first_right, num is :", num, " and num.left_or_right is :", num.left_or_right)


def can_explode(num):
    if type(num) == pair:
        depth_num, is_depth = is_depth_4(num, 0)
    elif type(num) == regular:
        pass
    else:
        raise("unexpected case in can_explode, num is :", num, " and its type is :", type(num))

    if is_depth == True:
        assert(type(depth_num) == pair)
        assert(type(depth_num.left) == regular)
        assert(type(depth_num.right) == regular)

        l = find_first_left(depth_num)
        assert(l == None or type(l) == regular)
        if type(l) == regular:
            l.val += depth_num.left.val
        r = find_first_right(depth_num)
        assert(r == None or type(r) == regular)
        if type(r) == regular:
            r.val += depth_num.right.val
        updated_num = regular(0, depth_num.parent, depth_num.left_or_right)
        if depth_num.left_or_right == True:
            depth_num.parent.left = updated_num
        elif depth_num.left_or_right == False:
            depth_num.parent.right = updated_num
        else:
            raise("unexpected case in depth_num in can_explode; depth_num is :", depth_num, " and depth_num.left_or_right is :", depth_num.left_or_right)
        
        return True

    else:
        return False




def is_regular_10(num):
    if type(num) == regular:
        if num.val >= 10:
            return (num, True)
        else:
            return (num, False)
    
    elif type(num) == pair:
        l_num, l_reg = is_regular_10(num.left)
        if l_reg == True:
            return (l_num, l_reg)
        r_num, r_reg = is_regular_10(num.right)
        if r_reg == True:
            return (r_num, r_reg)
        return (num, False)

    else:
        raise("unexpected case in is_regular_10")

def split_num(num):
    updated_num = pair(left = regular(val=int(floor(num.val/2)), left_or_right=True, parent=None),
                       right = regular(val=int(ceil(num.val/2)), left_or_right=False, parent=None),
                       left_or_right = num.left_or_right,
                       parent = num.parent)
    updated_num.left.parent = updated_num
    updated_num.right.parent = updated_num
    if num.left_or_right == True:
        num.parent.left = updated_num
    elif num.left_or_right == False:
        num.parent.right = updated_num
    else:
        raise("unexpected case in split_num")


def can_split(num):
    if type(num) == regular:
        if num.val >= 10:
            split_num(num)
            return True
    elif type(num) == pair:
        reg_num, is_reg = is_regular_10(num)
        if is_reg:
            split_num(reg_num)
            return True
        else:
            return False
    else:
        raise("unexpected case in can_split")





def reduce(num):
    while can_explode(num) or can_split(num):
        pass



def add_2(s1, s2):
    s1_num, s1 = convert_to_pair_or_regular(s1, parent=None, left_or_right=None)
    s2_num, s2 = convert_to_pair_or_regular(s2, parent=None, left_or_right=None)
    added = pair(left=s1_num, right=s2_num, left_or_right=None, parent=None)
    s1_num.parent = added
    s1_num.left_or_right = True
    s2_num.parent = added
    s2_num.left_or_right = False
    reduce(added)
    return added




def add(strs):
    assert(type(strs) == list)
    if len(strs) == 1:
        reduce(strs[0])
        return strs[0]
    else:
        c, _ = convert_to_pair_or_regular(strs[0], parent=None, left_or_right=None)
        for i in range(1, len(strs)):
            c = add_2(c, strs[i])
        return c



















def calc_magnitude(num):
    assert(type(num) == pair or type(num) == regular)
    if type(num) == pair:
        return 3*calc_magnitude(num.left) + 2*calc_magnitude(num.right)
    elif type(num) == regular:
        return num.val



def get_largest(strs):
    max_mag = 0
    for i in range(len(strs)):
        for j in range(len(strs)):
            if i != j:
                max_mag = max(max_mag, calc_magnitude(add_2(strs[i], strs[j])))
    print(f"max_mag is {max_mag}")


def get_strs(filename):
    with open(filename) as f:
        lines = f.readlines()
        strs = [line.strip() for line in lines]
        print(f"strs is {strs}")
    return strs





strs = get_strs("/home/harsh/now/aoc/aoc_2021/txts/eighteen.txt")
get_largest(strs)














