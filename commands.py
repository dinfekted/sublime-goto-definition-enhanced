import sublime
import sublime_plugin

from GotoDefinitionEnhanced import goto_definition

class GotoDefinitionEnhanced(sublime_plugin.TextCommand):
  def run(self, edit):
    goto_definition.goto_definition(self.view)