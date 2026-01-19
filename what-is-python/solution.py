"""
Problem: What is Python?
URL: https://neetcode.io/problems/python-what-is-python/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from decimal import Decimal, getcontext
"""
The Chudnovsky formula is a "Ramanujan-type" series.1 To understand how it works,
we have to look at it as a machine that balances three different moving parts: 
a fixed constant, a linearly growing part, and a massively shrinking part.
The formal identity is:$$\frac{426880\sqrt{10005}}{\pi} = \sum_{k=0}^{\infty} \frac{(6k)! (545140134k + 13591409)}{(3k)! (k!)^3 (-640320)^{3k}}$$1.
The "Constant" (The Scale)The number 426880 $\sqrt{10005}$ (which is C in your code)
acts as a scaling factor. 
The Chudnovsky brothers derived this using complex multiplication of elliptic curves. 
Specifically, it relates to a very special "imaginary quadratic field" 
involving the number $d = 163$.Because $e^{\pi\sqrt{163}}$ is an "almost integer" (it's very close to $640320^3 + 744$), 
this specific formula converges much faster than almost any other series in 
mathematics.2. The Numerator (The Growth)The numerator consists of two main parts:The 
Factorials $(6k)! / ((3k)!(k!)^3)$: This part creates huge integers. 
It represents the "shape" of the curve as it approaches $\pi$.The Linear 
Term 2$(545140134k + 13591409)$: In your code, this is L. 3As $k$ (the loop index) 
increases, this term grows steadily. 
It ensures that each step of the summation "plugs the hole" left by the previous step 
to reach the exact value of $\pi$.3. 
The Denominator (The Precision)The denominator is $(-640320)^{3k}$ (represented by X in 
your code).This is the "engine" of the speed.$640320^3$ is a massive number
(approx $2.62 \times 10^{17}$).Because this number is in the denominator, 
every time the loop increases $k$ by 1, you are dividing the term by roughly $10^{14}$.
How it works together: Each time you run the loop, the numerator gets bigger, 
but the denominator gets bigger much faster. 
This makes the new piece you are adding to the sum incredibly small—so small 
that it only affects the digits roughly 14 places further down the decimal line.4Why 
the code uses M, L, and XInstead of calculating the full formula from scratch every 
time (which would involve calculating $1000!$ then $1001!$, etc.), 
the code uses incremental updates:L (Linear): Just adds $545,140,134$ each loop.
X (Exponential): Just multiplies by the constant $-262,537,412,640,768,000$ each loop.
M (Multinomial): Uses a clever ratio (K ** 3 - 16 * K) // i ** 3 to update the 
factorials based on the previous step's result.Summary of WorkflowInitialize: 
Start with the first term of the series ($k=0$).Iterate: 
Calculate the next "slice" of the sum. Each slice is $10^{14}$ times smaller 
than the last.Summate: Add the slice to the total (S).
Finalize: Multiply the accumulated sum by the constant C and flip it 
(since the formula calculates $1/\pi$).Would you like to see how this formula changes 
if we wanted to calculate a different constant, like $e$ or $\sqrt{2}$?
"""
def calculate_pi(n):
    getcontext().prec = n + 2  # Set precision higher than needed for accuracy
    
    C = 426880 * Decimal(10005).sqrt()
    K = 6
    M = 1
    X = 1
    L = 13591409
    S = L
    
    for i in range(1, n):
        M = (K ** 3 - 16 * K) * M // i ** 3
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12
    
    pi = C / S
    return str(pi)[:n + 2]  # Return first n digits plus the '3.'

n = 20
pi_digits = calculate_pi(n)
print(pi_digits)
