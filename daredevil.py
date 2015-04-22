import sublime, sublime_plugin

enabled = None

class ListenerCommand(sublime_plugin.EventListener):
    def on_selection_modified_async(self, view):
        view.run_command("daredevil_highlight")

    def on_activated(self, view):
        global enabled
        enabled = view.settings().get("enable_daredevil", False)

class DaredevilHighlightCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global enabled
        if enabled:
            sel = self.view.sel()[0]
            (line_number, _) = self.view.rowcol(sel.begin())
            region = self.view.text_point(line_number, 0)
            line = self.view.line(region)
            self.view.add_regions('put-some-bg-color', [line],
                'keyword', 'circle', sublime.DRAW_NO_FILL)
