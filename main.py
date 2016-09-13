import sublime, sublime_plugin
import traceback

# ================================== #
#                                    #
# You can use the pyv8_loader module #
#    or implement your own module    #
#                                    #
#       import pyv8_loader           #
#                                    #
# ================================== #

import pyv8_loader

class try_pyv8_nowCommand(sublime_plugin.TextCommand):

  def run(self, edit):

    view = self.view
    sel = view.sel()[0]

    # Get the selected text #
    str_selected = view.substr(sel).strip()

    if not str_selected : 
      sublime.error_message("Plese select the text you want to evaluate with PyV8!")
      return

    try:

      # ======================================================== #
      # Here we call the "getV8()" method to get the PyV8 module #
      # ======================================================== #
      PyV8 = pyv8_loader.getV8()
      

      # Now you can use PyV8 #
      ctx = PyV8.JSContext()
      ctx.enter()
      js = str_selected
      result_js = str(ctx.eval(js))

      # It will show the result of evaluation #
      sublime.message_dialog("Result: "+result_js)

    except Exception as e:
      # Ops, you wrote bad JavaScript! :( #
      sublime.error_message("Error: "+traceback.format_exc())


'''
´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶
´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´¶¶
´´´´´´¶¶¶¶¶´´´´´´´¶¶´´´´´´´´´´´´´´¶¶
´´´´´¶´´´´´¶´´´´¶¶´´´´´¶¶´´´´¶¶´´´´´¶¶
´´´´´¶´´´´´¶´´´¶¶´´´´´´¶¶´´´´¶¶´´´´´´´¶¶
´´´´´¶´´´´¶´´¶¶´´´´´´´´¶¶´´´´¶¶´´´´´´´´¶¶
´´´´´´¶´´´¶´´´¶´´´´´´´´´´´´´´´´´´´´´´´´´¶¶
´´´´¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´¶¶
´´´¶´´´´´´´´´´´´¶´¶¶´´´´´´´´´´´´´¶¶´´´´´¶¶
´´¶¶´´´´´´´´´´´´¶´´¶¶´´´´´´´´´´´´¶¶´´´´´¶¶
´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶´´´´¶¶´´´´´´´´¶¶´´´´´´´¶¶
´¶´´´´´´´´´´´´´´´¶´´´´´¶¶¶¶¶¶¶´´´´´´´´´¶¶
´¶¶´´´´´´´´´´´´´´¶´´´´´´´´´´´´´´´´´´´´¶¶
´´¶´´´¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´¶¶
´´¶¶´´´´´´´´´´´¶´´¶¶´´´´´´´´´´´´´´´´¶¶
´´´¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´¶¶
´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶
'''