# upper traingular matrix 
MAX = 100; 
  
def luDecomposition(mat, n): 
  
    lower = [[0 for x in range(n)]  
                for y in range(n)]; 
    upper = [[0 for x in range(n)]  
                for y in range(n)];
                  
    # Decomposing matrix into Upper  
    # and Lower triangular matrix 
    for i in range(n): 
  
        # Upper Triangular 
        for k in range(i, n):  
  
            # Summation of L(i, j) * U(j, k) 
            sum = 0; 
            for j in range(i): 
                sum += (lower[i][j] * upper[j][k]); 
  
            # Evaluating U(i, k) 
            upper[i][k] = mat[i][k] - sum; 
  
        # Lower Triangular 
        for k in range(i, n): 
            if (i == k): 
                lower[i][i] = 1; # Diagonal as 1 
            else: 
  
                # Summation of L(k, j) * U(j, i) 
                sum = 0; 
                for j in range(i): 
                    sum += (lower[k][j] * upper[j][i]); 
  
                # Evaluating L(k, i) 
                lower[k][i] = int((mat[k][i] - sum) /
                                       upper[i][i]); 
  
    # setw is for displaying nicely 
    print("Lower Triangular:"); 
    print("\n")
    matrix = []
    # Displaying the result : 
    for i in range(n): 
        a = []
        # Lower 
        for j in range(n): 
            a.append(lower[i][j]);  
        matrix.append(a);

    for i in range(n):
        print(matrix[i])

    print("\n")
    print("Upper Triangular:");
    print("\n") 
    matrix = []
    # Displaying the result : 
    for i in range(n): 
        a = []
        # Lower 
        for j in range(n): 
            a.append(upper[i][j]);  
        matrix.append(a);

    for i in range(n):
        print(matrix[i]) 
  
# Driver code 
mat = [] 

n=int(input('Enter the n (n * n matrix): '))
for i in range(n):
    a = []
    for j in range(n):
            a.append(int(input('Enter element [{0}] [{1}]  '.format(i,j))))
    mat.append(a)
luDecomposition(mat, n); 
