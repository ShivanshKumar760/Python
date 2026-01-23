# Add Superhero Abilities

**🔗 [View on NeetCode](https://neetcode.io/problems/python-add-superhero-abilities/question)**

---

In this challenge, you'll extend the `SuperHero` class by adding new ability methods. The class and its attributes have already been defined in the provided code. Your tasks are outlined below:

**1. Enhance the `SuperHero` class:**

- Add methods `attack()` and `heal()` to the `SuperHero` class.

**2. Implement the ability methods:**

- `attack()`: Should print a string in the format `"{name} attacks with {power}!"`

- `heal()`: Should increase the superhero's `health` attribute by 10 points and print `"{name} heals 10 points. New health: {health}."`

**3. Create a superhero instance:**

- Create a superhero with the name "Catwoman", power "Agility", and health 120.

**4. Use the abilities:**

- Call the `attack()` and `heal()` methods for each superhero.

#### Expected Output

```
Catwoman attacks with Agility!
Catwoman heals 10 points. New health: 130.
```

Hints

- Remember, when defining methods in a class, always include `self` as the first parameter. For example: `def method_name(self):`.

- In the `attack()` method, use `print()` to show a message like "[name] attacks with [power]!"

- For `heal()`, increase `self.health` by 10 and print a message about healing.

- To create a hero: `hero1 = SuperHero("Hero Name", "Superpower", 100)`

- Remember to remove `pass` when you add code to a method.

---

## 💡 Solution

Check the `solution.py` file for the implementation.

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

*Synced from [NeetCode](https://neetcode.io) • [GitHub Pusher Extension](https://github.com/)*
