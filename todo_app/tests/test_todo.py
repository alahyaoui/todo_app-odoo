from odoo.exceptions import UserError, AccessError
from odoo.tests.common import TransactionCase


class TestTodo(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestTodo, self).setUp(*args, **kwargs)
        # Création d’un nouvel utilisateur pour les tests
        self.fresh_user = self.env['res.users'].create({
            'login': 'bob',
            'name': "Bob Bobman",
        })
        # Recherche de l’utilisateur avec les droits suffisants
        # sur le module
        self.task_manager = self.env.ref('todo_app.task_manager')

    def test_create(self):
        "Create a simple task."
        Todo = self.env['todo.task'].with_user(self.task_manager)
        task = Todo.create({'name': 'Test Task'})
        self.assertEqual(task.is_done, False)
        self.assertEqual(task.active, True)
        self.assertEqual(len(task.team_ids), 0)

    def test_update(self):
        "Update an inactive task."
        Todo = self.env['todo.task'].with_user(self.task_manager)
        task = Todo.create({'name': 'Test Task', 'active': False})
        task.name = 'Test Task Updated'
        self.assertEqual(task.active, True)

    def test_do_clear_done_success(self):
        "Set task active status from True to False with success."
        Todo = self.env['todo.task'].with_user(self.task_manager)
        task = Todo.create({'name': 'Test Task'})
        task.do_clear_done()
        self.assertEqual(task.active, False)

    def test_do_clear_done_error(self):
        "Set task active status from False to False with error."
        Todo = self.env['todo.task'].with_user(self.task_manager)
        task = Todo.create({'name': 'Test Task', 'active': False})
        with self.assertRaises(UserError):
            task.do_clear_done()

    def test_one_copy(self):
        "First Copy of an existing task."
        Todo = self.env['todo.task'].with_user(self.task_manager)
        task = Todo.create({'name': 'Test Task', 'active': False})
        copy_of_task = task.copy()
        self.assertNotEqual(task.name, copy_of_task.name)

    def test_multiple_copy(self):
        "Multiple Copy of an existing task."
        Todo = self.env['todo.task'].with_user(self.task_manager)
        task = Todo.create({'name': 'Test Task', 'active': False})
        copy_of_task1 = task.copy()
        copy_of_task2 = task.copy()
        self.assertNotEqual(task.name, copy_of_task1.name, copy_of_task2.name)

    def test_record_rule(self):
        "Test for a user not in the group"
        Todo = self.env['todo.task'].with_user(self.fresh_user)
        with self.assertRaises(AccessError):
            task = Todo.create({'name': 'NewTask'})
