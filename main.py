from pysine import sine

# In 12-tone equal temperament, octaves are split into 12 intervals,
# frequency ratios of which are "12th root of 2" : 1. These 1/12 parts of
# an octave are called a half step. Furthermore, multiplying a frequency
# by "12th root of 2" results in a tone a half step above the initial tone,
# and dividing results in a tone a half step below the initial tone.
hs_coef = 2 ** (1/12)  # Half step frequency ratio is "12th root of 2 : 1"
ws_coef = hs_coef ** 2 # Whole step is essentially multiplying the
                       # initial frequency twice by the half step frequency
                       # ratio


def step_up(scale, idx, tone):
    # Step up one diatonic step
    if scale[idx] == 0:
        tone *= ws_coef
    else:
        tone *= hs_coef

    if idx == 6:
        idx = 0
    else:
        idx += 1
    return tone, idx


def step_down(scale, idx, tone):
    # Step down one diatonic step
    if idx == 0:
        idx = 6
    else:
        idx -= 1

    if scale[idx] == 0:
        tone /= ws_coef
    else:
        tone /= hs_coef
    return tone, idx


def scale_selection():
    while True:
        scale_input = str(input("Please select a scale (type 'help' for options): ")).lower()

        if scale_input == "help":
            print(f"+{20 * '-'}+")
            print("|  Possible scales:  |\n"
                  "|  * major           |\n"
                  "|  * minor           |\n"
                  "|  * melodic_minor   |\n"
                  "|  * locrian         |")
            print(f"+{20 * '-'}+")
            print()
        elif scale_input.startswith("maj"):
            scale_steps = [0, 0, 1, 0, 0, 0, 1]
            break
        elif scale_input.startswith("min"):
            scale_steps = [0, 1, 0, 0, 1, 0, 0]
            break
        elif scale_input.startswith("mel"):
            scale_steps = [0, 1, 0, 0, 0, 0, 1]
            break
        elif scale_input.startswith("loc"):
            scale_steps = [1, 0, 0, 0, 1, 0, 0]
            break
    scale_index = [0, 1, 2, 3, 4, 5, 6]
    scale = {scale_index[i]: scale_steps[i] for i in range(len(scale_steps))}
    return scale


def main():
    # Title
    print(f"+{39*'-'}+")
    print("|  Cursed Angels We Have Heard On High  |")
    print(f"+{39 * '-'}+")
    print("\n")

    # Choose a scale
    scale = scale_selection()

    # Choose tempo (beats per minute)
    BPM = int(input("Please input a tempo (BPM): "))
    # Define note lengths
    n1_4 = 1 / (BPM / 60)
    nd1_4 = 1.5 * n1_4
    n2_4 = n1_4 * 2
    n1_8 = n1_4 / 2

    # Choose a tonic
    tonic = 440 # tonic is A

    """
    #Scale tester
    tone=440
    idx=0
    for step in range(len(scale)):
        sine(frequency=tone, duration=n1_4)
        tone, idx = step_up(scale, idx, tone)
    sine(frequency=tone, duration=n1_4)
    """

    print("\n")
    print("Lyrics:")
    print()

    # The real thing
    tone = tonic * ws_coef ** 2  # start on C#5
    idx = 2
    repeat = 0
    for j in range(2):
        repeat += 1

        if repeat == 1:
            print("Angels we have heard on high")
        else:
            print("And the mountains in reply")
        sine(frequency=tone, duration=n1_4)
        sine(frequency=tone, duration=n1_4)
        sine(frequency=tone, duration=n1_4)
        tone, idx = step_up(scale, idx, tone)
        tone, idx = step_up(scale, idx, tone)
        sine(frequency=tone, duration=n1_4)

        sine(frequency=tone, duration=nd1_4)
        tone, idx = step_down(scale, idx, tone)
        sine(frequency=tone, duration=n1_8)
        tone, idx = step_down(scale, idx, tone)
        sine(frequency=tone, duration=n2_4)

        if repeat == 1:
            print("Sweetly singing o’er the plains,")
        else:
            print("Echoing their joyous strains.")
        sine(frequency=tone, duration=n1_4)
        tone, idx = step_down(scale, idx, tone)
        sine(frequency=tone, duration=n1_4)
        tone, idx = step_up(scale, idx, tone)
        sine(frequency=tone, duration=n1_4)
        tone, idx = step_up(scale, idx, tone)
        tone, idx = step_up(scale, idx, tone)
        sine(frequency=tone, duration=n1_4)

        tone, idx = step_down(scale, idx, tone)
        tone, idx = step_down(scale, idx, tone)
        sine(frequency=tone, duration=nd1_4)
        tone, idx = step_down(scale, idx, tone)
        sine(frequency=tone, duration=n1_8)
        tone, idx = step_down(scale, idx, tone)
        sine(frequency=tone, duration=n2_4)

        tone, idx = step_up(scale, idx, tone)
        tone, idx = step_up(scale, idx, tone)

    # The curse
    idx = 4
    tone = tonic*ws_coef**3*hs_coef
    repeat = 0
    while True:
        repeat += 1

        if repeat == 1:
            print("Gloo-oooo")
        elif repeat == 6:
            print("oo-oooo (The shepherds are looking at each other, confused)")
        elif repeat == 10:
            print("oo-oooo (It's getting awkward)")
        elif repeat == 13:
            print("oo-oooo (The shepherds probably left at this point)")
        else:
            print("oo-oooo")
        sine(frequency=tone, duration=n2_4)
        tone, idx = step_up(scale, idx, tone)
        sine(frequency=tone, duration=n1_8)
        tone, idx = step_down(scale, idx, tone)
        sine(frequency=tone, duration=n1_8)
        tone, idx = step_down(scale, idx, tone)
        sine(frequency=tone, duration=n1_8)
        tone, idx = step_down(scale, idx, tone)
        sine(frequency=tone, duration=n1_8)
        tone, idx = step_up(scale, idx, tone)



if __name__ == "__main__":
    main()