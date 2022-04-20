# Proset cards

1. Tweak the parameters in `proset.py`. If you are satisfied with the
   default parameters, you can skip step 2.
2. Run it. You can collect the dependencies by hand or use Nix:

    ```
    nix develop --command python proset.py
    ```
3. Then print out the `output/pages.pdf` on your desired paper.
4. Cut out the cards, optionally rounding the corners.
   - I used 80 lbs cardstock at FedEx. FedEx also has a paper slicer
     for cutting the cards.
5. Play!


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
