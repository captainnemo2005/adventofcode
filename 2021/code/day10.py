"""
You ask the submarine to determine the best route out of the deep-sea cave, but it only replies:

Syntax error in navigation subsystem on line: all of them
All of them?! The damage is worse than you thought. You bring up a copy of the navigation subsystem (your puzzle input).

The navigation subsystem syntax is made of several lines containing chunks. There are one or more chunks on each line, and chunks contain zero or more other chunks. Adjacent chunks are not separated by any delimiter; if one chunk stops, the next chunk (if any) can immediately start. Every chunk must open and close with one of four legal pairs of matching characters:

If a chunk opens with (, it must close with ).
If a chunk opens with [, it must close with ].
If a chunk opens with {, it must close with }.
If a chunk opens with <, it must close with >.
So, () is a legal chunk that contains no other chunks, as is []. More complex but valid chunks include ([]), {()()()}, <([{}])>, [<>({}){}[([])<>]], and even (((((((((()))))))))).

Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.

A corrupted line is one where a chunk closes with the wrong character - that is, where the characters it opens and closes with do not form one of the four legal pairs listed above.

Examples of corrupted chunks include (], {()()()>, (((()))}, and <([]){()}[{}]). Such a chunk can appear anywhere within a line, and its presence causes the whole line to be considered corrupted.

For example, consider the following navigation subsystem:

[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
Some of the lines aren't corrupted, just incomplete; you can ignore these lines for now. The remaining five lines are corrupted:

{([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
[[<[([]))<([[{}[[()]]] - Expected ], but found ) instead.
[{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
[<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
<{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.
Stop at the first incorrect closing character on each corrupted line.

Did you know that syntax checkers actually have contests to see who can get the high score for syntax errors in a file? It's true! To calculate the syntax error score for a line, take the first illegal character on the line and look it up in the following table:

): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.
In the above example, an illegal ) was found twice (2*3 = 6 points), an illegal ] was found once (57 points), an illegal } was found once (1197 points), and an illegal > was found once (25137 points). So, the total syntax error score for this file is 6+57+1197+25137 = 26397 points!

Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error score for those errors?
"""
import logging as log

log.basicConfig(level=log.DEBUG, format="%(asctime)s %(message)s")

BRACKET_MAP = {")": "(", "]": "[", "}": "{", ">": "<"}
OPEN_BRACKETS = ["(", "[", "{", "<"]
CLOSE_BRACKETS = [")", "]", "}", ">"]
SCORE_MAP_PART1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
SCORE_MAP_PART2 = {")": 1, "]": 2, "}": 3, ">": 4}


def read_data() -> list:
    with open("../data/day10data.txt", "r") as file:
        line = lambda line: [n for n in line]
        return list(map(line, file.read().splitlines()))


def part1(vals) -> int:
    total_score = 0
    for line in vals:
        queue = []
        for i in line:
            if i in OPEN_BRACKETS:
                queue.append(i)
            else:
                open_bracket_in_queue = queue.pop(len(queue) - 1)
                expect_open_bracket = BRACKET_MAP.get(i)
                if expect_open_bracket == open_bracket_in_queue:
                    # log.info(
                    #     f"Expected {expect_open_bracket}, found {open_bracket_in_queue} for {i}"
                    # )
                    pass
                else:
                    # log.info(
                    #     f"Expected {expect_open_bracket}, but found {open_bracket_in_queue} instead for {i}"
                    # )
                    total_score += SCORE_MAP_PART1.get(i)
                    break
    return total_score


def part2(vals) -> int:
    BRACKET_MAP_REVERSE = {v: k for k, v in BRACKET_MAP.items()}
    scores = []

    for line in vals:
        queue = []
        iscorrupted = False
        for i in line:
            if i in OPEN_BRACKETS:
                queue.append(i)
            else:
                open_bracket_in_queue = queue.pop(len(queue) - 1)
                expect_open_bracket = BRACKET_MAP.get(i)
                if expect_open_bracket == open_bracket_in_queue:
                    # log.info(
                    #     f"Expected {expect_open_bracket}, found {open_bracket_in_queue} for {i}"
                    # )
                    pass
                else:
                    # log.info(
                    #     f"Expected {expect_open_bracket}, but found {open_bracket_in_queue} instead for {i}"
                    # )
                    iscorrupted = True
                    break
        if (len(queue) != 0) and (iscorrupted == False):
            score = 0
            # log.info(f"Queue = {queue}")
            # log.info(f"Start with a total score of 0.")
            for i in reversed(queue):
                # log.info(
                #     f"Multiply the total score by 5 to get {score*5}, then add the value of {BRACKET_MAP_REVERSE.get(i)}, ({SCORE_MAP_PART2.get(BRACKET_MAP_REVERSE.get(i))}) to get a new total score of {score*5 + SCORE_MAP_PART2.get(BRACKET_MAP_REVERSE.get(i))}."
                # )
                score = score * 5 + SCORE_MAP_PART2.get(BRACKET_MAP_REVERSE.get(i))
            scores.append(score)
    scores.sort(reverse=True)
    # log.info(f"{scores}")
    return scores[int(len(scores) / 2)]


if __name__ == "__main__":
    # log.info("Loading data....")
    vals = read_data()
    log.info(f"Part1: {part1(vals)}")
    log.info(f"Part2: {part2(vals)}")
