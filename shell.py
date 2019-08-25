import bhasha

while True:
    text = input("bhasha > ")
    result , error = bhasha.run(text)

    if error:
        print(error.as_string())
    else:
        print(result)
