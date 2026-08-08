class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        cleaned_text = re.sub(r"[^a-zA-Z0-9]","", s)

        cleaned_text=cleaned_text.lower()


        reversed_text = cleaned_text[ : :-1]

        if cleaned_text == reversed_text:
            return True
        else :
            return False