from django import forms

from issues.models import Issue
from triage.models import ProgrammingLanguage, COMPLEXITY_LEVEL

COMPLEXITY_LEVEL_WITH_EMPTY = [
    (None, 'Not Rated'),
    ('all', 'All Rates')
] + COMPLEXITY_LEVEL


class SearchForm(forms.Form):
    language = forms.ModelChoiceField(queryset=ProgrammingLanguage.objects.all(), to_field_name='name', required=True)
    rate = forms.ChoiceField(choices=COMPLEXITY_LEVEL_WITH_EMPTY, required=False, label="Difficult Level", initial='all')

    @property
    def results(self):
        if not self.is_valid():
            return Issue.objects.all().order_by('-created_at')[:20]

        rate = self._get_rate()

        query = dict(
            main_language=self.cleaned_data.get('language'),
        )

        if rate != 'all':
            query.update(current_rate__rate=rate)

        return Issue.objects.filter(**query).order_by('-created_at')[:1000]

    @property
    def search_title(self):
        if not self.is_valid():
            return 'Be a contributor to open source'

        language = self.cleaned_data.get('language')
        return f'Let me contrib with {language} to Open Source'

    @property
    def search_meta_description(self):
        if not self.is_valid():
            return 'Find an issue that is perfect with your skills and contribute to open source projects.'

        language = self.cleaned_data.get('language')
        return f'Find an {language} issue that is perfect with your skills and contribute to open source projects.'

    def _get_rate(self):
        rate = self.cleaned_data.get('rate')

        if not rate:
            return None

        return rate
