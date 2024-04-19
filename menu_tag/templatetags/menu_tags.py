from django import template
from ..models import Menu
from django.db.models import Prefetch


register = template.Library()


@register.inclusion_tag("menu_cat.html", takes_context=True)
def draw_menu(context, cat_name):
    categories = Menu.objects.all()
    menu_dict = {}
    for cat in categories:
        menu_dict[cat.pk] = {"item": cat, "children": [], "expanded": False}

    print(menu_dict)
    request = context["request"]
    # current_url = request.path
    for key, value in menu_dict.items():
        item = value["item"]
        print(item.slug, cat_name)

        if item.slug == cat_name:
            value ['expanded'] = True
            print('hereeee')
            parent_id = item.parent_id
            while parent_id:
                if parent_id in menu_dict:
                    menu_dict[parent_id]["expanded"] = True
                    parent_id = menu_dict[parent_id]["item"].parent_id
                else:
                    break 


            for child in value["children"]:
                child["expanded"] = True

    print("MENU_DICT:", menu_dict)
    root_items = []
    for cat in categories:
        if cat.parent:
            menu_dict[cat.parent_id]["children"].append(menu_dict[cat.pk])
        else:
            root_items.append(menu_dict[cat.pk])

    print("ROOT_ITEMS:", root_items)
    return {"menu_items": root_items}
    