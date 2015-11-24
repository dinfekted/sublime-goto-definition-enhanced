import sublime
import sublime_plugin

import re

try:
  from Statement import statement
  from LocalVariable import local_variable
  from Method import method
except ImportError as error:
  sublime.error_message("Dependency import failed; please read readme for " +
    "GotoDefinitionEnhanced plugin for installation instructions; to disable " +
    "this message remove this plugin; message: " + str(error))
  raise error

def goto_definition(view):
  if len(view.sel()) != 1:
    return

  if view.sel()[0].empty() == False:
    view.window().run_command('goto_definition')
    return

  point = view.sel()[0].b
  definition_point = _get_definition_point(view, point)
  if definition_point == None or definition_point == point:
    constant_point = _get_fallback_point(view, point)
    if constant_point != None:
      view.sel().clear()
      view.sel().add(sublime.Region(constant_point, constant_point))

    view.window().run_command('goto_definition')
  else:
    view.sel().clear()
    view.sel().add(sublime.Region(definition_point, definition_point))
    view.show(definition_point)

def _get_fallback_point(view, point):
  point_scope = view.scope_name(point)
  if 'constant' in point_scope or 'class' in point_scope:
    return point

  token = statement.get_token(view, point)

  if token == None:
    return None

  _, token = token
  while True:
    text = view.substr(sublime.Region(*token))
    call = re.search(r'(\w+[?!]?)\(', text)
    if call != None:
      return token[0] + call.end(1)

    token_scope = view.scope_name(token[0])
    if 'constant' in token_scope or 'class' in token_scope:
      return token[0]

    match = re.search(r'([a-z])|([A-Z])', text)
    if match.start(1) == -1 and match.group(2) != -1:
      return token[0]

    point = token[0]
    token = statement.get_parent_token(view, point)
    if token == None:
      return None

def _get_definition_point(view, point):
  methods = method.extract_methods(view)
  token = statement.get_token(view, point)
  if token == None:
    return None

  _, token = token
  while True:
    definition = _get_token_definition_point(view, methods, token)
    if definition != None:
      return definition

    point = token[0]
    token = statement.get_parent_token(view, point)
    if token == None:
      return None

def _get_token_definition_point(view, methods, token):
  method_name = re.search(r'\w+[?!]?', view.substr(sublime.Region(*token)))
  for current_method in methods:
    if method_name.group(0) != current_method['name']:
      continue

    region = sublime.Region(current_method['start'],
      current_method['body_start'])

    match = re.search(re.escape(method_name.group(0)), view.substr(region))
    if match == None:
      return None

    return region.a + match.end(0)

  return None