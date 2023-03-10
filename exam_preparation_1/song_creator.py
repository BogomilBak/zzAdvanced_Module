def add_songs(*args):
    result = {}
    end_result = ""
    for key, value in args:
        if key not in result:
            result[key] = []
        result[key].extend(value)
    for key, value in result.items():
        end_result += f'- {key}'"\n"
        if value:
            end_result += f'\n'.join(value)
            end_result += '\n'
    return end_result



print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))




