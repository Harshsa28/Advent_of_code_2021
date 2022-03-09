#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;


enum OP_TYPES {INP, ADD, MUL, DIV, MOD, EQL};

enum ARG_TYPES {CHAR, INT, NONE};


class Arg {
    ARG_TYPES arg_type;
    char ch;
    int val;

    public:
    void set_char (char ch) { arg_type = CHAR; Arg::ch = ch; }
    void set_int (int val) { arg_type = INT; Arg::val = val; }
    void set_none () { arg_type = NONE; }
    void print() {
        if (arg_type == CHAR) cout << ch;
        else if (arg_type == INT) cout << val;
    }

    ARG_TYPES get_arg_type () { return arg_type; }
    char get_char() { return ch; }
    int get_val () { return val; }
};

class Op {
    OP_TYPES op;
    Arg arg1, arg2;

    public:
    void set_op (string op_str) {
        if (op_str == "inp") { op = INP; }
        else if (op_str == "add") { op = ADD; }
        else if (op_str == "mul") { op = MUL; }
        else if (op_str == "div") { op = DIV; }
        else if (op_str == "mod") { op = MOD; }
        else if (op_str == "eql") { op = EQL; }
        else { cerr << "unexpected case in set_op : " << op_str << endl; exit(1); }
    }
    void set_args (Arg arg1, Arg arg2) {
        Op::arg1 = arg1;
        Op::arg2 = arg2;
    }

    void print () {
        cout << op << " ";
        arg1.print();
        cout << " ";
        arg2.print();
        cout << endl;
    }

    OP_TYPES get_op () { return op; }
    Arg get_arg1 () { return arg1; }
    Arg get_arg2 () { return arg2; }

};

class ALU {
    int w, x, y, z;

    public:
    ALU (): w(0), x(0), y(0), z(0) {}
    int get_var (char var) {
        if (var == 'w') { return w; }
        else if (var == 'x') { return x; }
        else if (var == 'y') { return y; }
        else if (var == 'z') { return z; }
        else { cerr << "unexpected case in get_var : " << var << endl; exit(1); }
    }
    void set_var (char var, int val) {
        if (var == 'w') { w = val; }
        else if (var == 'x') { x = val; }
        else if (var == 'y') { y = val; }
        else if (var == 'z') { z = val; }
        else { cerr << "unexpected case in set_var : " << var << endl; exit(1); }
    }

};


class MONAD {
    vector<Op> ops;

    public:
    MONAD(vector<Op> ops): ops(ops) {}

    void optimize() {
        bool optimized = false;

        do {
            optimized = false;

            for (int i = 0; i < ops.size(); ++i) {
                Op op = ops[i];


                // mul with 0 is 0
                if (op.get_op() == MUL && op.get_arg2().get_arg_type() == INT && op.get_arg2().get_val() == 0) {
                    Op updated_op;
                    // op.set_op()
                }
                
            }

        } while (optimized);
    }
};

vector<Op> read_ops (string filename) {
    ifstream f(filename);
    string line;
    vector<Op> ops;

    while (getline(f, line)) {
        // cout << "line is " << line << endl;
        Op op;
        if (line != "") {
            Arg arg1, arg2;
            
            op.set_op(line);
            
            getline(f, line);
            assert(line.length() == 1);
            arg1.set_char(line.at(0));

            getline(f, line);
            if (line == "") {
                arg2.set_none();
            }
            else if (isdigit(line.at(0)) || (line.at(0) == '-')) {
                int var = stoi(line);
                arg2.set_int(var);
            }
            else {
                // cout << "line is " << line << endl;
                assert(line.length() == 1);
                assert(isalpha(line.at(0)));
                arg2.set_char(line.at(0));
            }

            op.set_args(arg1, arg2);
            ops.push_back(op);
        }
    }
    // cout << "ops size is " << ops.size() << endl;
    assert(ops.size() == 252); // num ops in 24.txt
    return ops;
}





int main() {
    vector<Op> ops = read_ops("/Users/h2agrawa/now/Advent_of_code_2021/txts/24_copy.txt");
    // for (int i = 0; i < ops.size(); ++i) {
    //     ops[i].print();
    // }


}