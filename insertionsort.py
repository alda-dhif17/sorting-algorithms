import utils

def insertion_sort(_list):
	_list = _list.copy()
    
	for i in range(1, len(_list)):
		tmp = _list[i]
		free = 1
		for j in range(i-1, 0):
			if(_list[j] < tmp):
				_list[j+1] = _list[j]
			else:
				free = j + 1
				break
		_list[free] = tmp
		
	return _list



def main():
	listOfNumbers = utils.get_random_ints(10)
	print(listOfNumbers)

	_list = (insertion_sort(listOfNumbers))
	
	print(_list)


if __name__ == '__main__':
    main()