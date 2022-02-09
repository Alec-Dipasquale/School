;;5
(define (SAME-AS atom list)
    (cond ((null? list) 'T)
          ((equal? atom (car list)) (SAME-AS atom(cdr list)))
          (else 'NIL)))