from rest_framework import filters


class BookFilter(FilterSet):
    class Meta:
        model = BookDetail
        fields = {
            'title': ['exact', 'in', 'startswith'],
            'author': ['exact', 'in', 'startswith'],
            'editor': ['exact', 'in', 'startswith'],
            'publisher': ['exact', 'in', 'startswith'],
            'cl_num': ['exact', 'in', 'startswith']
        }


class CopyFilter(FilterSet):
    book_details = RelatedFilter(BookFilter, name="title",  queryset=BookDetail.objects.all())

    class Meta:
        model = BookCopy
        fields = {
            'ref_id': ['exact', 'in', 'startswith']
        }