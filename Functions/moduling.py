# 8-15. Printing Models: Put the functions for the example print_models.py in a
# separate file called printing_functions.py. Write an import statement at the top
# of print_models.py, and modify the file to use the imported functions.

from module1 import make_car as mc

mc('subarro','outback',color='black',nitro=True,year=1982,speed=220)
print(mc.__doc__)


# 8-17. Styling Functions: Choose any three programs you wrote for this chapter,
# and make sure they follow the styling guidelines described in this section.