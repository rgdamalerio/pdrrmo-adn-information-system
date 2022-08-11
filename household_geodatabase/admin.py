from django.contrib import admin

class MyAdminSite(admin.AdminSite):
  def get_app_list(self, request):
      ordering = {
          "Households": 1,
          "Demographies": 2,
          "Avail Programs": 3,
          "Livelihoods": 4,
          "Municipalities": 5,
          "Barangays": 6,
          "Building roof materials": 7,
          "Building status": 8,
          "Building types": 9,
          "Building uses": 10,
          "Building wall materials": 11,
          "Disabilities":12,
          "Farming technology": 13,
          "Genders": 14,
          "Grade levels": 15,
          "Evacuation areas": 16,
          "Water level systems": 17,
          "Household roof materials": 18,
          "Household tenural status": 19,
          "Household building types": 20,
          "Household wall materials": 21,
          "Household water tenural status": 22,
          "Livelihoods": 23,
          "Marital status": 24,
          "Monthly incomes": 25,
          "Nutritional status": 26,
          "Relationship to head": 27,
          "Livelihood tenural status": 28,
          "Track/strand/courses": 29,
          "Type of programs": 30,
          "Groups": 31,
          "Users": 32
      }
      app_dict = self._build_app_dict(request)
      # a.sort(key=lambda x: b.index(x[0]))
      # Sort the apps alphabetically.
      app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
      # Sort the models alphabetically within each app.
      for app in app_list:
          app['models'].sort(key=lambda x: ordering[x['name']])
      return app_list
