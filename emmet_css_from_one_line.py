import sublime, sublime_plugin, re

class EmmetMultilineCommand(sublime_plugin.TextCommand):
    
    def run(self, edit):
        
        v = self.view
        line_region = v.line(v.sel()[0])
        line_str = v.substr(line_region)

        # Перевести в массив по пробелу
        props_array = re.findall(r'([a-zA-Z0-9:!;().,?/\-+#]+)', line_str)
        padding = re.findall(r'^(\s+)', line_str)

        # Удаляем текущую строку
        v.replace(edit, line_region, '')

        # Расставляем свойства по строкам
        v.insert(edit, v.sel()[0].end(), padding[0] + props_array[0])
        v.run_command("expand_abbreviation_by_tab")
        
        i = 1
        while i < len(props_array):
            v.insert(edit, v.sel()[0].end(), '\n' + padding[0] + props_array[i])
            # sublime_plugin.WindowCommand.run("")
            v.run_command("expand_abbreviation_by_tab")
            
            i = i + 1

        # Каждый элемент массива преобразовать через Emmet
        # Вывести каждый элемент массива по очереди, добавляя инденты


        sublime.status_message('ds')