from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = "base/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            greeting_text="Welcome! This is Django base project.",
            #
            title="Home Page",
        )

        return context


class AboutUsView(TemplateView):
    template_name = "base/about_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            about="Base project",
            #
            title="About page",
        )

        return context
