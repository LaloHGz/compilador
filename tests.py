# Test cases
tests = [
#test 0
'''
program abc; 
var mariana, lalo,idss : int; 
    alberto, andres, max : float; 

void nuevo(edad:int,altura:float)[
    var comida,restaurante: int; mesa: int; {
        restaurante = 10; 
        print("hola"); 
    }
]; 

main {
    do{
        print("hello mariana");
    }
    while(idss > max);
} 

end''', 

#test 1

'''
program abc; 
var x : int;
main {
    x = 5;
    if (x > 0) {
        print("Positive");
    } else {
        print("Negative");
    };
    print("holaaa");
}
end
''',

#test 2
'''
program abc; 
var PI, radius : float;

main {
    PI = 3.14159;
    radius = 5.0;
    print(PI * radius * radius);
}
end
''',

# test 3
'''
program test5; 
var x, fibonacci: int; 
    y : float; 

void fibo(n:int)[
    {
        if (n < 1) {
            x = n;
        } else {
            fibonacci(n - 1);
            fibonacci(n - 2);
        };   
    }
]; 


void futbol(partidos:int, goles:int, p_victoria:float)[
    {
        partidos = 10;
        goles = 30;
        p_victoria = partidos * goles * 0.10;
        
        do{
          p_victoria = partidos * p_victoria;
          partidos = partidos - 1;
        }
        while(partidos > 5);
         
    }
]; 

void atp(n_player:int, ace: int, wins: int, ranking: int)[
    {
        if (wins > 100) {
            ranking = ranking - 10;
        } else {
            ranking = ranking + 1;
        };   
    }
]; 

main {
    x = 6;
    y = 7 / 25.3;
    print("fibonacci", fibonacci);
    print(x * x / x + x);
    futbol(3527,123,54,120.2);
    atp(3527,123,54,120);
} 

end
''',

# Test case 4 Fibonacci using do while
'''
program fibonacci;
var n, a, b, temp, i : int;

main {
    n = 10;  
    a = 0;  
    b = 1; 
    i = 1;

    print("Fibonacci Series:");

    do {
        print(a);
        temp = a + b;
        a = b;
        b = temp;
        i = i + 1;
    }
    while (i < n);
} 

end''',


# Test Case 5 - Factorial
'''
program test;

    var factorial, i, n : int;

    main {
        factorial = 1;
        i = 1;
        n = 5;
        do {
            factorial = factorial * i;
            i = i + 1;
        } while (i < (n+1));
        
        print("El factorial es", factorial);
    }

    end
''',

# Test case 6 - Simple Arithmetic Operations
'''
program arithmetic;
var a, b, c : int;
    x, y, z : float;

main {
    a = 10;
    b = 20;
    c = a + b * (a - b);
    print("Result of c:", c);

    x = 2.5;
    y = 4.5;
    z = x / y + x * y;
    print("Result of z:", z);
}
end
''',

# Test case 7 - Nested Loops
'''
program nestedLoops;
var i, j : int;

main {
    i = 0;
    do {
        j = 0;
        do {
            print("i:", i, "j:", j);
            j = j + 1;
        }
        while (j < 3);
        i = i + 1;
    }
    while (i < 2);
}
end
''',

# Test case 8 - Logical Operations
'''
program logicalOps;
var a, b : int;

main {
    a = 10;
    b = 5;
    print("Result of (a > b) and (b < a):", (a > b));

    print("Result of (a == b) or (b <= a):", (a > b));

    print("Result of not (a < b):",(b < a));
}
end
''',

# Test case 9 - Complex Conditionals
'''
program complexConditionals;
var a, b, c : int;
    x : float;

main {
    a = 5;
    b = 10;
    c = 15;
    x = 2.5;

    if (x > 1.0) {
        print("Condition is true");
    } else {
        print("Condition is false");
    };

    if (a + b > c) {
        print("a + b is greater than c");
    } else {
        print("a + b is not greater than c");
    };
}
end
''',

# Test case 10 - Simple Loop
'''
program simpleLoop;
var i, sum : int;

main {
    i = 0;
    sum = 0;
    do {
        sum = sum + i;
        print("Current sum:", sum);
        i = i + 1;
    }
    while (i < 5);
}
end
''',

# Test case 11 - Arithmetic and Assignment
'''
program arithmeticAssignment;
var a, b, c : int;

main {
    a = 1;
    b = 2;
    c = a + b;
    print("Initial c:", c);
    
    c = c * 2;
    print("c after multiplication:", c);
    
    c = c - b;
    print("c after subtraction:", c);
}
end
''',

# Test case 12 - Nested If-Else
'''
program nestedIfElse;
var a : int;

main {
    a = 10;
    if (a > 0) {
        print("a is positive");
        if (a > 5) {
            print("a is greater than 5");
        } else {
            print("a is less than or equal to 5");
        };
    } else {
        print("a is non-positive");
    };
}
end
''',

# Test case 13 - Basic Arithmetic with Floats
'''
program floatArithmetic;
var x, y, z : float;

main {
    x = 1.5;
    y = 2.5;
    z = x + y;
    print("Sum of x and y:", z);

    z = x * y;
    print("Product of x and y:", z);

    z = y - x;
    print("Difference of y and x:", z);

    z = y / x;
    print("Quotient of y and x:", z);
}
end
''',

# Test case 14 - Variable Reassignment
'''
program variableReassignment;
var a, b : int;

main {
    a = 5;
    print("Initial a:", a);
    
    a = 10;
    print("Reassigned a:", a);
    
    b = a;
    print("Assigned b to a:", b);
    
    b = b + 5;
    print("Incremented b:", b);
}
end
''',

# Test case 15 - Simple Comparison
'''
program simpleComparison;
var x, y : int;

main {
    x = 7;
    y = 10;
    
    if (x < y) {
        print("x is less than y");
    } else {
        print("x is not less than y");
    };

    if (y > x) {
        print("y is greater than x");
    } else {
        print("y is not greater than x");
    };
    
    if (x != 7) {
        print("x is not 7");
    } else {
        print("x is 7");
    };
}
end
''',

# Test case 16 - Multiple Assignments and Calculations
'''
program multipleAssignments;
var a, b, c, d : int;

main {
    a = 2;
    b = 3;
    c = 4;
    
    d = a + b * c;
    print("Result of a + b * c:", d);
    
    d = (a + b) * c;
    print("Result of (a + b) * c:", d);
    
    d = a * b + c;
    print("Result of a * b + c:", d);
    
    d = a * (b + c);
    print("Result of a * (b + c):", d);
}
end
''',

# Test case 17 - Simple For Loop Equivalent using Do-While
'''
program forLoopEquivalent;
var i : int;

main {
    i = 0;
    do {
        print("Current i:", i);
        i = i + 1;
    }
    while (i < 5);
}
end
''',

# Test case 18 - Comparison and Arithmetic
'''
program comparisonArithmetic;
var a, b, result : int;

main {
    a = 8;
    b = 4;
    
    if (a > b) {
        result = a - b;
        print("a is greater than b, result of a - b:", result);
    } else {
        result = b - a;
        print("a is not greater than b, result of b - a:", result);
    };
}
end
''',


# Test case 19 - Variable Initialization and Print
'''
program varInitPrint;
var x : int;
    y : float;

main {
    x = 10;
    y = 20.5;

    print("Value of x:", x);
    print("Value of y:", y);
}
end
''',


# Test case 20 - Nested If-Else with Do-While Loop
'''
program nestedIfElseWithLoop;
var a, b, c : int;

main {
    a = 5;
    b = 10;
    c = 15;

    do {
        if (a > b) {
            if (b != c) {
                print("a is greater than b and b is not equal to c");
            } else {
                print("a is greater than b and b is equal to c");
            };
        } else {
            if (a < c) {
                print("a is not greater than b and a is less than c");
            } else {
                print("a is not greater than b and a is not less than c");
            };
        };
        a = a + 1;
    }
    while (a < 7);
}
end
''',

# Test case 21 - Nested Loops with If-Else
'''
program nestedLoopsIfElse;
var i, j : int;

main {
    i = 0;

    do {
        j = 0;
        do {
            if (i != j) {
                print("i is not equal to j:", i, j);
            } else {
                print("i is equal to j:", i, j);
            };
            j = j + 1;
        }
        while (j < 3);
        i = i + 1;
    }
    while (i < 3);
}
end
''',

# Test case 22 - Complex Arithmetic in Do-While Loop
'''
program complexArithmeticLoop;
var a, b, c : int;

main {
    a = 1;
    b = 2;
    c = 3;

    do {
        if (a + b > c) {
            c = a * b;
            print("New value of c:", c);
        } else {
            b = b + 1;
            print("Incremented value of b:", b);
        };
        a = a + 1;
    }
    while (a < 5);
}
end
''',


# Test case 23 - Nested If-Else with Multiple Conditions in Loop
'''
program multipleConditionsLoop;
var x, y : int;

main {
    x = 0;
    y = 5;

    do {
        if (x < 3) {
            if (y > 3) {
                print("x is less than 3 and y is greater than 3");
            } else {
                print("x is less than 3 and y is not greater than 3");
            };
        } else {
            if (y != 5) {
                print("x is not less than 3 and y is not 5");
            } else {
                print("x is not less than 3 and y is 5");
            };
            y = y - 1;
        };
        x = x + 1;
    }
    while (x < 5);
}
end
''',

]