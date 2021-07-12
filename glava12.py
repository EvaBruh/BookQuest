# Глава 12
#
# import unittest
#
#
# class NameTestCase(unittest.TestCase):
#     def test_first_last_name(self):
#         """Names Jaa Jaa work?"""
#         formated = message('janis', 'joplin')
#         self.assertEqual(formated, 'Janis Joplin')
#
#     def test_mid_first_last_name(self):
#         """Names Jaa Jaa work?"""
#         formated = message('janis', 'joplin', 'jopa')
#         self.assertEqual(formated, 'Janis Joplin Jopa')
#
#
# if __name__ == '__main__':
#     unittest.main()
#
#
# def main():
#     first = ''
#     last = ''
#     mid = ''
#     print(message(first, mid, last))
#
#
# def message(first, mid, last):
#     if mid:
#         name = f'{first} {mid} {last}'
#     else:
#         name = f'{first} {last}'
#
#     return name.title()
#
#
# main()
