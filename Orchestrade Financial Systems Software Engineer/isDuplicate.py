# Time Complexity: O(n)
# Space Complexity: O(1)


def is_duplicate(input_string):
    if len(input_string)>256:
        return True

    flags = [Flase]*256
    for char in input_string:
        if not flags[ord[char]]:
            flags[ord[char]]
        else:
            return True
    return False
