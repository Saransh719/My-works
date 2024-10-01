// the variables we usually use are automatic
//if a variable is declared in another c file and used in this one, it is extern
//global variables are also external
//static variables are variables which do not get destroyed when a function ends if we write "static int a=5; a++;", the next time a function is called, the value of a will be 6 only and the first line will be ignored
//register variables are stored in cpu register instead of ram for faster access, the compiler may not assign register if cpu register is not free. In that case, auto is assigned

