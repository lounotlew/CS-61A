(define (deep-map fn s)
	(cond ((null? s) nil)
		((list? (car s)) (cons (deep-map fn (car s)) (deep-map fn (cdr s))))
		(else (cons (fn (car s)) (deep-map fn (cdr s))))))

(define (substitute s old new)
	(cond ((null? s) nil)
		((list? (car s)) (cons (substitute (car s) old new) (substitute (cdr s) old new)))
		((equal? (car s) old) (cons new (substitute (cdr s) old new)))
		(else (cons (car s) (substitute (cdr s) old new)))))

(define (sub-all s olds news)

	(define (contains s v)
		(if (null? s) False
			(if (equal? v (car s)) True
				(contains (cdr s) v))))

	(define (replacer x olds news)
		(if (null? olds) nil
			(if (equal? x (car olds)) (cons (car news) (sub-all (cdr s) olds news))
				(replacer x (cdr olds) (cdr news)))))
	
	(cond ((null? s) nil)
		((list? (car s)) (cons (sub-all (car s) olds news) (sub-all (cdr s) olds news)))
		((contains olds (car s)) (replacer (car s) olds news))
		(else (cons (car s) (sub-all (cdr s) olds news)))))