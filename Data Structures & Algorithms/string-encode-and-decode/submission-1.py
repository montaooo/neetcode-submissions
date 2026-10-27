class Solution:
    
    def encode(self, strs: List[str]) -> str:
        char = "い"
        encoded = ""
        for s in strs:
            encoded += (char + s)
        
        return encoded

    def decode(self, s: str) -> List[str]:
        char = "い"

        decoded = s.split("い")[1:]

        return decoded
