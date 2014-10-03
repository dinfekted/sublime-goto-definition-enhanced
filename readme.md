# Sublime GotoDefinitionEnhanced plugin

Expanding funcionality of default "goto defintion" sublime feature. Works on top
of default "goto definition".

### Demo

![Demo](https://raw.github.com/shagabutdinov/sublime-goto-definition-enhanced/master/demo/demo.gif "Demo")


### Installation

This plugin is part of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
plugin set. You can install sublime-enhanced and this plugin will be installed
automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
package.


### Usage

Hit keyboard shortcut to go to definition. If cursor is positioned over method
or variable in method call and this method is exists in currently opened file
that cursor will jump to this method without promting. If you want to find
definiton of method in other files hit keyboard shortcut twice. For classes
it'll work as it works by default.


### Commands

| Description     | Keyboard shortcut | Command palette                         |
|-----------------|-------------------|-----------------------------------------|
| Goto definition | ctrl+e            | GotoDefinitionEnhanced: Goto definition |