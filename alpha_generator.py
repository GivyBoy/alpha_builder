"""
Controls the generation of the alpha returns
"""
# Local imports
from alpha_builder import FormulaicAlphaBuilder  # builds the alphas
import alpha_functions  # module that houses all the alpha functions

# `dir(alpha_functions)` returns all functions within the specified file,
# afterwich all the alpha functions are filtered out, for the alphas that
# start with `alpha`. All custom alphas will have the `custom` prefix
alpha_funcs = [func for func in dir(alpha_functions) if str(func)
               .startswith("alpha")]
alpha_list = list(map(lambda alpha_func: FormulaicAlphaBuilder(
    alpha_func=alpha_func, start_date="19991231", vol_target=0.2),
    alpha_funcs))
print(len(alpha_list))  # prints 'pointers' to all the alpha objects

alpha_list.append(
    # this is used to manually instantiate the classes for signals that
    # have customized components
    FormulaicAlphaBuilder(alpha_func=alpha_functions.custom_alpha_04,
                          start_date="20011231", vol_target=0.1),
)

print(len(alpha_list))
