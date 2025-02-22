const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Конфигурация игры
const WORDS = ['javascript', 'programming', 'hangman', 'developer', 'interface', 'algorithm'];
const MAX_ATTEMPTS = 6;

// ASCII-арт для виселицы
const GALLOWS = [
  `
     ------
     |    |
     |
     |
     |
     |
     -
  `,
  `
     ------
     |    |
     |    O
     |
     |
     |
     -
  `,
  `
     ------
     |    |
     |    O
     |    |
     |
     |
     -
  `,
  `
     ------
     |    |
     |    O
     |   /|
     |
     |
     -
  `,
  `
     ------
     |    |
     |    O
     |   /|\\
     |
     |
     -
  `,
  `
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
     -
  `,
  `
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
     -
  `
];

class HangmanGame {
  constructor() {
    this.secretWord = WORDS[Math.floor(Math.random() * WORDS.length)];
    this.guessedLetters = new Set();
    this.attemptsLeft = MAX_ATTEMPTS;
  }

  get maskedWord() {
    return this.secretWord
      .split('')
      .map(c => this.guessedLetters.has(c) ? c : '_')
      .join(' ');
  }

  get status() {
    return `
${GALLOWS[MAX_ATTEMPTS - this.attemptsLeft]}
Слово: ${this.maskedWord}
Осталось попыток: ${this.attemptsLeft}
Использованные буквы: ${[...this.guessedLetters].join(', ')}
    `;
  }

  processGuess(letter) {
    if (this.guessedLetters.has(letter)) {
      console.log('Вы уже пробовали эту букву!');
      return false;
    }

    this.guessedLetters.add(letter);

    if (!this.secretWord.includes(letter)) {
      this.attemptsLeft--;
      return false;
    }

    return true;
  }

  get isWon() {
    return this.secretWord
      .split('')
      .every(c => this.guessedLetters.has(c));
  }

  get isLost() {
    return this.attemptsLeft <= 0;
  }
}

function startGame() {
  const game = new HangmanGame();

  console.log(`
=== ИГРА ВИСЕЛИЦА ===
Угадайте слово по буквам!
`);

  const askLetter = () => {
    console.log(game.status);

    rl.question('Введите букву: ', input => {
      const letter = input.toLowerCase().trim();

      if (!letter.match(/^[а-яё]$/i) && !letter.match(/^[a-z]$/i)) {
        console.log('Пожалуйста, введите одну букву!');
        return askLetter();
      }

      const isCorrect = game.processGuess(letter);

      if (game.isWon) {
        console.log(`
Поздравляем! Вы выиграли!
Загаданное слово: ${game.secretWord}
        `);
        rl.close();
        return;
      }

      if (game.isLost) {
        console.log(`
Игра окончена! Вы проиграли!
Загаданное слово: ${game.secretWord}
${GALLOWS[GALLOWS.length - 1]}
        `);
        rl.close();
        return;
      }

      console.log(isCorrect ? 'Правильно!' : 'Неправильно!');
      askLetter();
    });
  };

  askLetter();
}

// Запуск игры
startGame();