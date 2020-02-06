from django.shortcuts import render
from django.views import View
from django.views.generic import FormView, CreateView
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import Plan, TrainingSession, TrainingSessionNotes
from .forms import NoteAddForm
from plotly.offline import plot
#from plotly.graph_objects import Scatter
import plotly.graph_objects as go

from django.http import HttpResponse

# Create your views here.

class MainView(View):
    def get(self, request):
        ctx = {}
        return render(request, "html_piwko_po_treningu/base.html", ctx)

class LoginView(FormView):
    form_class = LoginForm
    success_url = "/"
    template_name = "html_piwko_po_treningu/login.html"

    def form_valid(self, form: LoginForm):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(self.request, username=username, password=password)

        if user is None:
            form.add_error(None, "Zły login lub hasło")
            return super().form_invalid(form)

        login(self.request, user)
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")

class PlanList(View):
    def get(self, request):
        plans = Plan.objects.all()
        ctx = {"plans": plans}
        return render(request, "html_piwko_po_treningu/plan_list.html", ctx)


class DetailedPlan(View):
    def get(self,request, plan_id):
        plan = Plan.objects.get(pk=plan_id)
        trainings = list(plan.trainingsession_set.all().order_by('week','day'))
        max_week = trainings[-1].week
        ts_table = []
        for week_no in range(1, max_week+1):
            table_row = [ts for ts in trainings if ts.week==week_no]
            ts_table.append(table_row)

        ctx = {'ts_table': ts_table,
               'plan':plan
               }
        return render(request, 'html_piwko_po_treningu/detailed_plan.html', ctx)

class EditPlan(FormView):
    permission_required = ('auth.user', 'PortalTreningowy.add_trainingsessionnotes')
    form_class = NoteAddForm
    template_name = 'html_piwko_po_treningu/edit_plan.html'
    success_url = 'plans'

    def get_initial(self):
        kwargs = super().get_initial()
        print(self.kwargs['training_session_id'])
        kwargs['training_session'] = TrainingSession.objects.get(pk=self.kwargs['training_session_id'])
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(EditPlan, self).form_valid(form)

class NoteList(View):
    def get(self, request):
        tsnotes = TrainingSessionNotes.objects.all()
        ctx = {"tsnotes": tsnotes}
        return render(request, "html_piwko_po_treningu/ts_notes.html", ctx)


class Vo2max_View(View):
    def get(self, request):
        ts_notes = TrainingSessionNotes.objects.all()
        x_data = [ts_notes[x].date for x  in range(0,len(ts_notes))]
        y_data = [ts_notes[y].user_vo2max for y in range(0, len(ts_notes))]
        plot_div = plot([go.Scatter(x=x_data, y=y_data, text='VO2max [mg/kg/min]',
                        marker_symbol=104, marker_size=10, marker_color='red',
                        mode='markers+lines', name='VO2max',
                        opacity=0.8, showlegend=True)],
                        output_type='div')
        return render(request, "html_piwko_po_treningu/vo2max_view.html", context={'plot_div': plot_div})

class MasaView(View):

    def get(self, request):
        ts_notes = TrainingSessionNotes.objects.all()
        x_data = [ts_notes[x].date for x  in range(0,len(ts_notes))]
        y_data = [ts_notes[y].user_weight for y in range(0, len(ts_notes))]
        plot_div = plot([go.Scatter(x=x_data, y=y_data, text='m [kg]',
                        marker_symbol=300, marker_size=10, marker_color='blue',
                        mode='markers+lines', name='m [kg]',
                        opacity=0.8, showlegend=True)],
                        output_type='div')
        return render(request, "html_piwko_po_treningu/masa.html", context={'plot_div': plot_div})

