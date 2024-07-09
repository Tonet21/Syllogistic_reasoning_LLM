from syllo import syllogisms, possible_conclusions


prompts = []
i = 0
for premise1, premise2, mood in syllogisms:
        prompt = f""" 
    Your task is to choose the valid conclusion for a syllogism. You will be presented 
    with a list of four choices for the conclusion and the  premises of the syllogism 
    between three backticks. Your answer should only be one of the choices or <NVC> if 
    you don't find a valid conclusion. The syllogism will be presented
    in the following format:
    Premise 1: <premise 1>
    Premise 2: <premise 2>
    Choices: <list of possible conclusions separated by commas>

    Take your time to answer, do not rush and take it step by step.

    ``` 
    Premise 1: {premise1}
    Premise 2: {premise2}
    Choices: {possible_conclusions[i][0]}, {possible_conclusions[i][1]}, {possible_conclusions[i][2]}, {possible_conclusions[i][3]}
    ```

    """
        prompts.append(prompt)
        i += 1

