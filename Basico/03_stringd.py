# Strings

### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo

my_string = "Hello World"
print(my_string)
print(len(my_string))  # len() is a built-in function
print(my_string[0])  # Indexing
print(my_string[0:5])  # Slicing
print(my_string[6:])    # Slicing
print(my_string[:5])   # Slicing
print(my_string[-1])  # Negative Indexing
print(my_string[-5:-1])  # Negative Slicing
print(my_string[-5:])   # Negative Slicing
print(my_string[:-1])  # Negative Slicing
print(my_string[::2])  # Stepping
print(my_string[::-1])  # Reversing
print(my_string[::-2])  # Reversing and Stepping
print(my_string.upper())    # String Methods
print(my_string.lower())    # String Methods
print(my_string.capitalize())   # String Methods
print(my_string.title())    # String Methods
print(my_string.swapcase())  # String Methods
print(my_string.replace("World", "Universe"))  # String Methods
print(my_string.count("l"))     # String Methods
print(my_string.count("l", 0, 5))       # String Methods
print(my_string.find("l"))    # String Methods
print(my_string.find("l", 0, 5))    # String Methods
