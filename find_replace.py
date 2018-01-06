import re

import sublime
import sublime_plugin


class FindReplaceCommand(sublime_plugin.TextCommand):
    """The implementation of 'find_replace' text command.

    Example:

        view.run_command(
            "find_replace", {
                "pattern": "the",
                "replace_by": "THE",
                "start_pt": 100,
                "flags": ["LITERAL", "ALL"]
            }
        )
    """

    FLAGS = {
        "ALL": 0,  # for internal use to replace all appearances
        "LITERAL": sublime.LITERAL,
        "IGNORECASE": sublime.IGNORECASE
    }

    def run(self, edit, pattern, replace_by, start_pt=0, flags=[]):
        """Find and replace all patterns.

        Arguments:
            edit (sublime.Edit):
                The edit token used to undo this command.
            pattern (string):
                The regex pattern to use for finding.
            replace_by (string):
                The text to replace all found words by.
            start_pt (int):
                The text position where to start.
            flags (list):
                The flags to pass to view.find()
                ["ALL", "LITERAL", "IGNORECASE"]
        """
        int_flags = self._flags(flags)

        def replace(region):
            if int_flags & sublime.LITERAL:
                self.view.replace(edit, found, replace_by)
            else:
                self.view.replace(edit, found, re.sub(
                    pattern, replace_by, self.view.substr(found),
                    flags=re.I if int_flags & sublime.IGNORECASE else 0
                ))

        if "ALL" in flags:
            for found in reversed(self.view.find_all(pattern, int_flags)):
                replace(found)
        else:
            found = self.view.find(pattern, int_flags, start_pt)
            if found:
                replace(found)

    def _flags(self, flags):
        """Translate list of flags."""
        result = 0
        for flag in flags:
            result |= self.FLAGS.get(flag, 0)
        return result

