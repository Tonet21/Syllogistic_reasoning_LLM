from syllo import syllogisms, possible_conclusions

system_message = f"""You are an expert in syllogistic reasoning.
                     Your role is to evaluate a syllogism and select the valid conclusion from a list of four options.
                     You will be provided with two premises and four possible conclusions in the following format:

                     Premise 1: <premise 1>
                     Premise 2: <premise 2>
                     Choices: <list of choices separated by commas>

                     Your response should be one of the given choices, or "NVC" if none of the options are valid.
                     State your choice ; there is no need to explain your reasoning .
                     Please take your time to analyze the syllogism carefully and avoid rushing to a conclusion.
                     """
prompts = []
i = 0
for premise1, premise2, mood, type_ in syllogisms:
        prompt = f"""

                    Premise 1: {premise1}
                    Premise 2: {premise2}
                    Choices: {possible_conclusions[i][0]}, {possible_conclusions[i][1]}, {possible_conclusions[i][2]}, {possible_conclusions[i][3]}

    """
        prompts.append(prompt)
        i += 1


