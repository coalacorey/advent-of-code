import `2023`.InputParser

fun main() {
    println("--- Day 2 ---")
    val input = InputParser.getInputAsStringList("day_02")
    println("Solution part 1: " + solvePart1(input))
    println("Solution part 2: " + solvePart2(input))
}

private fun solvePart1(input: List<String>): String {
    val games = extractInput(input)
    val red = 12
    val green = 13
    val blue = 14

    var res = 0
    for (game in games) {
        var skip = false
        for (cubes in game.cubes) {
            if (!skip) {
                for (cube in cubes) {
                    when (cube.color) {
                        Color.red -> {
                            if (cube.amount > red) {
                                res = res.plus(game.id)
                                skip = true
                                break
                            }
                        }

                        Color.green -> {
                            if (cube.amount > green) {
                                res = res.plus(game.id)
                                skip = true
                                break
                            }
                        }

                        Color.blue -> {
                            if (cube.amount > blue) {
                                res = res.plus(game.id)
                                skip = true
                                break
                            }
                        }
                    }

                }
            }

        }
    }
    return "${games.sumOf { it.id } - res}"
}

private fun solvePart2(input: List<String>): String {
    val games = extractInput(input)

    var res = 0
    for (game in games) {
        var maxRed: Int? = null
        var maxGreen: Int? = null
        var maxBlue: Int? = null
        for (cubes in game.cubes) {
            for (cube in cubes) {
                when (cube.color) {
                    Color.red -> {
                        if (maxRed == null || cube.amount > maxRed) {
                            maxRed = cube.amount
                        }
                    }

                    Color.green -> {
                        if (maxGreen == null || cube.amount > maxGreen) {
                            maxGreen = cube.amount
                        }
                    }

                    Color.blue -> {
                        if (maxBlue == null || cube.amount > maxBlue) {
                            maxBlue = cube.amount
                        }
                    }
                }
            }
        }
        if (maxRed == null) maxRed = 1
        if (maxGreen == null) maxGreen = 1
        if (maxBlue == null) maxBlue = 1
        res += (maxRed * maxGreen * maxBlue)
    }
    return "$res"
}

private fun extractInput(input: List<String>): List<Game> {
    val games = mutableListOf<Game>()

    input.forEach { line ->
        var l = line.replace(" ", "").replace("Game", "")
        val gameId = l.substringBefore(":").toInt()
        l = l.replaceFirst("$gameId:", "")
        val sets = l.split(";")
        val gameSets: MutableList<MutableList<Cubes>> = mutableListOf()
        for (s in sets) {
            val cubeSets: MutableList<Cubes> = mutableListOf()
            val coloredCubes = s.split(",")
            for (c in coloredCubes) {
                val color = c.findAnyOf(Color.entries.map { it.name })
                color?.let {
                    val amount = c.replace(it.second, "").toInt()
                    val cube = Cubes(color = Color.valueOf(it.second), amount = amount)
                    cubeSets.add(cube)
                }
            }
            gameSets.add(cubeSets)
        }
        games.add(Game(gameId, gameSets))
    }
    return games
}

enum class Color {
    red, green, blue
}

data class Cubes(val color: Color, val amount: Int)

data class Game(val id: Int, val cubes: List<List<Cubes>>)