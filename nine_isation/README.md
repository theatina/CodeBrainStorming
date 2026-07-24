# 🌀 The Nine-isation of Numbers

A Python exploration into one of the most fascinating algorithmic properties of the number 9. 

This repository contains a mathematical script that demonstrates how any positive integer can be collapsed into the number 9 by recursively subtracting the sum of its digits.

## 📖 What is "Nine-isation"?

The code executes a simple but visually striking algorithm:
1. Take any positive integer (e.g., **34**).
2. Calculate the sum of its digits ($3 + 4 = 7$).
3. Subtract that sum from the original number ($34 - 7 = 27$).
4. Repeat the process with the new number. 

No matter how large your starting number is, repeating this loop will cause the number to shrink until it inevitably lands on exactly **9**. 

---

## 🧮 The Mathematical Theory: Why Does It Happen?

This phenomenon is rooted in **Modulo 9 Arithmetic** and the structure of our Base-10 counting system. 

Mathematically, any number $N$ is congruent to the sum of its digits modulo 9:
$$N \equiv \sum \text{digits}(N) \pmod 9$$

Because of this rule, if you subtract the sum of a number's digits from the number itself, the result is **always a perfect multiple of 9**. 
$$N - \sum \text{digits}(N) = 9k$$
*(where k is an integer)*

Because the script loops this subtraction continuously, the number rapidly shrinks by multiples of 9. It acts like a gravitational pull, continuously pulling the number down until it collapses into the ultimate numerical anchor: **9**.

---

## ✨ The Beauty of 9

The number 9 holds a unique "magical" status in number theory. Because it is the highest single digit in Base-10 ($10 - 1$), it acts as a mirror for all other numbers:
* **The Ghost Property (Addition):** Adding 9 to any number doesn't change its digital root. ($4 + 9 = 13 \rightarrow 1 + 3 = 4$).
* **The Black Hole Property (Multiplication):** Multiplying any number by 9 forces its digital root to become 9. ($9 \times 4 = 36 \rightarrow 3 + 6 = 9$).

This script leverages the "Black Hole" property through subtraction!

---

## 🚀 How to Use the Script

The script features an interactive Command-Line Interface (CLI). It is highly optimized using pure integer math (bypassing slow string conversions) and executes extremely fast. 

### Running the program
Run the script in your terminal:
```bash
python -m nine_isation_of_nums
