import `2023`.InputParser

fun main() {
    println("--- Day 3 ---")
    val input = InputParser.getInputAsStringList("day_03")
    println("Solution part 1: " + solvePart1(input))
    println("Solution part 2: " + solvePart2(input))
}

private fun solvePart1(input: List<String>): String {
    val numbers = extractNumbers(input)
    val symbols = extractSymbols(input)

    val overlappingNumbers =
        numbers.filter { number -> number.coordinates.any { coordinate -> coordinate in symbols.flatMap { it.possibleCoordinates } } }

    return "${overlappingNumbers.sumOf { it.n }}"
}

private fun solvePart2(input: List<String>): String {
    var res = 0

    val numbers = extractNumbers(input)
    val symbols = extractSymbols(input)

    val possibleGears = symbols.filter { coordinate -> coordinate.c == "*" }

    possibleGears.forEach { gear ->
        val neighboringNumbers =
            numbers.filter { number: Number -> number.coordinates.any { coordinate: Coordinate -> coordinate in gear.possibleCoordinates } }
                .map { it.n }

        if (neighboringNumbers.size == 2) {
            var m = 1
            neighboringNumbers.forEach { n ->
                m *= n
            }
            res += m
        }
    }
    return "$res"
}

private fun extractNumbers(input: List<String>): MutableList<Number> {
    val numbers = mutableListOf<Number>()
    input.forEachIndexed { y, line ->
        line.forEachIndexed { x, char ->
            val number: Number? = numbers.lastOrNull()
            if (char.isDigit()) {
                if (number == null) {
                    val n = Number(
                        n = char.toString().toInt(),
                        coordinates = mutableListOf(Coordinate(Pair(x, y)))
                    )
                    numbers.add(n)
                } else {
                    if (number.coordinates.last().x == x - 1) {
                        val n = number.copy(
                            n = "${number.n}${char}".toInt(),
                            coordinates = number.coordinates.apply { add(Coordinate(Pair(x, y))) })
                        numbers[numbers.lastIndex] = n
                    } else {
                        val n = Number(
                            n = char.toString().toInt(),
                            coordinates = mutableListOf(Coordinate(Pair(x, y)))
                        )
                        numbers.add(n)
                    }
                }
            }
        }
    }
    return numbers
}

fun extractSymbols(input: List<String>): MutableList<Symbol> {
    val symbols = mutableListOf<Symbol>()
    input.forEachIndexed { y, line ->
        line.forEachIndexed { x, char ->
            if (char != '.' && !char.isDigit()) {
                symbols.add(Symbol(char.toString(), Coordinate(Pair(x, y))))
            }
        }
    }
    return symbols
}

data class Number(
    val n: Int,
    val coordinates: MutableList<Coordinate>,
    val isEnginePart: Boolean = false
)

data class Symbol(
    val c: String,
    val coordinates: Coordinate,
) {
    val possibleCoordinates: MutableList<Coordinate> = getPossibleCoordinates(this.coordinates)

    private fun getPossibleCoordinates(c: Coordinate): MutableList<Coordinate> {
        val coordinates = mutableListOf<Coordinate>()
        for (nX in -1..1) {
            for (nY in -1..1) {
                coordinates.add(Coordinate(Pair(c.x + nX, c.y + nY)))
            }
        }
        return coordinates
    }
}

@JvmInline
value class Coordinate(val c: Pair<Int, Int>) {
    val x: Int
        get() = c.first

    val y: Int
        get() = c.second
}
