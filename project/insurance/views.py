from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from .models import ClientFamily, Client
from .forms import ClientFamilyForm, ClientForm


class ClientCreateView(CreateView):
    model = Client
    template_name = "insurance/create_bimename.html"
    form_class = ClientForm

    # def get_context_data(self, **kwargs):
    #     context = super(ClientCreateView, self).get_context_data(**kwargs)
    #     context.update({'family_form': ClientFamilyForm})
    #     return context

    def form_valid(self, form):
        if form.is_valid():
            user = self.request.user
            client = form.save(commit=False)
            client.user = user
            client.save()

    def form_invalid(self, form):
        print(form.errors)
        cxz

class ClientFamilyCreateView(CreateView):
    model = ClientFamily
    template_name = "insurance"


client_create = ClientCreateView.as_view()


def landing_page(request, **kwargs):
    return render(request, "landing/landing.html")