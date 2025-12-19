from trie import Trie
from colorama import Fore, Style, init

init(autoreset=True)


class Homework(Trie):
    def count_words_with_suffix(self, pattern: str) -> int:
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string")

        count = sum(1 for word in self.get_all_words() if word.endswith(pattern))
        print(Fore.GREEN + f"Words ending with '{pattern}': {count}")
        return count

    def has_prefix(self, prefix: str) -> bool:
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string")

        node = self.root
        for char in prefix:
            if char not in node.children:
                print(Fore.RED + f"Prefix '{prefix}' not found")
                return False
            node = node.children[char]

        print(Fore.BLUE + f"Prefix '{prefix}' exists in the Trie")
        return True

    def get_all_words(self, node=None, prefix=""):
        if node is None:
            node = self.root

        words = []
        if node.value is not None:
            words.append(prefix)

        for char, child_node in node.children.items():
            words.extend(self.get_all_words(child_node, prefix + char))

        return words


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    print(Fore.YELLOW + "All words in Trie:", trie.get_all_words())

    trie.count_words_with_suffix("e")  # apple
    trie.count_words_with_suffix("ion")  # application
    trie.count_words_with_suffix("a")  # banana
    trie.count_words_with_suffix("at")  # cat

    trie.has_prefix("app")  # True
    trie.has_prefix("bat")  # False
    trie.has_prefix("ban")  # True
    trie.has_prefix("ca")  # True
