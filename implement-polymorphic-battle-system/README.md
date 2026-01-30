# Implement Polymorphic Battle System

**🔗 [View on NeetCode](https://neetcode.io/problems/python-implement-polymorphic-battle-system/question)**

---

Given the code of the `Hero` class complete the following tasks:

- Create a `Warrior` class that inherits from `Hero` and overrides the `attack` method to return the `power + 10` of the hero.

- Create a `Mage` class that inherits from `Hero`. Set the `health` to 80 and override the `attack` method to return the `power + 20` of the hero.

- Create a `show_attack` function that takes a hero and prints the attack of the hero using the format `{hero.name} attacks with {hero.attack} damage!`

Hints

- The key to polymorphism is that `show_attack()` works with any hero type

- Each hero type can implement `attack()` differently

- Remember to use the `super()` function to call the parent class's `__init__` method when initializing the child class

- You can update the `health` attribute of the hero using the `self.health` attribute in the child class

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
