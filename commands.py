import sublime
import sublime_plugin

from GotoDefinitionEnhanced import goto_definition

def _get_definition(self):
  pass

class GotoDefinitionEnhanced(sublime_plugin.TextCommand):
  def run(self, edit):
    goto_definition.goto_definition(self.view)