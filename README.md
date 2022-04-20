# Proset cards

1. Tweak the parameters in `proset.py`. If you are satisfied with the
   default parameters, you can skip step 2.
2. Run it. You can collect the dependencies by hand or use
   [Nix][2]/[Nix flakes][3]:

    ```
    nix develop --command python proset.py
    ```
3. Then print out the [`output/pages.pdf`][1] on your desired paper.
4. Cut out the cards, optionally rounding the corners.
   - I used 80 lbs cardstock at FedEx. FedEx also has a paper slicer
     for cutting the cards.
5. Play!

[1]: https://github.com/charmoniumQ/proset/blob/main/output/pages.pdf
[2]: https://nixos.org/
[3]: https://nixos.wiki/wiki/Flakes#Installing_flakes

## Playing the game

1. Shuffle all the cards face down into a deck.
2. Take 7 cards from the deck and lay them face up on the table, where
   every player can reach them.
3. Players try to find a subset of cards such that the subset contains
   an even number of every color pip. When a player finds one, they
   say, "proset", and take the cards into their stack.
4. The dealer replaces the cards, if there are cards left in the deck
   (so there are 7 cards in the play area until the deck runs
   out).
5. Repeat step 3 and 4 until there are no cards in the deck or in the
   play area.
6. The player with the greatest number of cards in their stack wins.

# Is this just the card game Set?

No.

- It's easier to explain.
- Prosets can be any number of cards (including the entire board).
- One is guaranteed a proset in at most 7 cards.
- There should be no cards left at the end of the game (the remaining
  cards should form a proset for someone to grab).
  - This is a useful checksum. If this property is violated, each
    player should review their stack to make sure they only took valid
    prosets.

# The theory

- Each card is a 6-long vector whose elements are binary
  ($\mathbb{Z}^6_2$, for those in the know).
- A proset is a set of cards which reduce to zero under addition
  modulo 2 (also known as XOR).
- In any set of 7 6-dimensional vectors, there must be a non-trivial
  relation among those vectors. This non-trivial relation is a proset.
- There can be more than one proset on a board of 7 6-pip
  cards. Challenge question: How many prosets can their be on a board
  of 7 6-pip cards?
