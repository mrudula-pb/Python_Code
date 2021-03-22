# You are a developer for a university. Your current project is to develop a system for students to find courses they share with friends. The university has a system for querying courses students are enrolled in, returned as a list of (ID, course) pairs.

# Write a function that takes in a list of (student ID number, course name) pairs and returns,
# for every pair of students, a list of all courses they share.

# We can assume that the total number of courses a student can take is bounded by a small constant.

# Sample Input:

# student_course_pairs_1 = [
#   ["58", "Linear Algebra"],
#   ["94", "Art History"],
#   ["94", "Operating Systems"],
#   ["17", "Software Design"],
#   ["58", "Mechanics"],
#   ["58", "Economics"],
#   ["17", "Linear Algebra"],
#   ["17", "Political Science"],
#   ["94", "Economics"],
#   ["25", "Economics"],
#   ["58", "Software Design"],
# ]

# Sample Output (pseudocode, in any order):

# find_pairs(student_course_pairs_1) =>
# {
#   "58,17": ["Software Design", "Linear Algebra"]
#   "58,94": ["Economics"]
#   "58,25": ["Economics"]
#   "94,25": ["Economics"]
#   "17,94": []
#   "17,25": []
# }



# Additional test cases:

# Sample Input:

# student_course_pairs_2 = [
#   ["42", "Software Design"],
#   ["0", "Advanced Mechanics"],
#   ["9", "Art History"],
# ]

# Sample output:

# find_pairs(student_course_pairs_2) =>
# {
#   "0,42": []
#   "0,9": []
#   "9,42": []
# }



# n: number of student,course pairs in the input
# s: number of students
# c: number of courses being offered
import collections

student_course_pairs_1 = [
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"],
    ["25", "Economics"],
    ["58", "Software Design"],
]

student_course_pairs_2 = [
    ["42", "Software Design"],
    ["0", "Advanced Mechanics"],
    ["9", "Art History"],
]

def find_pairs(student_course_pairs_1):
    #print(student_course_pairs_1)

    # dict_course = collections.defaultdict(list)
    # for element in student_course_pairs_1:
    #     dict_course[element[1]].append((element[0]))
    # print(dict_course)

    # result = dict()
    # print(len(student_course_pairs_1))
    # for sub in range(len(student_course_pairs_1)):
    #     print(student_course_pairs_1[sub])
    #     #print(len(student_course_pairs_1[sub]))
    #     for element in range(len(student_course_pairs_1[sub])):
    #         print(student_course_pairs_1[sub][element])

    # My
    # solution
    # would
    # be
    # to
    # make
    # a
    # Dictionary
    # with the student being the key and the value would be a Set of courses.

    # The time complexity for this method is O(N + N ^ 2) = O(N ^ 2) and the space is O(N) or O(2N)
    # if you consider answer but still O(N).

# make
    #     # a
    #     # Dictionary
    #     # with the student being the key and the value would be a Set of courses.
    result = {}
    students = []
    enrollment = collections.defaultdict(set)
    for entry in student_course_pairs_1:
        student_id, course = entry
        if student_id not in enrollment:
            students.append(student_id)
        enrollment[student_id].add(course)
    print(enrollment)
    print(students)

    # Then iterate through all key pairs and take the intersection between the
    # two value sets and append the intersection result as an answer for current pair.
    for i, student in enumerate(students):
        print(student)
        for j in range(i+1, len(students)):
            common = enrollment[student].intersection(enrollment[students[j]])
            if common:
                result[(student, students[j])] = list(common)
            else:
                []
    return result
    #return pass

value = find_pairs(student_course_pairs_1)
print(value)

