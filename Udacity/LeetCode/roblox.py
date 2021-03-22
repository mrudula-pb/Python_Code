"""
Imagine we have an image. We'll represent this image as a simple 2D array
where every pixel is a 1 or a 0.
The image you get is known to have a single rectangle of 0s on a background of 1s.

Write a function that takes in the image and returns one of the following representations
 of the rectangle of 0's: top-left coordinate and bottom-right coordinate OR top-left
 coordinate, width, and height.

image1 = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 0, 0, 0, 1],
  [1, 1, 1, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1],
]

Sample output variations (only one is necessary):

findRectangle(image1) =>
  x: 3, y: 2, width: 3, height: 2
  2,3 3,5 -- row,column of the top-left and bottom-right corners
"""
# top_left_row = row
            # top_left_column = column
            # column += 1
            # while image1[row][column] == 0:
            #     column += 1  # column 6
            # bottom_right_row = row
            # bottom_right_column = column
    # return (top_left_row, top_left_column, bottom_right_row, bottom_right_column)

def return_2dImage(image1):
    global bottom_right_row, bottom_right_column

def top_left_row_column():
    global top_left_row, top_left_column
    img_length = len(image1)
    for row in range(img_length):
        for column in range(img_length):
            while image1[row][column] == 0:
                top_left_row = row
                top_left_column = column
                row += 1
                print(top_left_row, top_left_column)
            if image1[row][column] != 0:
                column += 1
            else:
                row += 1
            continue

# def find_bottom_right_row_column(top_left_row, top_left_column, image1):
#     # global bottom_right_row, bottom_right_column
#     length = len(image1)
#     while image1[top_left_row][top_left_column] != 1:
#         top_left_row += 1
#     if
#             top_left_column += 1
#             top_left_row -= 1
#             continue
#
#     for top_left_row in range(length):
#         for top_left_column in range(length):
#             if image1[top_left_row][top_left_column] == 0:
#                 top_left_row += 1
#                 continue
#             elif image1[top_left_row][top_left_column] != 0:
#                 top_left_column += 1
#                 continue
#             continue

image1 = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
]
top_left_row, top_left_column = top_left_row_column(image1)
# find_bottom_right_row_column(top_left_row, top_left_column, image1)
print(top_left_row, top_left_column)
#print(bottom_right_row, bottom_right_column)