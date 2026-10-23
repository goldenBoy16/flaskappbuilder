from flask import render_template

from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from .extensions import appbuilder

from .models import Categoria, Ingrediente


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )

class CategoriaView(ModelView):
    datamodel = SQLAInterface(Categoria)
 
    label_columns = {"nombre": "Nombre",
                     "descripcion": "Descripcion",
                     "activo": "Activo",
                     "ingredientes": "Ingredientes"
                    }
   
    list_columns = ["nombre", "descripcion", "activo"]
 
    show_columns = [ "id", "nombre", "descripcion", "activo", "ingredientes"]
   
    add_columns = ["nombre", "descripcion", "activo"]
   
    edit_columns = ["nombre", "descripcion", "activo"]
   
    order_columns = ["nombre"]
   
   
   
   
class IngredientView(ModelView):
    datamodel = SQLAInterface(Ingrediente)
 
    label_columns = {"nombre": "Nombre",
                     "categoria": "Categoria",
                     "cantidad": "Cantidad",
                     "unidad_medida": "Unidad de Medida",
                     "costo_unitario": "Costo Unitario",
                     "stock_minimo" : "Stock Minimo",
                     "fecha_vencimiento" : "Fecha de Vencimiento",
                     "activo" : "Activo"
                    }
   
    list_columns = ["nombre",
                     "categoria",
                     "cantidad",
                     "unidad_medida",
                     "costo_unitario",
                     "stock_minimo",
                     "fecha_vencimiento",
                     "activo"]
 
    show_columns = [ "id", "nombre",
                     "categoria",
                     "cantidad",
                     "unidad_medida",
                     "costo_unitario",
                     "stock_minimo",
                     "fecha_vencimiento",
                     "activo"]
   
    add_columns = ["nombre",
                     "categoria",
                     "cantidad",
                     "unidad_medida",
                     "costo_unitario",
                     "stock_minimo",
                     "fecha_vencimiento",
                     "activo"]

    show_columns = ["id"] + list_columns
    add_columns = list_columns
    edit_columns = add_columns
    search_columns = ["nombre"]
    order_columns = ["nombre"]

# Registro de vistas en el menú de Flask-AppBuilder
appbuilder.add_view(
    CategoriaView,
    "Modulo Categorías",
    icon="fa-folder-open",
    category="Inventario",
)

appbuilder.add_view(
    IngredientView,
    "Modulo Ingredientes",
    icon="fa-cubes",
    category="Inventario",
)