import os
import json


directory = os.path.dirname(os.path.abspath(__file__))


def getContents(fileName):
    with open(os.path.join(directory, fileName), "r", encoding="utf8") as file:
        data = []
        for line in file:
            line = line.replace("\n", "")
            data.append(line)

    return data


def getTranslations(fileName):
    with open(os.path.join(directory, fileName), "r", encoding="utf8") as file:
        data = json.load(file)
    
    return data


def updateTranslations(jsonData, fileName):
    jsonObject = json.dumps(jsonData, indent=4, ensure_ascii=False)

    with open(os.path.join(directory, fileName), "w", encoding='utf8') as outfile:
        outfile.write(jsonObject)


def getConsecutive(jsonData):
    keys = jsonData.keys()
    
    return int(list(keys)[-1]) + 1


def main():
    englishTranslations = getContents("english.txt")
    spanishTranslations = getContents("spanish.txt")
    translations = getTranslations("translations.json")

    if len(englishTranslations) != len(spanishTranslations):
        raise ValueError("Length of english and spanish translations has to be the SAME.")
    
    print("---SETTINGS---")
    name = input("Name: ")
    
    translationPairs = []
    for i in range(len(englishTranslations)):
        translationPairs.append([englishTranslations[i], spanishTranslations[i]])
        
    translations[getConsecutive(translations)] = {
        "name": name,
        "translations": translationPairs
    }

    updateTranslations(translations, "translations.json")

    print(f"\nAdded {len(translationPairs)} translation pairs.")
    

if __name__ =="__main__":
    main()
