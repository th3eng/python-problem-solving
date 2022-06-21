from string import ascii_letters, punctuation


def arithmetic_arranger(list_of_sums, show_result=True) -> str:
    """
    Args:
        list_of_sums: list of sums in string
        show_result: boolean, True if result should be shown
    Returns:
        string: string of formatted arithmetic problems
    
    Maximum number of problems is 5.
    Maximum number of digits in a sum is 4. eg. "1234 + 5678"
    Two numbers allowed in a problem. eg. "1234 + 5678"
    Operators are limited to +, -.
    """
    if len(list_of_sums) == 0:
        return "You have no sums to display."

    if len(list_of_sums) > 5:
        return "Error: Too many problems."

    # Create a variable containing all rejected symbols and letters
    rejectedSymbols = (ascii_letters + punctuation).translate(
        {ord(c): None for c in "+- "}
    )

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    # Check if all sums are valid and add them to the lines
    for sum in list_of_sums:
        for symbol in rejectedSymbols:
            if symbol in sum:
                print(f"Error: Numbers must only contain digits.{symbol}")
                return
        if "+" not in sum and "-" not in sum:
            print("Error: Operator must be '+' or '-'.")
        else:
            operator = "+" if "+" in sum else "-"

            nums = str(sum).split(operator)

            # Check if the equation is valid
            if nums.__len__() != 2:
                print("elements must be two!")
                return

            # remove spaces from numbers
            nums[0] = nums[0].strip()
            nums[1] = nums[1].strip()

            # Check if numbers are valid (only 4 digits per number)
            for num in nums:
                # Check if number digits not more than 4
                if len(num) > 4:
                    print("Error: Numbers cannot be more than four digits.")
                    return

            # Add the numbers to the lines
            line1 += f'{" "* ((max(len(nums[0]),len(nums[1]))+2) - len(nums[0]))}{int(nums[0])}    '
            line2 += f'{operator}{" "* ((max(len(nums[0]),len(nums[1]))+1) - len(nums[1]))}{int(nums[1])}    '
            line3 += ("-" * (max(len(nums[0]), len(nums[1])) + 2)) + "    "

            # calculate the result
            if show_result:
                result = (
                    (int(nums[0]) + int(nums[1]))
                    if operator == "+"
                    else (int(nums[0]) - int(nums[1]))
                )
                line4 += f'{" "*((max(len(nums[0]), len(nums[1]))+2)-len(str(result)))}{result}    '

    # remove last space from all lines
    line1.removesuffix("    ")
    line2.removesuffix("    ")
    line3.removesuffix("    ")
    line4.removesuffix("    ")

    # return the formatted equations
    return f"{line1}\n{line2}\n{line3}\n{line4}"
