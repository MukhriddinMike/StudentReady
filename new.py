class Student:
    num_of_students = 0

    def __init__(self, name, date, number):
        self.name = name
        self.date = date
        self.number = number

    def get_info(self):
        dataset_list = ''.join(self.name)
        for item in dataset_list.split(' '):
            dataset_array.append(item)

        quick_sort(dataset_array)


list = []
dataset_array = []
finish = False
history = []


def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


while (not finish):
    input_stream = input().split()
    action = input_stream[0]
    if action == 'n':
        name = input_stream[1]
        birthdate = input_stream[2]
        number = input_stream[3]
        if birthdate == number:
            print("Duplicate Number")
        temp = Student(name, birthdate, number)
        list.append(temp)

    elif action == "e":
        exit()

    elif action == "h":
        if len(history) == 0:
            print("is empty")
            continue
        history.reverse()
        for x in history:
            for one in list:
                if x == one.name:
                    print(one.name, one.date, one.number)




    elif action == "f":
        name = input_stream[1]
        if name in list:
            history.append(name)
        if name in list:
            print("{0} {1} {3}".format(Student.name, Student.date, Student.number))
    elif action == "s":
        for student in list:
            # print(student)
            student.get_info()
        for student_arr in dataset_array:
            print(student_arr)

    else:
        finish = True
