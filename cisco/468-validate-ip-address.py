class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        idx = ip_type = 0         
        while idx < len(queryIP) and idx  < 5 and ip_type == 0:
            qch = queryIP[idx]
            if qch == ".":
                ip_type = 4
            elif qch == ":":
                ip_type = 6
            
            idx += 1

        if ip_type == 0:
            return "Neither"

        if ip_type == 4:
            parts = queryIP.split(".")
            if len(parts) != 4:
                return "Neither"

            for part in parts:
                if len(part) == 0 or len(part) > 3: 
                    return "Neither"
                
                if (part[0] == "0" and len(part) != 1) or  (not part.isdigit()) or (int(part) > 255):
                    return "Neither"
        
            return "IPv4"
        else:
            parts = queryIP.split(":")
            if len(parts) != 8:
                return "Neither"

            valid_character = set(
                ["A", "B", "C", "D", "E", "F","a", "b", "c", "d", "e", "f", 
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
            for part in parts:
                if len(part) == 0 or len(part) > 4:
                    return "Neither"

                for pch in part:
                    if pch not in valid_character:
                        return "Neither"
            return "IPv6"

print(Solution().validIPAddress("2001:0db8:85a3:00000:0:8A2E:0370:7334"))