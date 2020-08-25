# i have created this file
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse("<h1>hello shivam<h1>")
# def about(request):
#     return HttpResponse("about shivam")
def index(request):
    # return HttpResponse("Home")
    # params={'name':'shivam','place':'USA'}
    return render(request,'index2.html')

def analyze(request):
    text1=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    print(removepunc)
    print(text1)
    if removepunc=="on":
    # analyzed=text1
                 punctuations=''')[]{<>" + // ":" + // . "," + //! '''
                 analysed=""
                 for char in text1:
                              if char not in punctuations:
                                         analysed=analysed+char
                 params={'purpose':'Removed punctuations','analysed_text':analysed}
                 return render(request,'analyze.html',params)
    elif fullcaps=="on":
        analysed=""
        for char in text1:
            analysed=analysed+char.upper()
        params={'purpose':'Change to uppercase','analysed_text':analysed}
        return render(request,'analyze.html',params)
    elif newlineremover=="on":
        analysed=""
        for char in text1:
            if char!="\n" and char!="\r":
                analysed=analysed+char
                     
        params={'purpose':'Change to uppercase','analysed_text':analysed}
        return render(request,'analyze.html',params)
    # elif charcount=="on":
    #     count=0
    #     for char in text1:
    #         count=count+1
                     
    #     params={'purpose':'Charactercount','analysed_text':count}
    #     return render(request,'analyze.html',params)
    elif extraspaceremover=="on":
        analysed=""
        for index,char in enumerate(text1):
            if text1[index]==" " and text1[index+1]==" ":
                pass
            else:
                analysed=analysed+char
                     
        params={'purpose':'Change to uppercase','analysed_text':analysed}
        return render(request,'analyze.html',params)

    else:
        return HttpResponse("Error")
def ex1(request):
    s='''<a href="https://www.google.com/">Google</a>'''
    return HttpResponse(s)
    
    # return HttpResponse("remove punc")
    
# def capfirst(request):
#     return HttpResponse("capitalizefirst")
# def newlineremove(request):
#     return HttpResponse("newlineremove")
# def spaceremove(request):
#     return HttpResponse("spaceremove <a href='/'>back</a>")
# def charcount(request):
#     return HttpResponse("charcount")