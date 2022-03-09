#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;



enum OP_TYPES {INP, ADD, MUL, DIV, MOD, EQL, INT};

class AST {
    int val; // only for leaves with ints
    // char var; // only for leaves with w's
    int index; // for w0 to w13
    OP_TYPES op_type;
    AST * left, * right; // for tree structure of AST

    public:
    // AST() {}
    // AST(OP_TYPES op_type): op_type(op_type) {}
    // AST(OP_TYPES op_type, AST * left, AST * right): op_type(op_type), left(left), right(right) {}
    // AST(OP_TYPES op_type, int val): op_type(op_type), val(val) {}
    // AST(OP_TYPES op_type, char var): op_type(op_type), var(var) {}

    void set_val(int val) { assert(op_type == INT); AST::val = val; }
    int get_val() { assert(op_type == INT); return val; }
    // void set_var(char ch) { AST::var = var; }
    // char get_var() { return var; }
    void set_index (int index) { assert(op_type == INP); AST::index = index; }
    int get_index () { assert(op_type == INP); return AST::index; }
    void set_left(AST * left) { assert(op_type != INT && op_type != INP); AST::left = left; }
    AST * get_left() { assert(op_type != INT && op_type != INP); return left; }
    void set_right(AST * right) { assert(op_type != INT && op_type != INP); AST::right = right; }
    AST * get_right() { assert(op_type != INT && op_type != INP); return right; }
    void set_op_type(OP_TYPES op_type) { AST::op_type = op_type; }
    void set_op_type (string op_str) {
        if (op_str == "inp") { AST::op_type = INP; }
        else if (op_str == "add") { AST::op_type = ADD; }
        else if (op_str == "mul") { AST::op_type = MUL; }
        else if (op_str == "div") { AST::op_type = DIV; }
        else if (op_str == "mod") { AST::op_type = MOD; }
        else if (op_str == "eql") { AST::op_type = EQL; }
        else { cerr << "unexpected case in set_op : " << op_str << endl; exit(1); }
    }
    OP_TYPES get_op_type() { return op_type; }
    

    void print() {
        if (op_type == INP) cout << "INP";
        else if (op_type == ADD) cout << "ADD";
        else if (op_type == MUL) cout << "MUL";
        else if (op_type == DIV) cout << "DIV";
        else if (op_type == MOD) cout << "MOD";
        else if (op_type == EQL) cout << "EQL";
        else if (op_type == INT) cout << "INT";
        else { cerr << "unexpected case in print()" << endl; exit(1); }
        cout << "(";
        if (op_type == INP) {
            cout << index << ")";
        }
        else if (op_type == INT) {
            cout << val << ")";
        }
        else {
            left->print();
            cout << ",";
            right->print();
            cout << ")";
        }
    }
};







class ALU {
    AST * w, * x, * y, * z;
    int index; // for counting w0 to w13 for INPs

    public:

    ALU(): index(0) {
        AST * w_temp = new AST();
        w_temp->set_op_type(INT);
        w_temp->set_val(0);
        w = w_temp;

        AST * x_temp = new AST();
        x_temp->set_op_type(INT);
        x_temp->set_val(0);
        x = x_temp;

        AST * y_temp = new AST();
        y_temp->set_op_type(INT);
        y_temp->set_val(0);
        y = y_temp;

        AST * z_temp = new AST();
        z_temp->set_op_type(INT);
        z_temp->set_val(0);
        z = z_temp;
    }

    AST * get_ast_from_char (char ch) {
        if (ch == 'w') { return w; }
        else if (ch == 'x') { return x; }
        else if (ch == 'y') { return y; }
        else if (ch == 'z') { return z; }
        else  { cerr << "unexpected case in get_ast_from_char" << endl; exit(1); }
    }

    void set_ast_to_char (char ch, AST * ast) {
        if (ch == 'w') { w = ast; }
        else if (ch == 'x') { x = ast; }
        else if (ch == 'y') { y = ast; }
        else if (ch == 'z') { z = ast; }
        else { cerr << "unexpected case in set_ast_to_char" << endl; exit(1); }
    }

    void read_file (string filename) {
        ifstream f(filename);
        string line;

        while (getline (f, line)) {
            // cout << "line is " << line << endl;
            if (line != "") {
                AST * ast = new AST();
                ast->set_op_type(line);

                getline(f, line);
                assert(line.length() == 1);
                char arg1_ch = line.at(0);
                AST * arg1 = get_ast_from_char(arg1_ch);

                getline(f, line);
                if (line == "") { // inp
                    ast->set_index(index);
                    index += 1;
                }
                else {
                    AST * arg2;
                    if (isdigit(line.at(0)) || (line.at(0) == '-')) { // int
                        int var = stoi(line);
                        arg2 = new AST();
                        arg2->set_op_type(INT);
                        arg2->set_val(var);
                    }
                    else { // var
                        char arg2_ch = line.at(0);
                        arg2 = get_ast_from_char(arg2_ch);
                    }

                    ast->set_left(arg1);
                    ast->set_right(arg2);

                }

                // ast = optimize(ast);

                set_ast_to_char(arg1_ch, ast);
                
                // cout << arg1_ch << " : ";
                // AST * arg1_temp = get_ast_from_char(arg1_ch);
                // // cout << arg1_temp->get_op_type() << endl;
                // arg1_temp->print();
                // cout << endl << endl;
            }
        }

        // cout << "done with reading" << endl;
    }


