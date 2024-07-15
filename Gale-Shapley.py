def gale_shapley(men_preferences, women_preferences):
    n = len(men_preferences)
    free_men = list(range(n))
    men_partner = [-1] * n
    women_partner = [-1] * n
    women_free_count = n

    while women_free_count > 0:
        man = free_men.pop(0)
        man_prefs = men_preferences[man]

        for woman in man_prefs:
            current_partner = women_partner[woman]

            if current_partner == -1:
                women_partner[woman] = man
                men_partner[man] = woman
                women_free_count -= 1
                break
            else:
                woman_prefs = women_preferences[woman]
                if woman_prefs.index(man) < woman_prefs.index(current_partner):
                    women_partner[woman] = man
                    men_partner[man] = woman
                    free_men.append(current_partner)
                    break
        else:
            free_men.append(man)

    return men_partner, women_partner

def get_preferences(num_people, role):
    preferences = []
    for i in range(num_people):
        print("Enter the preferences for", role, i, "(space-separated indices):")
        prefs = list(map(int, input().split()))
        preferences.append(prefs)
    return preferences

def main():
    num_people = int(input("Enter the number of men/women: "))

    print("Enter the preferences for men:")
    men_preferences = get_preferences(num_people, "man")

    print("Enter the preferences for women:")
    women_preferences = get_preferences(num_people, "woman")

    men_partner, women_partner = gale_shapley(men_preferences, women_preferences)

    print("Men's partners:", men_partner)
    print("Women's partners:", women_partner)

if __name__ == "__main__":
    main()
