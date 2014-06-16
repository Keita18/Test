import sublime, sublime_plugin
import os

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, test!")
		os.system("sleep")
		os.system("sleep")
