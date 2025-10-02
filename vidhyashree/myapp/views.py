from django.shortcuts import render
def calculateBMI(request):
    bmi=None
    Weight=None
    Height=None
    if request.method == "POST":
        Weight=float(request.POST.get("Weight"))
        Height=float(request.POST.get("Height"))/100
        bmi = Weight/(Height**2)
        bmi =round(bmi,2)
        print(f"1Weight in kg: {Weight} ,Height in m: {Height},bmi: {bmi}")
    return render(request,'myapp/math.html',{'bmi':bmi})
