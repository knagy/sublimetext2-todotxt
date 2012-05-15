import sublime, sublime_plugin, re, datetime

class ToggleCompleteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			line = self.view.line(region)
			
			data = self.view.substr(line)
			if re.match(r"^x [0-9]{4}-[0-9]{2}-[0-9]{2} ", data):
				self.view.erase(edit, sublime.Region(line.begin(), line.begin() + 13))
			elif re.match(r"^x ", data):
				self.view.erase(edit, sublime.Region(line.begin(), line.begin() + 2))
			else:
				self.view.insert(edit, line.begin(), "x " + datetime.date.today().isoformat() + " ")