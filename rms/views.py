from django.shortcuts import redirect, render
from django.views import View


class RMSHomeView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/')
        return render(self.request, 'rms_1_main.html', {})


class RMSStartView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/')
        return render(self.request, 'rms_3.html', {})
