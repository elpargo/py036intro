from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, world.")

def hello_name(request, question_id):
    return HttpResponse("Hello, {}".format(question_id))

def environ(request):
	output = []
	for k,v in request.environ.items():
		output.append("<h2>")
		output.append(unicode(k))
		output.append("</h2>")
		output.append("<p>")
		output.append(unicode(v))
		output.append("</p>")
	return HttpResponse("".join(output))

from django.shortcuts import render

def environ_with_template(request):
	context = {'environ': request.environ}
	return render(request, 'environ.html', context)