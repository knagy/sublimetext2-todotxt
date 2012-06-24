import sublime, sublime_plugin, re

class SetPriorityCommand(sublime_plugin.TextCommand):
	def run(self, edit, priority=""):
		for region in self.view.sel():
			line = self.view.line(region)
			
			result = re.match(r"^\([A-Z]\) ", self.view.substr(line))
			if result:
				if priority:
					self.view.replace(edit, sublime.Region(line.begin(), line.begin() + 3), priority)
				else:
					self.view.erase(edit, sublime.Region(line.begin(), line.begin() + 4))
			elif priority:
				self.view.insert(edit, line.begin(), priority + " ")

class IncreasePriorityCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			line = self.view.line(region)
			
			result = re.match(r"^\(([A-Z])\) ", self.view.substr(line))
			if result:
				letter = result.group(1)
				if letter != "A":
					self.view.replace(edit, sublime.Region(line.begin(), line.begin() + 3), "(" + chr(ord(letter) - 1) + ")")
			else:
				self.view.insert(edit, line.begin(), "(Z) ")

class DecreasePriorityCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			line = self.view.line(region)
			
			result = re.match(r"^\(([A-Z])\) ", self.view.substr(line))
			if result:
				letter = result.group(1)
				if letter != "Z":
					self.view.replace(edit, sublime.Region(line.begin(), line.begin() + 3), "(" + chr(ord(letter) + 1) + ")")
				else:
					self.view.erase(edit, sublime.Region(line.begin(), line.begin() + 4))
