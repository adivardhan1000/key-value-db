import unittest
from db_commands import Commands
from read_input_cmd import parse_string_call_db_commands

class Test(unittest.TestCase):

    def setUp(self):
        self.c = Commands()

    def test_connection(self):
        self.assertTrue(self.c.checkConnection())

    def test_commands(self):
        self.assertTrue(parse_string_call_db_commands(self.c, 'SET abc 5'))
        self.assertEqual(parse_string_call_db_commands(self.c, 'GET abc').decode(),'5')
        self.assertEqual(parse_string_call_db_commands(self.c, 'INCR abc'),6)
        self.assertEqual(parse_string_call_db_commands(self.c, 'INCRBY abc 5'),11)
        self.assertTrue(parse_string_call_db_commands(self.c, 'DEL abc'))
        self.assertIsNone(parse_string_call_db_commands(self.c, 'GET abc'))

    def test_multi_commands(self):
        parse_string_call_db_commands(self.c, 'MULTI')
        parse_string_call_db_commands(self.c, 'SET abc 5')
        parse_string_call_db_commands(self.c, 'SET abcd 5')
        parse_string_call_db_commands(self.c, 'GET abc')
        parse_string_call_db_commands(self.c, 'INCR abc'),
        parse_string_call_db_commands(self.c, 'INCRBY abc 5')
        parse_string_call_db_commands(self.c, 'DEL abcd')
        parse_string_call_db_commands(self.c, 'EXEC')
        self.assertEqual(parse_string_call_db_commands(self.c, 'GET abc').decode(),'11')        
        self.assertIsNone(parse_string_call_db_commands(self.c, 'GET abcd'))

    def test_discard_command(self):
        parse_string_call_db_commands(self.c, 'DEL abc')
        parse_string_call_db_commands(self.c, 'MULTI')
        parse_string_call_db_commands(self.c, 'SET abc 5')
        parse_string_call_db_commands(self.c, 'SET abcd 5')
        parse_string_call_db_commands(self.c, 'GET abc')
        parse_string_call_db_commands(self.c, 'INCR abc'),
        parse_string_call_db_commands(self.c, 'INCRBY abc 5')
        parse_string_call_db_commands(self.c, 'DEL abcd')
        parse_string_call_db_commands(self.c, 'DISCARD')
        # self.assertEqual(parse_string_call_db_commands(self.c, 'GET abc').decode(),'11')        
        self.assertIsNone(parse_string_call_db_commands(self.c, 'GET abc'))
    
    def test_compact(self):
        self.assertTrue(parse_string_call_db_commands(self.c, 'SET abc 5'))
        self.assertEqual(parse_string_call_db_commands(self.c, 'GET abc').decode(),'5')
        self.assertEqual(parse_string_call_db_commands(self.c, 'INCR abc'),6)
        self.assertEqual(parse_string_call_db_commands(self.c, 'INCRBY abc 5'),11)
        output =parse_string_call_db_commands(self.c, 'COMPACT')
        expectedOutput = ['SET abc 11']
        self.assertEqual(output, expectedOutput)

    def test_exceptions(self):
        self.assertFalse(parse_string_call_db_commands(self.c, 'SETA abc 5'))
        self.assertFalse(parse_string_call_db_commands(self.c, 'SET abc'))
        parse_string_call_db_commands(self.c, 'SET abc ab')
        self.assertFalse(parse_string_call_db_commands(self.c, 'INCR abc'))
        self.assertFalse(parse_string_call_db_commands(self.c, 'INCRBY abc 15'))


if __name__=="__main__":
    unittest.main()