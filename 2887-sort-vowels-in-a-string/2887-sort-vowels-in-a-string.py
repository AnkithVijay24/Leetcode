class Solution:
    def sortVowels(self, s: str) -> str:
        # Define vowels
        vowels = 'aeiouAEIOU'

        # Extract and sort vowels from the string
        sorted_vowels = sorted([char for char in s if char in vowels])

        # Initialize a list for the result
        result = []

        # Index for the sorted vowels
        vowel_index = 0

        # Iterate through the original string
        for char in s:
            if char in vowels:
                # Replace vowel with the next sorted vowel
                result.append(sorted_vowels[vowel_index])
                vowel_index += 1
            else:
                # Keep consonants as is
                result.append(char)

        # Join the list into a string and return
        return ''.join(result)
