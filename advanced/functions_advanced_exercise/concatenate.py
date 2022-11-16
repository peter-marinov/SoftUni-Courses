def concatenate(*args, **kwargs):
    text = ''.join(args)
    for key, value in kwargs.items():
        if key in text:
            text = text.replace(key, value)
    return text

print(concatenate("Soft", "UNI", "Is", "Grate",
                  "!", UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons",
                  C="P", s="", java='Java'))
