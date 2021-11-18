from odoo.exceptions import UserError
from odoo.tests.common import TransactionCase


class TestTodo(TransactionCase):

    def test_create(self):
        "Create a simple task."
        Todo = self.env['todo.task']
        task = Todo.create({'name': 'Test Task'})
        self.assertEqual(task.is_done, False)
        self.assertEqual(task.active, True)
        self.assertEqual(len(task.team_ids), 0)

    def test_update(self):
        "Update an inactive task."
        Todo = self.env['todo.task']
        task = Todo.create({'name': 'Test Task', 'active': False})
        task.name = 'Test Task Updated'
        self.assertEqual(task.active, True)

    def test_do_clear_done_success(self):
        "Set task active status from True to False with success."
        Todo = self.env['todo.task']
        task = Todo.create({'name': 'Test Task'})
        task.do_clear_done()
        self.assertEqual(task.active, False)

    def test_do_clear_done_error(self):
        "Set task active status from False to False with error."
        Todo = self.env['todo.task']
        task = Todo.create({'name': 'Test Task', 'active': False})
        with self.assertRaises(UserError):
            task.do_clear_done()

    def test_one_copy(self):
        "First Copy of an existing task."
        Todo = self.env['todo.task']
        task = Todo.create({'name': 'Test Task', 'active': False})
        copy_of_task = task.copy()
        self.assertNotEqual(task.name, copy_of_task.name)

    def test_multiple_copy(self):
        "Multiple Copy of an existing task."
        Todo = self.env['todo.task']
        task = Todo.create({'name': 'Test Task', 'active': False})
        copy_of_task1 = task.copy()
        copy_of_task2 = task.copy()
        self.assertNotEqual(task.name, copy_of_task1.name, copy_of_task2.name)
