# Test cases
tests = [
    #test 0
    '''
program abc; 
var mariana, lalo : int; 
    alberto, andres : float; 

void nuevo(edad:int,altura:float)[
    var comida,restaurante: int; mesa: int; {
        restaurante = 10; print("hola"); 
    }
]; 

main {
    do{
        print("hello mariana");
    }
    while(idss);
} 

end''', 

#test 1
'''
program prueba;

main{ 

} 

end''',

#test 2
'''
program prueba;

main{ 

if ((a*7 / b) > (5*5*5)){
    print("comida corrida");
};

} 

end''',

#test 3
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
}
end
''',

#test 4
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

# test 5
'''
program test5; 
var x: int; 
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
          goles = partidos * p_victoria;
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
    partidos = 10;
    goles = 10;
    p_victoria = 0.53;
    print("fibonacci");
    futbol(partidos,goles,p_victoria);
    atp(3527,123,54,120);
} 

end
''',

#test 6 - tiene que dar error
'''
program prueba;

main{  

end'''

]