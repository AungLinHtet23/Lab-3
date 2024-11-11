import Lab2.bmi as bmi

print("Test BMI")

def test_Under_weight_bmi():
    result=-1
    input_weight=65
    input_height=1.90
    test_bmi=0
    result=bmi.calculate_bmi(input_height,input_weight)
    assert (result==test_bmi)

def test_Normal_weight_bmi():
    result=0
    input_weight=80
    input_height=1.80
    test_bmi=0
    result=bmi.calculate_bmi(input_height,input_weight)
    assert (result==test_bmi)

def test_Over_weight_bmi():
    result=1
    input_weight=90
    input_height=1.90
    test_bmi=0
    result=bmi.calculate_bmi(input_height,input_weight)
    assert (result==test_bmi)    
