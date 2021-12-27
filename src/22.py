import re


class Axis:
    def __init__(self, l, r): 
        self.l = l 
        self.r = r 

    def intersect(self, other):
        # returns True if self (axis) intersects with other (axis)
        return (self.l >= other.l and self.r <= other.r) or \
                (self.l < other.l and self.r >= other.l and self.r <= other.r) or \
                (other.l < self.l and other.r >= self.l and other.r <= self.r) or \
                (other.l >= self.l and other.r <= self.r)

    def is_empty(self):
        return self.l > self.r

    def common(self, other):
        # returns common axis between self and other
        if self.l >= other.l and self.r <= other.r:
            return Axis(self.l, self.r)
        elif self.l < other.l and self.r >= other.l and self.r <= other.r:
            return Axis(other.l, self.r)
        elif other.l < self.l and other.r >= self.l and other.r <= self.r:
            return Axis(self.l, other.r)
        elif other.l >= self.l and other.r <= self.r:
            return Axis(other.l, other.r)
        else:
            raise("unexpected case in common")

class Range:
    def __init__(self, on_off, x, y, z): 
        # on_off is bool. x, y, z are objects of class axis
        self.on_off = on_off
        self.x = x 
        self.y = y 
        self.z = z 
        self.x1 = x.l
        self.x2 = x.r
        self.y1 = y.l
        self.y2 = y.r
        self.z1 = z.l
        self.z2 = z.r

    def is_empty(self):
        return self.x.is_empty() or self.y.is_empty() or self.z.is_empty()

    def intersect(self, other):
        # returns True if self intersects with other. False otherwise
        # return self.x.intersect(other.x) and self.y.intersect(other.y) and self.z.intersect(other.z)
        return (((self.x1 >= other.x1 and self.x1 <= other.x2) or (other.x1 >= self.x1 and other.x1 <= self.x2)) and \
                ((self.y1 >= other.y1 and self.y1 <= other.y2) or (other.y1 >= self.y1 and other.y1 <= self.y2)) and \
                ((self.z1 >= other.z1 and self.z1 <= other.z2) or (other.z1 >= self.z1 and other.z1 <= self.z2)))
                

    def common(self, other):
        return Range(other.on_off, self.x.common(other.x), self.y.common(other.y), self.z.common(other.z))

    def minus(self, common):
        # remember to give priority to common
        parts = []
        # 1
        parts.append(Range(self.on_off, Axis(self.x.l, self.x.r), Axis(self.y.l, self.y.r), Axis(self.z.l, common.z.l-1)))
        # 2
        parts.append(Range(self.on_off, Axis(self.x.l, self.x.r), Axis(self.y.l, self.y.r), Axis(common.z.r+1, self.z.r)))
        # 3
        parts.append(Range(self.on_off, Axis(self.x.l, self.x.r), Axis(self.y.l, common.y.l-1), Axis(common.z.l, common.z.r)))
        # 4
        parts.append(Range(self.on_off, Axis(self.x.l, self.x.r), Axis(common.y.r+1, self.y.r), Axis(common.z.l, common.z.r)))
        # 5
        parts.append(Range(self.on_off, Axis(self.x.l, common.x.l-1), Axis(common.y.l, common.y.r), Axis(common.z.l, common.z.r)))
        # 6
        parts.append(Range(self.on_off, Axis(common.x.r+1, self.x.r), Axis(common.y.l, common.y.r), Axis(common.z.l, common.z.r)))

        # TODO: check if any part is empty?
        parts = [p for p in parts if not p.is_empty()]

        return parts

    def num_of_cubes(self):
        '''
        print("in num_on_cubes")
        self.display()
        '''
        if self.on_off is True:
            return (self.x.r - self.x.l + 1) * (self.y.r - self.y.l + 1) * (self.z.r - self.z.l + 1)
        else:
            return 0
    
    def display(self):
        print(f"printing {self}, on_off is {self.on_off}, x axis is {self.x.l, self.x.r}, y axis is {self.y.l, self.y.r} and z axis is {self.z.l, self.z.r}")

def flow(ranges):
    lst_A = [ranges[0]]
    lst_B = ranges[1:]

    while len(lst_B) > 0:
        B = lst_B.pop(0)
        intersected = False

        for A in lst_A:
            if A.intersect(B):
                #print("we have intersection")
                '''
                print("A is ")
                A.display()
                print("B is ")
                B.display()
                '''
                intersected = True

                common = A.common(B)
                # put common in lst_A
                lst_A.append(common)
                '''
                print("common is ")
                common.display()
                '''

                A_minus = A.minus(common)
                '''
                print("A_minus is ")
                for A_minus_temp in A_minus:
                    A_minus_temp.display()
                    print(f"does A_minus_temp intersect wiht common: {A_minus_temp.intersect(common)}")
                print(f"len(A_minus) is {len(A_minus)}")
                '''
                # put A_minus in lst_A
                lst_A.extend(A_minus)

                B_minus = B.minus(common)
                # put B_minus in lst_B. put it at the front.
                B_minus.extend(lst_B)
                lst_B = B_minus
                #lst_B.extend(B_minus)
                
                #print(f"len(lst_A) is {len(lst_A)} and len(lst_B) is {len(lst_B)}")
                lst_A.remove(A)
                #print(f"len(lst_A) is {len(lst_A)} and len(lst_B) is {len(lst_B)}")
                break

        if not intersected:
            lst_A.append(B)
    
    num_on_cubes = 0
    for A in lst_A:
        num_on_cubes += A.num_of_cubes()

    return num_on_cubes


def preprocess(steps):
    ranges = []
    for s in steps:
        assert(len(s) == 7)
        ranges.append(Range(s[0], Axis(s[1], s[2]), Axis(s[3], s[4]), Axis(s[5], s[6])))
    return ranges



def get_steps(lines):
    steps = [None for _ in range(len(lines))]
    for i in range(len(lines)):
        line = lines[i]
        space = line.split(' ')
        if space[0] == "on":
            on_off = True
        elif space[0] == "off":
            on_off = False
        else:
            raise("unexpected case")

        comma = space[1].split(',')

        x = re.split('\.|=', comma[0])
        x1 = int(x[1])
        x2 = int(x[3])

        y = re.split('\.|=', comma[1])
        y1 = int(y[1])
        y2 = int(y[3])

        z = re.split('\.|=', comma[2])
        z1 = int(z[1])
        z2 = int(z[3])

        steps[i] = (on_off, x1, x2, y1, y2, z1, z2)
    return steps







def get_data(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        return lines




if __name__=="__main__":
    lines = get_data("/home/harsh/now/aoc/aoc_2021/txts/22.txt")
    steps = get_steps(lines)
    ranges = preprocess(steps)
    print(flow(ranges))

