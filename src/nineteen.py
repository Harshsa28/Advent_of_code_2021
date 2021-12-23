import copy


def matrix(locs):
    mat = [[None for i in range(len(locs))] for j in range(len(locs))]
    red = [[None for i in range(len(locs))] for j in range(len(locs))]
    for i in range(len(locs)):
        for j in range(len(locs)):
            temp = (locs[j][0]-locs[i][0], locs[j][1]-locs[i][1], locs[j][2]-locs[i][2])
            #mat[i][j] = (temp, (locs[j], locs[i]))
            mat[i][j] = locs[j]
            temp1 = sorted(list(map(abs, temp)))
            s = ""
            for t in temp1:
                s += str(t)
            red[i][j] = (s, (i, j))
        red[i] = sorted(red[i], key=lambda x: x[0])
    return (mat, red)

def get_mat(locs):
    mat = [[None for i in range(len(locs))] for j in range(len(locs))]
    for i in range(len(locs)):
        for j in range(len(locs)):
            mat[i][j] = locs[j]
    return mat

def get_red_from_mat(mat):
    red = [[None for j in range(len(mat[i]))] for i in range(len(mat))]
    locs = mat[0]
    for i in range(len(locs)):
        for j in range(len(locs)):
            temp = (locs[j][0]-locs[i][0], locs[j][1]-locs[i][1], locs[j][2]-locs[i][2])
            temp1 = sorted(list(map(abs, temp)))
            s = ""
            for t in temp1:
                s += str(t)
            red[i][j] = (s, (i, j))
        red[i] = sorted(red[i], key=lambda x: x[0])
    return red





def cmp_reds(red1, mat1, red2, mat2):
    for i1 in range(len(red1)):
        for i2 in range(len(red2)):
            j1 = 0
            j2 = 0
            c = 0
            red1_i1 = red1[i1]
            red2_i2 = red2[i2]
            eq1 = []
            eq2 = []
            while j1 < len(red1_i1) and j2 < len(red2_i2):
                if red1_i1[j1][0] == red2_i2[j2][0]:
                    #eqs.append((mat1[red1_i1[j1][1][0]][red1_i1[j1][1][1]][1][0], mat2[red2_i2[j2][1][0]][red2_i2[j2][1][1]][1][0]))
                    eq1.append(mat1[red1_i1[j1][1][0]][red1_i1[j1][1][1]])
                    eq2.append(mat2[red2_i2[j2][1][0]][red2_i2[j2][1][1]])
                    #eqs.append((mat1[red1_i1[j1][1][0]][red1_i1[j1][1][1]], mat2[red2_i2[j2][1][0]][red2_i2[j2][1][1]]))
                    c += 1
                    j1 += 1
                    j2 += 1
                else:
                    if red1_i1[j1][0] < red2_i2[j2][0]:
                        j1 += 1
                    elif red1_i1[j1][0] > red2_i2[j2][0]:
                        j2 += 1
                    else:
                        raise("unexpected case in cmp_mats")
            if c == 12:
                #print("found match")
                return (eq1, eq2)
    #raise("didn't find match")
    return None



