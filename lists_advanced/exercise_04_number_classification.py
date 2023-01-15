all_numbers = list(map(int, input().split(", ")))

positive_list = [str(number) for number in all_numbers if number >= 0]
negative_list = [str(number) for number in all_numbers if number < 0]
even_list = [str(number) for number in all_numbers if number % 2 == 0]
odd_list = [str(number) for number in all_numbers if number % 2 != 0]

print(f"Positive: {', '.join(positive_list)}\n"
      f"Negative: {', '.join(negative_list)}\n"
      f"Even: {', '.join(even_list)}\n"
      f"Odd: {', '.join(odd_list)}")
