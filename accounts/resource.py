from import_export import resources
from .models import Univ_category

class Univ_Resource(resources.ModelResource):
    class Meta:
        model = Univ_category