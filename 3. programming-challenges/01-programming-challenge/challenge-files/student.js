// Write your code here

// My first fction
function myFirstFunction(bike) {
    forward(bike);
}

// Twice forward 
function twiceForward(bike) {
    forward(bike);
    forward(bike);
}

// Thrice forward 
function thriceForward(bike) {
    forward(bike);
    forward(bike);
    forward(bike);
}

// Forward 4
function forward4(bike) {
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
}

// Forward 5
function forward5(bike) {
    let i = 5;

    while (i > 0) {
        forward(bike);
        i = i - 1;
    }
}

// Forward 10
function forward10(bike) {
    let i = 10;

    while (i > 0) {
        forward(bike);
        i = i - 1;
    }
}

// Right
function right(bike) {
    turnRight(bike);
    forward(bike);
}

// Ell shape
function ellShape(bike) {
    forward5(bike);
    turnRight(bike);
    forward4(bike);
}

// U turn
function uTurn(bike) {
    thriceForward(bike);
    turnRight(bike);
    forward10(bike);
    turnRight(bike);
    twiceForward(bike);
}

// Crooked U turn
function forwardN(bike, steps) {
    let i = steps;

    while (i > 0) {
        forward(bike);
        i = i - 1;
    }
}

function crookedUTurn(bike) {
    forwardN(bike, 7);
    turnRight(bike);
    forwardN(bike, 9);
    turnRight(bike);
    forwardN(bike, 3);
}

// Forward until wall
function forwardUntilWall(bike) {
    while (!sensor(bike)) {
        forward(bike);
    }
}

// Smart ell shape
function smartEllShape(bike) {
    forwardUntilWall(bike);
    turnRight(bike);
    forwardUntilWall(bike);
}

// Spiral
function spiral(car) {
    let i = 18;
    while (i > 0) {
        forwardUntilWall(car);
        while (sensor(car)) {
            turnRight(car);
        }
        i = i - 1
    }
}

// Left
function turnLeft(car) {
    turnRight (car);
    turnRight (car);
    turnRight (car);
}

function left(car) {
    turnLeft(car);
    forward(car);
}

// Slalom
function slalom(car) {
    forwardUntilWall(car);
    turnLeft(car);
    forwardUntilWall(car);
    turnRight(car);
    forwardUntilWall(car);
    turnRight(car);
    forwardUntilWall(car);
    turnLeft(car);
    forwardUntilWall(car);
    turnLeft(car);
    forwardUntilWall(car);
    turnRight(car);
    forwardUntilWall(car);
    turnRight(car);
    forwardUntilWall(car);
}

// Left or Right
function leftOrRight(car) {
    turnLeft(car);
    forwardUntilWall(car);
    turnRight(car);
    forwardUntilWall(car);
    turnRight(car);
    forwardUntilWall(car);
    turnLeft(car);
    forwardUntilWall(car);
}

// Incomplete U
function incompleteU(car) {
    forwardUntilWall(car);
    turnRight(car);
    forwardUntilWall(car);
    turnRight(car);
    forwardUntilWall(car);
}

// Which direction
function whichDirection(car) {
    while (sensor(car)) {
        turnRight(car);
    }
    forwardUntilWall(car);
}

// First right
function sensorRight(car) {
    turnRight(car);
    let result = sensor(car);
    turnLeft(car);

    return result
}

function firstRight(car) {
    while (sensorRight(car)) {
        forward(car);
    }
    turnRight(car);
    forwardUntilWall(car);
}

// First left
function sensorLeft(car) {
    turnLeft(car);
    let result = sensor(car);
    turnRight(car);

    return result
}

function firstLeft(car) {
    while (sensorLeft(car)) {
        forward(car);
    }
    turnLeft(car);
    forwardUntilWall(car);
}

// ZigZag
function zigZag(car) {
    firstRight(car);
    turnLeft(car);
    forward(car);
    firstLeft(car);    
}

// Second right
function forwardUntilFreeRight(car) {
    while (sensorRight(car)) {
        forward(car)
    }
}

function secondRight(car) {
    forwardUntilFreeRight(car);
    forward(car);
    forwardUntilFreeRight(car);
    turnRight(car);
    forwardUntilWall(car);
}

// Third right
function thirdRight(car) {
    forwardUntilFreeRight(car);
    forward(car);
    forwardUntilFreeRight(car);
    forward(car);
    forwardUntilFreeRight(car);
    turnRight(car);
    forwardUntilWall(car);
}

// Forth right
function forwardUntilNthRight(car, nrights) {
    let i = nrights;

    while (i > 0) {
        forward(car);

        if (!sensorRight(car)) {
            i = i - 1;
        }
    }
}

function fourthRight(car) {
    forwardUntilNthRight(car, 4);
    turnRight(car);
    forwardUntilWall(car);
}

// Fifth Left
function forwardUntilNthLeft(car, nlefts) {
    let i = nlefts;

    while (i > 0) {
        forward(car);

        if (!sensorLeft(car)) {
            i = i - 1;
        }
    }
}

function fifthLeft(car) {
    forwardUntilNthLeft(car, 5);
    turnLeft(car);
    forwardUntilWall(car);
}

// Maze
function maze(car) {
    function L(n) {
        forwardUntilNthLeft(car, n);
        turnLeft(car);
    }

    function R(n) {
        forwardUntilNthRight(car, n);
        turnRight(car);
    }
        
    R(2);
    L(1);
    L(2);
    L(2);
    R(4);
    R(1);
    L(3);
    forwardUntilWall(car);
}

// Find dead end
function turnAround(car){
    turnRight(car);
    turnRight(car);
}

function backward(car) {
    turnAround(car);
    forward(car);
    turnAround(car);
}

function isDeadEnd(car) {
    if (!sensor(car)) {
        return false;
    }

    if (!sensorRight(car)) {
        return false;
    }

    if (!sensorLeft(car)) {
        return false
    }

    return true;
}

function findDeadEnd(car) {
    while(true) {
        forward(car);

        if (isDeadEnd(car)) {
            return;
        }

        backward(car);
        turnRight(car);
    }
}

// Follow
function follow(car) {
    
}

// Right hand

// Forward until destination

// Roomba

// Satnav
