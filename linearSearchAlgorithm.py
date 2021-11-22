def search(arr, search_Element):
	left = 0
	length = len(arr)
	position = -1
	right = length - 1
	for left in range(0, right, 1):
		if (arr[left] == search_Element):
			position = left
			print("Element found in Array at ", position +
				1, " Position with ", left + 1, " Attempt")
			break

		# If search_element is found with
		# right variable
		if (arr[right] == search_Element):
			position = right
			print("Element found in Array at ", position + 1,
				" Position with ", length - right, " Attempt")
			break
		left += 1
		right -= 1
	if (position == -1):
		print("Not found in Array with ", left, " Attempt")
arr = [1, 2, 3, 4, 5]
search_element = 5
search(arr, search_element)