def try_24(d):
    a, b, c = d
    #pos = [(a, b, c), (a, c, -b), (a, -b, -c), (a, -c, b), (-a, -b, c), (-a, c, b), (-a, b, -c), (-a, -c, -b), (b, -a, c), (b, c, a), (b, a, -c), (b, -c, -a), (-b, a, c), (-b, c, -a), (-b, -a, -c), (-b, -c, a), (c, b, -a), (c, -a, -b), (c, -b, a), (c, a, b), (-c, b, a), (-c, a, -b), (-c, -b, -a), (-c, -a, b)]
    #pos = [(a, b, c), (a, c, -b), (a, -b, -c), (a, -c, b), (-a, -b, c), (-a, c, b), (-a, b, -c), (-a, -c, -b), (b, -a, c), (b, c, a), (b, a, -c), (b, -c, -a), (-b, a, c), (-b, c, -a), (-b, -a, -c), (-b, -c, a), (c, b, -a), (c, -a, -b), (c, -b, a), (c, a, b), (-c, b, a), (-c, a, -b), (-c, -b, -a), (-c, -a, b)]
    pos = [(a, b, c), (-a, b, c), (a, -b, c), (a, b, -c), (a, -b, -c), (-a, b, -c), (-a, -b, c), (-a, -b, -c), (a, c, b), (-a, c, b), (a, -c, b), (a, c, -b), (a, -c, -b), (-a, c, -b), (-a, -c, b), (-a, -c, -b), (b, a, c), (-b, a, c), (b, -a, c), (b, a, -c), (b, -a, -c), (-b, a, -c), (-b, -a, c), (-b, -a, -c), (c, a, b), (-c, a, b), (c, -a, b), (c, a, -b), (c, -a, -b), (-c, a, -b), (-c, -a, b), (-c, -a, -b), (b, c, a), (-b, c, a), (b, -c, a), (b, c, -a), (b, -c, -a), (-b, c, -a), (-b, -c, a), (-b, -c, -a), (c, b, a), (-c, b, a), (c, -b, a), (c, b, -a), (c, -b, -a), (-c, b, -a), (-c, -b, a), (-c, -b, -a)]
    return pos


def try_num(d, num):
    pos = try_24(d)
    return pos[num]


def try_pos(eq1, eq2):
    assert(len(eq1) == len(eq2) == 12)
    assert(len(eq1[0]) == len(eq2[0]) == 3)
    loc = (eq1[0][0]-eq2[0][0], eq1[0][1]-eq2[0][1], eq1[0][2]-eq2[0][2])
    for i in range(1, len(eq1)):
        temp = (eq1[i][0]-eq2[i][0], eq1[i][1]-eq2[i][1], eq1[i][2]-eq2[i][2])
        if temp != loc:
            return None
    return loc

def get_loc(eq1, eq2):
    eq2_pos = [try_24(d) for d in eq2]
    assert(len(eq2_pos[0]) == 48)
    for i in range(len(eq2_pos[0])):
        loc = try_pos(eq1, [x[i] for x in eq2_pos])
        if loc != None:
            #print(f"loc is {loc}")
            return (loc, i)
    #print("nothing worked")
    return None




def pre(s):
    locs = [None for _ in range(len(s))]
    for i in range(len(s)):
        locs[i] = list(map(int, s[i].split(",")))
        assert(len(locs[i]) == 3)
    return locs


def preprocess(scanners):
    locs = [None for _ in range(len(scanners))]
    for i in range(len(scanners)):
        s = scanners[i]
        locs[i] = [None for i in range(len(s))]
        for j in range(len(s)):
            locs[i][j] = list(map(int, s[j].split(",")))
            assert(len(locs[i][j]) == 3)
    return locs


def get_data(filename):
    scanners = [[]]
    scan_index = 0
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            if line == "\n":
                scanners.append([])
                scan_index += 1
            elif line[0] == "-" and line[1] == "-":
                pass
            elif line[0].isdigit() or line[0] == "-":
                scanners[scan_index].append(line[:-1])
            else:
                raise(f"unexpected case, line is {line}")
    return scanners
    #return [scanners[x] for x in [25, 30, 33, 20, 14, 22]] # 20
    #return [scanners[x] for x in [1,4,3,0,2]]


def get_mats_reds(locs):
    mats = [None for _ in range(len(locs))]
    reds = [None for _ in range(len(locs))]
    for i in range(len(locs)):
        mats[i], reds[i] = matrix(locs[i])
    return (mats, reds)





