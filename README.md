# Ex.05 Design a Website for Server Side Processing
## Date:03/10/2025

## AIM:
 To design a website to calculate the Body Mass Index (BMI) in the server side. 


## FORMULA:
BMI=W/H<sup>2</sup>
<br> BMI --> Body Mass Index
<br> W --> Weight
<br> H --> Height

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<html>
<title>Body mass index</title>
<style>
body
{
background-color: blue;
}
.edge {
width: 1550px;
margin-left: auto;
margin-right: auto;
padding-top: 345px;
padding-left: 300px;
}
.box {
display:block;
border: solid 6px purple;
width: 600px;
min-height: 300px;
font-size: 30px;
background-color: yellow;
}
.formelt{
color: orange;
text-align: center;
margin-top: 6px;
margin-bottom: 6px;
}
h1
{
color:rgb(0, 255, 179);
text-align: center;
padding-top: 30px;
} 
</style>
</head>
<body>
<div class= "edge">
<div class= "box">
<h1>Body mass index</h1>
<h2>Vidhya shree.k(25008027)</h2>
<form method="POST">
{% csrf_token %}
<div class= "formelt">
    Weight: <input type= "text" name="Weight" value="{{Weight}}"></input>(in kg)<br/>
</div>
<div class= "formelt">
    Height: <input type= "text" name="Height" value="{{Height}}"></input>(in m)<br/>
</div>
<div class= "formelt">
<input type="submit" value="Calculate"><br/>
</div>
<div class="formelt">
    bmi: <input type="text" name="bmi" value="{{bmi}}" align:"center"></input>kg/m<sup>2</sup><br/>
</div> 
</form> 
</div>
</div> 
</body>
</html>
views.py
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
urls.py
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns=[
	path('admin/', admin.site.urls),
    path('',views.calculateBMI,name="home"),
    path('bmi/', views.calculateBMI,name='bmi')
]


```


## SERVER SIDE PROCESSING:
![alt text](<vidhyashree/myapp/templates/myapp/Screenshot 2025-10-03 050218.png>)

## HOMEPAGE:
![alt text](<vidhyashree/myapp/templates/myapp/Screenshot 2025-10-03 050153.png>)

## RESULT:
The program for performing server side processing is completed successfully.
