import os
import signal

from honcho.process import Process, ProcessManager
from ..helpers import call, patch, assert_equal, FIXTURE_ROOT


class TestProcessManager(object):

    @patch('honcho.process.Process')
    def test_add_processes(self, process_mock):
        pm = ProcessManager()
        pm.add_process('foo', 'ruby server.rb')
        pm.add_process('bar', 'python worker.py')

        expected = [call('ruby server.rb', name='foo', quiet=False),
                    call('python worker.py', name='bar', quiet=False)]

        assert_equal(process_mock.mock_calls, expected)

    @patch('os.kill')
    def test_term_kills_child(self, process_mock):
        os.chdir(FIXTURE_ROOT)
        process = Process('python server.py', name='server', quiet=False)
        process.term(signal.SIGTERM)
        expected = [call(process.pid, signal.SIGTERM)]
        assert_equal(process_mock.mock_calls, expected)
