import django.conf
import django.contrib.auth
import django.contrib.auth.mixins
import django.contrib.messages
import django.core.mail
import django.core.signing
import django.db.models
import django.forms
import django.http
import django.template.loader
import django.urls
from django.utils.translation import gettext_lazy as _
import django.views.generic

import users.forms
import users.models


__all__ = []


class ProfileEditFormView(django.views.generic.UpdateView):
    success_message = _("profile_edit_success")
    form_class = users.forms.ProfileEditForm
    template_name = "users/profile_edit.html"
    success_url = django.urls.reverse_lazy("users:profile-current")

    def get_object(self, *args, **kwargs):
        return self.request.user


class SignupFormView(django.views.generic.FormView):
    redirect_authenticated_user = True
    form_class = users.forms.SignUpForm
    template_name = "users/signup.html"
    success_url = django.urls.reverse_lazy("users:login")

    def dispatch(self, request, *args, **kwargs):
        if (
            self.redirect_authenticated_user
            and self.request.user.is_authenticated
        ):
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. "
                    "Check that your LOGIN_REDIRECT_URL doesnt point "
                    "to a login page.",
                )

            return django.http.HttpResponseRedirect(redirect_to)

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        print("form valid")
        user = form.save()
        django.contrib.auth.login(self.request, user)

        # django.contrib.messages.success(
        #     self.request,
        #     _("message_signup_success"),
        # )
        return super().form_valid(form)


class ProfileTemplateView(
    django.contrib.auth.mixins.LoginRequiredMixin,
    django.views.generic.TemplateView,
):
    template_name = "users/profile.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["user"] = user
        return context


class ProfileDetailView(django.views.generic.DetailView):
    template_name = "users/profile.html"
    queryset = users.models.User.objects.all()


class UserDeleteView(
    django.contrib.auth.mixins.LoginRequiredMixin,
    django.views.generic.RedirectView,
):
    url = django.urls.reverse_lazy("homepage:main")

    def get(self, request, *args, **kwargs):
        request.user.delete()
        return super().get(request, *args, **kwargs)


class UserListView(django.views.generic.ListView):
    queryset = users.models.User.objects.all()