#
# To debug a Python function,
#  * make sure the function is imported into this file
#      (i.e., use   from is_legal import is_a_legal_coloring
#      if you want to debug the is_a_legal_coloring function)
#  * call the function you want to debug once (as per the is_a_legal_coloring example below)
#  * double-click on the left margin to get a 'thumb tack' on the function call
#  * right-click on this file in the Navigator pane on the left of your Eclipse window,
#    and choose Debug As->Python Run
#  * click "ok" when asked about changing perspectives
#
#  then debug the program, as illustrated in lecture
#
#  When done, remember to:
#  * stop the program by clicking on the "red box" in the upper left pane
#    (if that box is grey rather than red, the program is already stopped)
#  * right-click on "Debug" in your perspectives menu and choose "close"
#


from is_legal import is_a_legal_coloring
from graph_coloring import collect_legal_colorings

is_a_legal_coloring('Mr Yb Vg Hb Cg Rb Ar', 'HV HM VM VY MR MC MY CR CY AC YA')
collect_legal_colorings("AH", "rgb", "")