import utils

def selection_sort(_list):
	for i in range(0, len(_list)):
		min = i
		for j in range(i+1, len(_list)):
			if _list[j] < _list[min]:
				min = j
                
		_list[i], _list[min] = _list[min], _list[i]
	return _list
    	

def main():
	listOfNumbers = utils.get_random_ints(10, 0, 100)
	print(listOfNumbers)

	_list = selection_sort(listOfNumbers)
	
	print(_list)


if __name__ == '__main__':
    main()