# -*- coding: utf-8 -*-
def longest_common_substring(string1, string2):
    """
    The function returns the number of longest common substring which can be
    created from two input strings without swaps.

    Input format (string1, string2) where string1 and string2 are strings.
    """
    string1_len = len(string1)
    old_row, current_row = [0]*(string1_len+1), [0]*(string1_len+1)
    for char2 in string2:
        for j, char1 in enumerate(string1):
            if char2 == char1:
                current_row[j] = old_row[j-1]+1
            else:
                current_row[j] = max(current_row[j-1], old_row[j])
        old_row, current_row = current_row, [0]*(string1_len+1)
    return max(old_row)
