# Write a function "pretty_print_dict" that prints a given dict in sorted order


def pretty_print_dict (dictionary):
    for key, value in sorted(dictionary.items()):
        print(key, value)

#Key = student name; value = disney character
students = {
"Annamarie" : "Baymax",
"Adriana" : "Rapunzel",
"Sydney" : "Ariel",
"Lisette" : "Mulan"
}
pretty_print_dict(students)
