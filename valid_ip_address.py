def restore_ip_addresses(s):
    def is_valid(segment):
        # Check if the segment is valid: <= 255 and no leading zeroes unless it's '0'
        return int(segment) <= 255 and (segment == "0" or not segment.startswith("0"))

    def backtrack(start=0, parts=[]):
        # If we've reached 4 parts and we are at the end of the string, add to result
        if len(parts) == 4 and start == len(s):
            result.append('.'.join(parts))
            return
        # If we've reached 4 parts or the end of the string, stop
        if len(parts) == 4 or start == len(s):
            return

        # Try all possible 1, 2, and 3 length segments
        for length in range(1, 4):
            # Ensure we do not go past the string length
            if start + length <= len(s):
                segment = s[start:start + length]
                if is_valid(segment):
                    backtrack(start + length, parts + [segment])

    result = []
    backtrack()
    return result


# Test cases
# ['255.255.11.135', '255.255.111.35']
print(restore_ip_addresses("25525511135"))
print(restore_ip_addresses("25505011535"))  # []
