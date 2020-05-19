(terpri)
(princ "Program to calculate factorial of a number iteratively and then display it.")
(terpri)
(terpri)
(princ "Enter the number: ")
(setq n (read))
(setq no n)

(defun fac(num)
	(if (= num 1)
	      1
    	(* num (fac (decf num 1)))
	)
)

(terpri)
(princ "The factorial of no is: ")
(write (fac n))

