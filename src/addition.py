
# This is a test commit
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    
def sub(a, b):
    return a - b

def test_sub():
    assert sub(1, 2) == -1
    assert sub(1, -1) == 2
    
def mult(a, b):
    return a * b

def test_mult():
    assert mult(1, 2) == 2
    assert mult(1, -1) == -1
    
def div(a, b):
    return a / b

def test_div():
    assert div(1, 2) == 0.5
    assert div(1, -1) == -1

def mod(a, b):
    return a % b

def test_div():
    assert mod(1, 2) == 1
    assert mod(1, -1) == 1

