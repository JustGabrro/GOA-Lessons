def find_last_even(numbers_list):
    # გავიმეოროთ სიაში ბოლო ინდექსიდან დაწყებული
    for i in range(len(numbers_list) - 1, -1, -1):
        # შევამოწმოთ არის თუ არა რიცხვი i ინდექსზე ლუწი
        if numbers_list[i] % 2 == 0:
            # თუ ლუწია, დავაბრუნოთ ნომერი
            return numbers_list[i]
    # თუ ლუწი რიცხვი არ არის ნაპოვნი, დავაბრუნოთ None
    return None

#   მაგალითად:
print(find_last_even([1, 2, 3, 4, 5])) 