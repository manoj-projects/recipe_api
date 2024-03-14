from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

from core.management.commands.wait_for_db import Command


class CommandTests(SimpleTestCase):
    """Test commands."""

    @patch.object(Command, 'check')  # Patching the method directly
    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if database ready."""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep', return_value=None)  # To prevent actual sleeping
    @patch.object(Command, 'check')
    def test_wait_for_db_delay(self, patched_check, patched_sleep):
        """Test waiting for database when getting OperationalError."""
        patched_check.side_effect = [OperationalError] * 2 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 3)
        patched_check.assert_called_with(databases=['default'])
