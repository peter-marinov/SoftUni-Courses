from design_patterns.command.coomand import Command


class AddCommand(Command):
    def execute(self, *args):
        self.nums.extend(args)