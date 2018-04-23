; Load this file into an interactive session with:
; python3 scheme -load quiz03.scm

(define (map f s)
  ; List the result of applying f to each element in s.
  (if (null? s) s
    (cons (f (car s)) (map f (cdr s)))))

(define (filter f s)
  ; List the elements of s for which f returns a true value.
  (if (null? s) s
    (let ((rest (filter f (cdr s))))
      (if (f (car s)) (cons (car s) rest) rest))))

(define (no-repeats s)
  (define t (list))
  (define (contains s v)
    (if (null? s) False
      (if (= v (car s)) True
        (contains (cdr s) v))))
  (define (make-list t s)
    (cond ((null? s) nil)
      ((contains t (car s)) (make-list t (cdr s)))
      ((not (contains t (car s))) (cons (car s) (make-list (append t (list (car s))) (cdr s))))))
  (make-list t s))

(define (how-many-dots s)
  (cond ((null? s) 0)
    ((and (pair? s) (number? (cdr s))) (+ 1 (how-many-dots (car s))))
    ((pair? s) (+ (how-many-dots (car s)) (how-many-dots (cdr s))))
    (else 0)))
