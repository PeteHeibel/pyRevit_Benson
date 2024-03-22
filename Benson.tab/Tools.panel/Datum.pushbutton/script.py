from pyrevit import revit, DB, forms

# Get the active view
view = revit.doc.ActiveView

# Name of the subcategory to turn off
subCategory = "Datum Symbol"

if view.ViewTemplateId == DB.ElementId.InvalidElementId:
    if str(view.DetailLevel) == "Coarse":
        try:
            # Get a subcategory of the Detail Item model category by name
            category = revit.doc.Settings.Categories.get_Item(DB.BuiltInCategory.OST_DetailComponents).SubCategories.get_Item(subCategory);

            # Wrap the visibility toggle in a transaction
            with revit.Transaction("Toggle Datum Symbol Visibility"):
                # Get the current hidden state and toggle directly
                new_hidden = not view.GetCategoryHidden(category.Id)
                view.SetCategoryHidden(category.Id, new_hidden)

                # Display result to user
                # forms.alert(category.Name + " visibility is " + str(new_hidden), title="Result", warn_icon=False)
        except:
            forms.alert(subCategory + "s could not be found in this document.", title="Result", warn_icon=False)
    else:
        forms.alert("Datum Symbols are only visible in views with a 'Coarse' Detail Level.")
else:
    forms.alert("Datum Symbols are controlled by the active view's View Template.")
