        original_position = alphabet.index(letter)
        encrypted_word += alphabet[(original_position + 2) % 26]
        #(Index+Moves)%Total?