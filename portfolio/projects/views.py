from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, "main.html")

def project_one(request):
    return render(request, "project_one.html")

def email_agent(request):
    return render(request, "email_agent.html")

def sql_certification(request):
    return render(request, "sql_certification.html")