    AST * optimize (AST * ast) {
        OP_TYPES op_type = ast->get_op_type();
        
        if (op_type == MUL) {
            AST * left = ast->get_left();
            AST * right = ast->get_right();
            // mul by 0 is 0
            if (right->get_op_type() == INT && right->get_val() == 0) {
                // cout << "used mul by 0" << endl;
                AST * updated_ast = new AST();
                updated_ast->set_op_type(INT);
                updated_ast->set_val(0);
                delete ast;
                return updated_ast;
            }
            // mul by 1 is left
            else if (right->get_op_type() == INT && right->get_val() == 1) {
                // cout << "used mul by 1" << endl;
                delete ast;
                return left;
            }
            // mul of 2 ints is int
            else if (right->get_op_type() == INT && left->get_op_type() == INT) {
                // cout << "used mul by 2 ints" << endl;
                // delete ast;
                AST * updated_ast = new AST();
                updated_ast->set_op_type(INT);
                updated_ast->set_val(left->get_val() * right->get_val());
                delete ast;
                return updated_ast;
            }
        }
        else if (op_type == DIV) {
            AST * left = ast->get_left();
            AST * right = ast->get_right();
            // div by 0 is undefined
            if (right->get_op_type() == INT && right->get_val() == 0) {
                cerr << "div by 0 is undefined" << endl;
                exit(1);
            }
            // div by 1 is left
            else if (right->get_op_type() == INT && right->get_val() == 1) {
                delete ast;
                return left;
            }
            // div of 2 ints is int
            else if (right->get_op_type() == INT && left->get_op_type() == INT) {
                AST * updated_ast = new AST();
                // updated_ast->set
            }
        }
        return ast;
    }



    void print() {
        cout << "in alu print" << endl;

        cout << "w : ";
        w->print();
        cout << endl;

        cout << "x : ";
        x->print();
        cout << endl;

        cout << "y : ";
        y->print();
        cout << endl;

        cout << "z : ";
        z->print();
        cout << endl;
    }
    

    // ALU (): w(0), x(0), y(0), z(0) {}
    // ALU() {}
    // int get_var (char var) {
    //     if (var == 'w') { return w; }
    //     else if (var == 'x') { return x; }
    //     else if (var == 'y') { return y; }
    //     else if (var == 'z') { return z; }
    //     else { cerr << "unexpected case in get_var : " << var << endl; exit(1); }
    // }
    // void set_var (char var, int val) {
    //     if (var == 'w') { w = val; }
    //     else if (var == 'x') { x = val; }
    //     else if (var == 'y') { y = val; }
    //     else if (var == 'z') { z = val; }
    //     else { cerr << "unexpected case in set_var : " << var << endl; exit(1); }
    // }

};







// class MONAD {
//     vector<Op> ops;

//     public:
//     MONAD(vector<Op> ops): ops(ops) {}

//     void optimize() {
//         bool optimized = false;

//         do {
//             optimized = false;

//             for (int i = 0; i < ops.size(); ++i) {
//                 Op op = ops[i];


//                 // mul with 0 is 0
//                 if (op.get_op() == MUL && op.get_arg2().get_arg_type() == INT && op.get_arg2().get_val() == 0) {
//                     Op updated_op;
//                     updated_op.set_op()
//                 }
                
//             }

//         } while (optimized);
//     }
// };

// vector<Op> read_ops (string filename) {
//     ifstream f(filename);
//     string line;
//     vector<Op> ops;

//     while (getline(f, line)) {
//         // cout << "line is " << line << endl;
//         Op op;
//         if (line != "") {
//             Arg arg1, arg2;
            
//             op.set_op(line);
            
//             getline(f, line);
//             assert(line.length() == 1);
//             arg1.set_char(line.at(0));

//             getline(f, line);
//             if (line == "") {
//                 arg2.set_none();
//             }
//             else if (isdigit(line.at(0)) || (line.at(0) == '-')) {
//                 int var = stoi(line);
//                 arg2.set_int(var);
//             }
//             else {
//                 // cout << "line is " << line << endl;
//                 assert(line.length() == 1);
//                 assert(isalpha(line.at(0)));
//                 arg2.set_char(line.at(0));
//             }

//             op.set_args(arg1, arg2);
//             ops.push_back(op);
//         }
//     }
//     // cout << "ops size is " << ops.size() << endl;
//     assert(ops.size() == 252); // num ops in 24.txt
//     return ops;
// }











int main() {
    cout << unitbuf;
    cout << flush;
    // vector<Op> ops = read_ops("/Users/h2agrawa/now/Advent_of_code_2021/txts/24_copy.txt");
    // for (int i = 0; i < ops.size(); ++i) {
    //     ops[i].print();
    // }

    ALU alu;
    alu.read_file("/Users/h2agrawa/now/Advent_of_code_2021/txts/24_copy.txt");

    cout << "calling alu print" << endl;
    // alu.print();


}