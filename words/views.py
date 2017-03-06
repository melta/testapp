from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from words.word import Word


def index(request):
    """ Main app view.
    """

    if request.POST.get("clear"):
        return HttpResponseRedirect(reverse("words:index"))

    context = {}
    template = "words/index.html"
    data = request.POST.get("data", None)
    data_file = request.FILES.get("data_file", None)

    if request.method == "POST" and request.POST.get("run"):
        if not data and not data_file:
            return render(request, template,
                          {"error_message": "Please provide some text."})

        context = {"words": []}
        if data_file:
            context["words"] = Word(
                data_file.read().decode("utf-8")).concordance()
        elif data:
            context["words"] = Word(data).concordance()

    return render(request, template, context)
