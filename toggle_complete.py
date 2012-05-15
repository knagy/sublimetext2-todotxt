import sublime, sublime_plugin, re, datetime

class ToggleCompleteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			line = self.view.line(region)
			
			result = re.match(r"^x ", self.view.substr(line))
			if result:
				self.view.replace(edit, sublime.Region(line.begin(), line.begin() + 13), "")
			else:
				self.view.insert(edit, line.begin(), "x " + datetime.date.today().isoformat() + " ")