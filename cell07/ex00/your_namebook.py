def array_of_names(persons):
    return [f"{person} {name}".capitalize() for person, name in persons.items()]

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))