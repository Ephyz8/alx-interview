def pascal_triangle(n):
    """
     Returns a list of integers
     representing the Pascal Triangle of n
     returns empty list if n <= 0
     """
    triangle = []
    if n <= 0:
       return triangle
    for j in range(n):
     row = [1] * (j + 1)
     for k in range(1, j):
       row[k] = triangle[j - 1][k - 1] + triangle[j - 1][k]
       triangle.append(row)
       return triangle
    
