import sublime, sublime_plugin, re

class SetPriorityCommand(sublime_plugin.TextCommand):
	def run(self, edit, priority=""):
		for region in self.view.sel():
			line = self.view.line(region)
			
			result = re.match(r"^\([ABC]\) ", self.view.substr(line))
			if result:
				if priority:
					self.view.replace(edit, sublime.Region(line.begin(), line.begin() + 3), priority)
				else:
					self.view.erase(edit, sublime.Region(line.begin(), line.begin() + 4))
			elif priority:
				self.view.insert(edit, line.begin(), priority + " ")