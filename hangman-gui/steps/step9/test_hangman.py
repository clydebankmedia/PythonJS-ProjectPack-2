# test_hangman.py (separate from your app file)
import unittest
from hangman import HangmanGame

# Just a few tests; not very thorough.
class TestHangman(unittest.TestCase):
  def test_init(self):
    g = HangmanGame("foo", 3)
    self.assertEqual(g.get_display(), "___")
    self.assertFalse(g.already_guessed('f'))
    self.assertEqual(g.remaining_guesses, 3)
    self.assertEqual(g.status, HangmanGame.GameStatus.IN_PROGRESS)

  def test_guess_letter_success(self):
    g = HangmanGame("foo", 3)
    g.guess_letter('f')
    self.assertEqual(g.get_display(), "f__")
    self.assertTrue(g.already_guessed('f'))
    self.assertEqual(g.remaining_guesses, 2)
    self.assertEqual(g.status, HangmanGame.GameStatus.IN_PROGRESS)

  def test_guess_letter_failure(self):
    g = HangmanGame("foo", 3)
    g.guess_letter('x')
    self.assertEqual(g.get_display(), "___")
    self.assertTrue(g.already_guessed('x'))
    self.assertEqual(g.remaining_guesses, 2)
    self.assertEqual(g.status, HangmanGame.GameStatus.IN_PROGRESS)

  def test_guess_letter_multi(self):
    g = HangmanGame("foo", 3)
    g.guess_letter('o')
    self.assertEqual(g.get_display(), "_oo")
    self.assertTrue(g.already_guessed('o'))
    self.assertEqual(g.remaining_guesses, 2)
    self.assertEqual(g.status, HangmanGame.GameStatus.IN_PROGRESS)

  def test_guess_word(self):
    g = HangmanGame("foo", 3)
    g.guess_word('bar')
    self.assertEqual(g.get_display(), "___")
    self.assertTrue(g.already_guessed('bar'))
    self.assertEqual(g.remaining_guesses, 2)
    self.assertEqual(g.status, HangmanGame.GameStatus.IN_PROGRESS)

  def test_win_word(self):
    g = HangmanGame("foo", 3)
    g.guess_word('foo')
    self.assertEqual(g.get_display(), "foo")
    self.assertTrue(g.already_guessed('foo'))
    self.assertEqual(g.remaining_guesses, 2)
    self.assertEqual(g.status, HangmanGame.GameStatus.WON)

  def test_lose_word(self):
    g = HangmanGame("foo", 1)
    g.guess_word("bar")
    self.assertEqual(g.get_display(), "___")
    self.assertTrue(g.already_guessed('bar'))
    self.assertEqual(g.remaining_guesses, 0)
    self.assertEqual(g.status, HangmanGame.GameStatus.LOST)

  def test_win_letter(self):
    g = HangmanGame("foo", 3)
    g.guess_letter('f')
    g.guess_letter('o')
    self.assertEqual(g.get_display(), "foo")
    self.assertTrue(g.already_guessed('f'))
    self.assertTrue(g.already_guessed('o'))
    self.assertEqual(g.remaining_guesses, 1)
    self.assertEqual(g.status, HangmanGame.GameStatus.WON)

  def test_lose_letter(self):
    g = HangmanGame("foo", 2)
    g.guess_letter('f')
    g.guess_letter('e')
    self.assertEqual(g.get_display(), "f__")
    self.assertTrue(g.already_guessed('f'))
    self.assertTrue(g.already_guessed('e'))
    self.assertEqual(g.remaining_guesses, 0)
    self.assertEqual(g.status, HangmanGame.GameStatus.LOST)

if __name__ == "__main__":
  unittest.main()
