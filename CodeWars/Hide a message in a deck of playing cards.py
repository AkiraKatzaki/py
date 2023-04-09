"""
An OOP learning excersie in python.
"""

import random


class Card():
    """A playing card object
        Parameters
        ----------
            value : int
                The value of a card. 1 is Ace. 11 is Jack. 12 is Queen. 13 is King.
            suit : str
                The suit of the card. Generally 'Spades', 'Hearts', 'Diamonds', or 'Clubs'.
        Attributes
        -----------
            hidden : bool
                If true, the card is "face down" and can't be viewed with the show() method.
    """

    def __init__(self, value: int, suit: str, hidden=False):

        self._value = value
        self._suit = suit
        self._hidden = hidden

    @property
    def value(self):
        """Returns the numerical value of the card. Returns None if self.hidden is set to True"""
        if not self._hidden:
            return self._value
        else:
            return None

    @property
    def suit(self):
        """Returns the suit of the card. Returns None if self.hidden is set to True"""
        if not self._hidden:
            return self._suit
        else:
            return None

    @property
    def hidden(self):
        """Returns True if the card is hidden, False if the card is not hidden."""
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):

        if hidden.__class__ != bool:
            raise TypeError('Must be bool type.')
        self._hidden = hidden
        return self

    def changeHidden(self, hidden=None):
        """Changes the value of hidden. This is like showing a card from a players hand
        or revealing a face down card.
        """
        if hidden is None:
            self._hidden = not self._hidden
            return self

        if hidden.__class__ == bool:
            self._hidden = hidden
            return self
        else:
            raise TypeError("Must be bool type.")

    def show(self):
        """Prints the value and suit of the Card object."""

        if self.hidden:
            print("This card is hidden.")
            return None

        if self.value == 1:
            print(f'Ace of {self.suit}')
        elif self.value < 11:
            print(f'{self.value} of {self.suit}')
        elif self.value == 11:
            print(f'Jack of {self.suit}')
        elif self.value == 12:
            print(f'Queen of {self.suit}')
        else:
            print(f'King of {self.suit}')

    # Ordering functions:

    #     These functions define an order on the cards. Note, the order depends entirely
    #     on the value of the card and nothing else. Bacause of this, two cards are equal
    #     if they have the same value but not necessarly the same suit.

    #     Card(4, 'Spades') == Cards(4, 'Hearts') will return True

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value


class Collection():
    """An object for a collection of cards. This is the base class for a deck of cards or a player's hand.
        Attributes:
        ----------
        cards : list
            A list to hold the playing card objects in the collection.
        replacement : bool
            If True, self.draw() does NOT remove a card object from the collection.
            If False, self.draw() removes a card object from the collection.
    """

    def __init__(self, cards=None, replacement=False):

        if cards is None:
            self.cards = []
        else:
            self.cards = cards
        self.replacement = replacement

    def shuffle(self) -> None:
        """Randomizes the order of the collection of cards."""

        random.shuffle(self.cards)

    def reveal(self) -> None:
        """Sets the hidden attribut of all card objects to False.
        This is like showing your hand to another player or looking throuhg a deck of cards.
        """
        for card in self.cards:
            card.hidden = False

    def hide(self) -> None:
        """Sets the hidden attribute of all card objects to True.
        Like hiding a card from another player.
        """
        for card in self.cards:
            card.hidden = True

    def show(self):
        """Prints the value and suit of each card in the collection."""

        for card in self.cards:
            card.show()

    def discard(self):
        """Empties the entire collection of cards. The Card instances are removed from the program."""

        self.cards.clear()

    def draw(self, replacement=None) -> Card:
        """Returns the first card in the collection.
        Like drawing a card from a deck or a players hand."""

        if replacement is None:
            replacement = self.replacement

        if replacement:
            return self.cards[0]
        else:
            return self.cards.pop(0)

    def __len__(self) -> int:
        """Returns the number of cards in the collection."""
        return len(self.cards)

    def __add__(self, other): # Определяет добавление в коллекцию карточек. Возвращает новую коллекцию со всеми теми же картами, что и self и other.
        # type(self) гарантирует, что объект коллекции может быть подклассом.
        return type(self)(cards=self.cards + other.cards)


class Deck(Collection): # Колода стандартных игральных карт. Свежеинициализированный объект колоды состоит из 52 карточных объектов со стандартными мастями и значениями. Это можно использовать как колоду карт для игры в различные игры. Наследуется от класса Collection.
    def __init__(self, cards=None):
        super().__init__(cards)
        if self.cards == []:
            self.build()

    def build(self): # Создает 52 карты в стандартной колоде игральных карт. (Этот метод только добавляет карты. Это не удаляет карты из колоды. Чтобы удалить карты,метод discard() должен быть вызван из родительского класса)
        for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
            for value in range(1, 14):
                self.cards.append(Card(value, suit))

    def reset(self): # Возвращает колоду в исходное состояние: 52 стандартные игральные карты.
        self.discard()
        self.build()