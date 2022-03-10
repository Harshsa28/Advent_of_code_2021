




class ALU:
    # w=0, x=0, y=0, z=0
    vars = [0,0,0,0] # w, x, y, z



    def execute_op(op, arg1, arg2):




    def eval (lines, nums):
        assert(len(nums) == 14)
        num_i = 0
        for line in lines:
            words = line.split(' ')
            assert(len(words) == 2 or len(words) == 3)
            op = words[0]
            if op == "inp":
                w = nums[num_i]
                num_i += 1
            elif op == "add":
                arg1 = words[1]
                arg2 = words[2]
                if (arg1 == 'w'):













