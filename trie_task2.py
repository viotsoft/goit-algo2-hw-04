from trie import Trie
from colorama import Fore, Style, init

init(autoreset=True)


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:

        if not strings or not all(isinstance(s, str) for s in strings):
            print(Fore.RED + "Некоректні вхідні дані.")
            return ""

        for word in strings:
            self.put(word)

        node = self.root
        prefix = ""

        while node and len(node.children) == 1:
            for char, child_node in node.children.items():
                prefix += char
                node = child_node

        if prefix:
            print(Fore.GREEN + f"Найдовший спільний префікс: {prefix}")
        else:
            print(Fore.YELLOW + "Спільного префікса немає.")

        return prefix


if __name__ == "__main__":

    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    print(Fore.CYAN + "Тест 1: ", strings)
    result = trie.find_longest_common_word(strings)
    if result:
        print(Fore.MAGENTA + f"Результат: {result}\n")

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    print(Fore.CYAN + "Тест 2: ", strings)
    result = trie.find_longest_common_word(strings)
    if result:
        print(Fore.MAGENTA + f"Результат: {result}\n")

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    print(Fore.CYAN + "Тест 3: ", strings)
    result = trie.find_longest_common_word(strings)
    if result:
        print(Fore.MAGENTA + f"Результат: {result}\n")
