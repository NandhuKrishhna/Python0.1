def calculate_grade():
    """Calculating grade based on marks"""
    try:
        marks = float(input("Please enter your mark"))
        if not 0 <= marks <= 100:
            print("Error: Marks must be between 0 and 100.")
        if marks >= 90:
            print("GRADE: A")
        elif marks >= 80:
            print("GRADE: B")
        elif marks >= 70:
            print("GRADE: C")
        else:
            print("FAILED")
    except ValueError:
        print("Error: Please enter a valid number for marks.")


# # calculate_grade()
# for i in range(1,11):
#     print(f'{5}*{i}={5*i}');

# for i in range(2,21,2):
    # print(i)


# for i in range(1, 11):
#     if i % 3 == 0:
#         continue
#     print(i, end=" ")
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)
