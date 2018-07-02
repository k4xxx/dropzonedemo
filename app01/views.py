from django.shortcuts import render

def dropzoneTest(request):
    if request.is_ajax():
        file = request.FILES.get('file')
        with open('file.jpg','wb') as f:
            for line in file:
                f.write(line)
    return render(request,'dropzoneTest.html')