def get_locs(reds, mats, c):
    assert(len(reds) == len(mats))
    solved = [0]
    unsolved = [x for x in range(len(reds)) if x not in solved]
    beacons = mats[0][0]
    checks = 0
    while len(unsolved) > 0:
        checks += 1
        if checks > len(unsolved) + 10:
            print(f"going into new, solved is {solved} and unsolved is {unsolved} and checks is {checks}")
            new_beacons = []
            for b in beacons:
                if b not in new_beacons:
                    new_beacons.append(b)
            new_reds = [copy.deepcopy(reds[l]) for l in unsolved]
            new_mats = [copy.deepcopy(mats[l]) for l in unsolved]
            return get_locs(new_reds, new_mats, len(new_beacons))
            #break
        for j in solved:
            i = unsolved[0]
            eqs = cmp_reds(reds[j], mats[j], reds[i], mats[i])
            if eqs is not None:
                eq_j, eq_i = eqs
                loc, num = get_loc(eq_j, eq_i)
                if loc is not None:
                    print(f"it worked for {j} and {i}, loc is {loc}")
                    checks = 0
                    solved.append(i)
                    unsolved.pop(0)
                    #print(len(mats), len(mats[0]), len(mats[0][0]), len(mats[0][0][0]))
                    #print(len(mats[i]), len(mats[i][0]), len(mats[i][0][0]))
                    #print(f"mats is {mats}")
                    #print(f"mats[i] is {mats[i]}")
                    #mats[i] = [try_num(x, num) for x in mats[i]]
                    for t1 in range(len(mats[i])):
                        for t2 in range(len(mats[i][t1])):
                            temp = try_num(mats[i][t1][t2], num)
                            mats[i][t1][t2] = [temp[0]+loc[0], temp[1]+loc[1], temp[2]+loc[2]]
                    beacons.extend(mats[i][0])
                    reds[i] = get_red_from_mat(mats[i])
                    break
            temp = unsolved.pop(0)
            unsolved.append(temp)
            continue


    '''

            if eqs is not None:
                eq_j, eq_i = eqs
            else:
                #unsolved = unsolved[1:] + [unsolved[0]]
                temp = unsolved.pop(0)
                unsolved.append(temp)
                continue
            loc, num = get_loc(eq_j, eq_i)
            if loc is not None:
                print(f"it worked for {j} and {i}, loc is {loc}")
                solved.append(i)
                unsolved.pop(0)
                #print(len(mats), len(mats[0]), len(mats[0][0]), len(mats[0][0][0]))
                #print(len(mats[i]), len(mats[i][0]), len(mats[i][0][0]))
                #print(f"mats is {mats}")
                #print(f"mats[i] is {mats[i]}")
                #mats[i] = [try_num(x, num) for x in mats[i]]
                for t1 in range(len(mats[i])):
                    for t2 in range(len(mats[i][t1])):
                        temp = try_num(mats[i][t1][t2], num)
                        mats[i][t1][t2] = [temp[0]+loc[0], temp[1]+loc[1], temp[2]+loc[2]]
                beacons.extend(mats[i][0])
                reds[i] = get_red_from_mat(mats[i])
                break
            else:
                temp = unsolved.pop(0)
                unsolved.append(temp)
                continue
    '''
    new_beacons = []
    for b in beacons:
        if b not in new_beacons:
            new_beacons.append(b)
    #print(f"new_beacons is {new_beacons}")
    #print(f"len(new_beacons) is {len(new_beacons)}")
    c += len(new_beacons)
    return c







scanners = get_data("/home/harsh/now/aoc/aoc_2021/txts/nineteen.txt")
#print(scanners)
locs = preprocess(scanners)
#print(f"locs is \n{locs}")
#mat, red1 = matrix(locs[0])
#red2 = get_red_from_mat(mat)
#print(red1 == red2)
mats, reds = get_mats_reds(locs)
# print(f"reds is \n{reds}")
print(get_locs(reds, mats, 0))
'''


#eq0, eq1 = cmp_reds(reds[0], mats[0], reds[1], mats[1])
#get_loc(eq0, eq1)



with open("/home/harsh/now/aoc/aoc_2021/txts/nineteen_s0_all.txt") as f:
    strs = f.readlines()
    print(f"strs is {strs}")
    locs0 = pre(strs)

m0, red0 = matrix(locs0)
#print(red1)


with open("/home/harsh/now/aoc/aoc_2021/txts/nineteen_s1_all.txt") as f:
    strs = f.readlines()
    locs1 = pre(strs)

m1, red1 = matrix(locs1)
#print(red2)


eq0, eq1 = cmp_reds(red0, m0, red1, m1)
get_loc(eq0, eq1)


new_eq0, new_eq1 = cmp_reds(reds[0], mats[0], reds[1], mats[1])
get_loc(new_eq0, new_eq1)

'''
