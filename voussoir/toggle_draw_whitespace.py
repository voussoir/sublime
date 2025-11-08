'''
Thank you facelessuser
https://forum.sublimetext.com/t/keybinding-draw-white-space-toggle/5122
'''
import sublime
import sublime_plugin

class ToggleDrawWhitespaceCommand(sublime_plugin.TextCommand):
    def run(self, edit, options=["selection", "all"]):
        try:
            current = self.view.settings().get("draw_white_space", "selection")
            index = options.index(current)
        except:
            index = 0

        index = (index + 1) % len(options)
        self.view.settings().set("draw_white_space", options[index])
