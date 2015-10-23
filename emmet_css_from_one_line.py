import sublime, sublime_plugin, re

class EmmetCssFromOneLineCommand(sublime_plugin.TextCommand):
    
    def run(self, edit):
        
        view = self.view
        line_region = view.line(view.sel()[0])
        line_str = view.substr(line_region)
        left_padding = re.findall(r'^(\s+)', line_str)[0]

        # find commands in line
        props_array = re.findall(r'([a-zA-Z0-9:!;().,?/\-+#]+)', line_str)
        
        # Delete long string
        view.replace(edit, line_region, '')

        def runEmmet():
            view.run_command("expand_abbreviation_by_tab")

        # Processing first element
        view.insert(edit, view.sel()[0].end(), left_padding + props_array[0])
        runEmmet()
        
        i = 1
        while i < len(props_array):
            view.insert(edit, view.sel()[0].end(), '\n' + left_padding + props_array[i])
            runEmmet()
            i += 1
