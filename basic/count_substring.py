def count_substring(string, substring):
    count = 0
    substring_length = len(substring)
    string_length = len(string)
    
    for i in range(string_length - substring_length + 1):
        print(i)
        if string[i:i+substring_length] == substring:
            count += 1
            
    return count

# Example usage
S1 = "timisverttim"
substring = "tim"
occurrences = count_substring(S1, substring)
print(f"The substring '{substring}' occurs {occurrences} times in the string.")
