numbers = [1,3,8,35, 4,2,3]
numSet = set()

for nums in numbers:
    if nums in numbers:
        if nums in numSet:
            print ("YES")
        else:
            print ("NO")
        numSet.add(nums)

        
def count_distinct_words_and_a(input_string):
    words = input_string.split()
    distinct_words = set(words)
    print("Number of distinct words:", len(distinct_words))

    count_a = sum(word.count('a') for word in distinct_words)
    print("Number of times 'a' appears in distinct words:", count_a)

input_string = " The quick brown fox jumps over the lazy dog"
count_distinct_words_and_a(input_string)



def common_elements(listA, listB):
    setA = set(listA)
    setB = set(listB)

    common_set = setA & setB

    common_list = sorted(list(common_set))

    print(" ".join(map(str, common_list)))

listA = [18, 2, 90, 3, 5]
listB = [2, 86, 42, 5, 7]
common_elements(listA, listB)




def language_info():
    num_people = int(input("How many people are there? "))

    languages = []

    for i in range(1, num_people + 1):
        num_languages = int(input(f"(To person {i}) How many languages can you speak? "))

        person_languages = set()

        for _ in range(num_languages):
            language = input("What languages can you speak in?-Please only input one language ")
            person_languages.add(language)

        languages.append(person_languages)

    common_languages = set.intersection(*languages)

    all_languages = set.union(*languages)

    print("Number of languages everyone speaks:", len(common_languages))
    print("Spoken language(s) everyone speaks:", ', '.join(common_languages))
    print("Total languages spoken in the group:", len(all_languages))
    print("Languages spoken:", ', '.join(all_languages))

language_info()
