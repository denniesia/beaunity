from django.db.models import Count, Q
from django.utils.timezone import now

from beaunity.category.models import Category
from beaunity.challenge.models import Challenge
from beaunity.common.forms import SearchForm
from oauthlib.uri_validate import query


class FilteredQuerysetMixin:
    def get_filtered_queryset(self):
        current_datetime = now()
        archived = self.request.GET.get('archived', '').lower() == 'true'

        if archived:
            queryset = self.model.objects.filter(
                end_time__lt=current_datetime
            )
        else:
            queryset = self.model.objects.filter(
                end_time__gte=current_datetime
            )

        city = self.request.GET.get('city')
        category = self.request.GET.get('category')
        sort_by = self.request.GET.get('sort_by')
        online = self.request.GET.get('online')
        difficulty = self.request.GET.get('difficulty')
        query = self.request.GET.get('query')

        form = SearchForm(self.request.GET)

        if form.is_valid():
            query = form.cleaned_data.get('query')
            if query:
                queryset = queryset.filter(
                    title__icontains=query)

        if city:
            queryset = queryset.filter(city=city)

        if category:
            queryset = queryset.filter(categories__title=category)

        if online:
            queryset = queryset.filter(is_online=True)

        if sort_by:
            if sort_by == 'Popularity':
                queryset = queryset.annotate(
                    popularity=Count('attendees')
                ).order_by(
                    '-popularity'
                )
            elif sort_by == 'Public':
                queryset = queryset.filter(is_public=True)
            elif sort_by == 'Hosts':
                queryset = queryset.order_by('created_by__username')


        if difficulty == 'Beginner':
            queryset = queryset.filter(difficulty='Beginner')
        elif difficulty == 'Intermediate':
            queryset = queryset.filter(difficulty='Intermediate')
        elif difficulty == 'Advanced':
            queryset = queryset.filter(difficulty='Advanced')
        elif difficulty == 'Legendary':
            queryset = queryset.filter(difficulty='Legendary')

        if self.model == Challenge:
            if sort_by == 'Popularity':
                return queryset.filter(is_approved=True).distinct()
            return queryset.filter(is_approved=True).distinct().order_by(*self.ordering)

        if sort_by == 'Popularity':
            return queryset.distinct()
        return queryset.distinct().order_by(*self.ordering)

class FilteredContextMixin:
    def get_filtered_context(self, context, model):
        request = self.request
        applied_filters = {}
        query = ''

        if request.GET.get('query'):
            query = request.GET.get('query')
        if request.GET.get('city'):
            applied_filters['city'] = request.GET['city']
        if request.GET.get('category'):
            applied_filters['category'] = request.GET['category']
        if request.GET.get('sort_by'):
            applied_filters['Sorted by'] = request.GET['sort_by']
        if request.GET.get('online'):
            applied_filters['online'] = 'Online'
        if request.GET.get('archived'):
            applied_filters['archived'] = True

        #only for challenge
        if request.GET.get('difficulty'):
            applied_filters['difficulty'] = request.GET['difficulty']

        context['filter_mode'] = bool(applied_filters)
        context['applied_filters'] = applied_filters
        context['query'] = query

        context['categories'] = Category.objects.all()
        context['cities'] = model.objects.exclude(
            city=None
        ).exclude(
            city=''
        ).values_list(
            'city', flat=True
        ).distinct()

        context['model_name'] = model.__name__
        return context