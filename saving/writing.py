def writeInput(dataFile: list , FileName : str):
    with open(FileName, "w") as file:
        for i, string in enumerate(dataFile): 
            if i != len(dataFile)-1: file.write(f"{string}\n")
            else: file.write(f"{string}")
            
    file.close()