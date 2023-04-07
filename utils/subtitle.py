def generate_subtitle(text):
    # output.txt will be used to display the subtitle on OBS
    with open("output.txt", "w", encoding="utf-8") as outfile:
        try:
            words = text.split()
            lines = [words[i:i+10] for i in range(0, len(words), 10)]
            for line in lines:
                outfile.write(" ".join(line) + "\n")
        except:
            print("Error writing to output.txt")


