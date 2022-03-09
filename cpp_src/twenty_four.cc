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
    int set_var (char var, int val) {
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
};










vector<Op> read_ops (string filename) {
    ifstream f(filename);
    string line;

}





int main() {

}