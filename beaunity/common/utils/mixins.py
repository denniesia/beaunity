from django.db.models import Count
from django.utils.timezone import now


from beaunity.category.models import Category

class FilteredQuerysetMixin:
    model = None  # Set this in the view using the mixin

    def get_filtered_queryset(self):
        current_datetime = now()
        archived = self.request.GET.get('archived', '').lower() == 'true'

        if not self.model:
            raise ValueError("Model not specified in the view using FilteredQuerysetMixin.")

        if archived:
            queryset = self.model.objects.filter(end_time__lt=current_datetime)
        else:
            queryset = self.model.objects.filter(end_time__gte=current_datetime)

        city = self.request.GET.get('city')
        category = self.request.GET.get('category')
        sort_by = self.request.GET.get('sort_by')
        online = self.request.GET.get('online')

        if city:
            queryset = queryset.filter(city=city)

        if category:
            queryset = queryset.filter(categories__title=category)

        if online:
            queryset = queryset.filter(is_online=True)

        if sort_by == 'Popularity':
            queryset = queryset.annotate(popularity=Count('attendees')).order_by('-popularity')
        elif sort_by == 'Public events':
            queryset = queryset.filter(is_public=True)
        elif sort_by == 'Hosts':
            queryset = queryset.order_by('created_by__username')

        if sort_by not in ['Popularity', 'Hosts']:
            queryset = queryset.order_by('start_time')

        return queryset.distinct()

class FilteredContextMixin:
    def get_filtered_context(self, context, model):
        request = self.request
        applied_filters = {}

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

        context['applied_filters'] = applied_filters
        context['filter_mode'] = bool(applied_filters)
        context['categories'] = Category.objects.all()
        context['cities'] = model.objects.exclude(city='').values_list('city', flat=True).distinct()
        return context