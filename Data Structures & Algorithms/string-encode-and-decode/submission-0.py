class Solution:

    # - Turn each char into ord 
    # - Group by comma
    # - Within the substring, delineate by *
    # - Empty strings, use a single *

    # ["ab", "c", "def"] -> "97*98,99,100*101*102" -> ["99*98", "99", "100*101*102"]
    # [""] -> ["*"] (note: check if len = 1 and str[0] == '*')
    # ["", ""] -> "*,*" -> ["*,*"]
    # ["", "ab", "a", ""] -> *,97*98,97,* -> ["*", "97*98", "*"]

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs: # ["", "ab", "a", ""]
            encoded_str = ""
            if len(string) == 0:
                encoded_str += "*,"
            else:
                for i in range(len(string)):
                    encoded_str += str(ord(string[i]))
                    if i + 1 < len(string):
                        encoded_str += "*"
                    else:
                        encoded_str += ","
            output += encoded_str
        return output
        
    def decode(self, s: str) -> List[str]:
        split_strs = s.split(",") # ["*", "97*98", "*"]
        split_strs.pop() # remove because of splitting on last comma
        output = []
        for string in split_strs:
            if string == "*":
                output.append("")
            else:
                decoded_string = ""
                chars = string.split("*") # ["97", "98"]
                for char in chars:
                    decoded_string += chr(int(char)) # "a" -> "ab"
                output.append(decoded_string)
        return output
                








