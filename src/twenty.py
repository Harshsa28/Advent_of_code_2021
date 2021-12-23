import numpy as np
np.set_printoptions(threshold=np.inf)
import pandas as pd


class image:
    def __init__(self, lines):
        self.img = [None for _ in range(len(lines))]
        #self.img = np.array([None for _ in range(len(lines))])
        for i in range(len(lines)):
            self.img[i] = list(lines[i])
        self.img = np.array(self.img)
        self.empty_char = '.'
    
    def get_empty_layers(self):
        empty = 0
        if self.empty_char == '.':
            non_empty_char = '#'
        elif self.empty_char == '#':
            non_empty_char = '.'
        else:
            raise("unexpected case")
        while (non_empty_char not in self.img[empty]) and (non_empty_char not in self.img[len(self.img)-empty-1]) and (non_empty_char not in [x[empty] for x in self.img]) and (non_empty_char not in [x[len(x)-empty-1] for x in self.img]):
            empty += 1
        return empty

    def add_empty_layer(self):
        self.img = np.concatenate([np.full((1, self.img.shape[1]), self.empty_char), self.img], axis=0) # first row
        self.img = np.concatenate([self.img, np.full((1, self.img.shape[1]), self.empty_char)], axis=0) # last row
        self.img = np.concatenate([np.full((self.img.shape[0], 1), self.empty_char), self.img], axis=1) # first col
        self.img = np.concatenate([self.img, np.full((self.img.shape[0], 1), self.empty_char)], axis=1) # last col
    
    def remove_empty_layer(self):
        self.img = np.delete(self.img, (0), axis=0) # first row
        self.img = np.delete(self.img, (-1), axis=0) # last row
        self.img = np.delete(self.img, (0), axis=1) # first col
        self.img = np.delete(self.img, (-1), axis=1) # last col
        
    def make_2_empty_layers(self):
        num_empty = self.get_empty_layers()
        while num_empty < 2:
            self.add_empty_layer()
            num_empty = self.get_empty_layers()
        #while num_empty > 2:
        #    self.remove_empty_layer()
        #    num_empty = self.get_empty_layers()
        #assert(self.get_empty_layers() == 2)
    
    def get_bin(self, x, y):
        bin_str = ""
        central = self.img[x][y]
        for i in range(3):
            for j in range(3):
                if x-1+i >= 0 and x-1+i < self.img.shape[0] and y-1+j >= 0 and y-1+j < self.img.shape[1]:
                    bin_str += self.img[x-1+i][y-1+j]
                else:
                    bin_str += central
        bin_str = bin_str.replace('#', '1').replace('.', '0')
        return int(bin_str, 2)

    def update_empty_char(self, alg):
        self.empty_char = alg[int((self.empty_char*9).replace('#', '1').replace('.', '0'), 2)]

    def update(self, alg):
        self.make_2_empty_layers()
        #assert(self.get_empty_layers() == 2)
        op = np.full(self.img.shape, '.')
        assert(self.img.shape == op.shape)
        
        # we only calc from first inner layer (i.e. we ignore last layer)
        for i in range(0, self.img.shape[0]):
            for j in range(0, self.img.shape[1]):
                op[i][j] = alg[self.get_bin(i, j)]
        self.img = op
        self.update_empty_char(alg)
        self.make_2_empty_layers()
 
    def count_lit(self):
        return (self.img == '#').sum()






def get_data(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        alg = list(lines[0])
        img = image(lines[2:])
        print(f"alg is \n{alg} and img is \n{img}")
        return alg, img







if __name__=="__main__":
    alg, img = get_data("/home/harsh/now/aoc/aoc_2021/txts/twenty.txt")
    #while img.get_empty_layers() < 100:
    #    img.add_empty_layer()
    for i in range(50):
        img.update(alg)
    print(img.count_lit())

