def quadratic_solver(a, b, c):
    if a == 0:
        print("1st coefficient can't be zero. Solving as a linear equation.")
        if b == 0:
            if c == 0:
                print("Infinite solutions (all real numbers are solutions).")
            else:
                print("No solution.")
        else:
            root = -c / b
            print(f"There is only one real root: {root:.3f}")
        return
    
    D = b**2 - 4*a*c
    if D > 0:
        root1 = (-b + D**0.5) / (2*a)
        root2 = (-b - D**0.5) / (2*a)
        print(f"Two real roots: {root1:.3f} and {root2:.3f}")
    elif D == 0:
        root = -b / (2*a)
        print(f"There is only one real root: {root:.3f}")
    else:
        real_part = -b / (2*a)
        imaginary_part = (-D)**0.5 / (2*a)
        fimag = abs(imaginary_part)
        print(f"Two complex roots: {real_part:.3f}+{fimag:.3f}i and {real_part:.3f}-{fimag:.3f}i")

a = float(input("Please enter 1st coefficient: "))
b = float(input("Please enter 2nd coefficient: "))
c = float(input("Please enter 3rd coefficient: "))

quadratic_solver(a, b, c)
