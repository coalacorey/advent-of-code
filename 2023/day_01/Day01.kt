import `2023`.InputParser

fun main() {
    println("--- Day 1 ---")
    val input = InputParser.getInputAsStringList("day_01")
    println("Solution part 1: " + solvePart1(input))
    println("Solution part 2: " + solvePart2(input))
}

private fun solvePart1(input: List<String>): String {
    val res: List<Int> = input.map { line ->
        //Replace all characters
        var l = line.replace(Regex("[a-zA-Z]*"), "")

        //If we have a single digit, it acts as first and last digit and therefore we combine them
        l = if (l.length > 1) l else l + l

        //Get first and last digit and turn it into an int
        l.filterIndexed { index, _ -> index == 0 || index == l.lastIndex }.toInt()
    }
    return res.sum().toString()
}

private fun solvePart2(input: List<String>): String {
    val numbers = mapOf(Pair("one", "1"), Pair("two", "2"), Pair("three", "3"), Pair("four", "4"), Pair("five", "5"), Pair("six", "6"), Pair("seven", "7"), Pair("eight", "8"), Pair("nine", "9"))
    val res: List<Int> = input.map { line ->
        var l = line

        //Find first occurrence of a written digit, replace it if it appears before the first digit
        var numResults = l.findAnyOf(numbers.keys, 0, false)
        if (numResults != null) {
            val firstNumIndex = l.findAnyOf(numbers.values)?.first ?: Int.MAX_VALUE
            if (numResults.first < firstNumIndex) {
                l = l.replaceFirst(numResults.second, numbers.getOrDefault(numResults.second, numResults.second))
            }
        }

        //Find last occurrence of a written digit, replace it if it appears after the last digit
        numResults = l.findLastAnyOf(numbers.keys, l.lastIndex, false)
        if (numResults != null) {
            val lastNumIndex = l.findLastAnyOf(numbers.values, startIndex = l.lastIndex)?.first ?: Int.MIN_VALUE
            if (numResults.first > lastNumIndex) {
                l = l.replaceLast(numResults.second, numbers.getOrDefault(numResults.second, numResults.second))
            }
        }

        //Replace remaining characters
        l = l.replace(Regex("[a-zA-Z]+"), "")

        //If we have a single digit, it acts as first and last digit and therefore we combine them
        l = if (l.length > 1) l else l + l

        //Get first and last digit and turn it into an int
        l.filterIndexed { index, _ -> index == 0 || index == l.lastIndex }.toInt()
    }
    return res.sum().toString()
}

fun String.replaceLast(oldValue: String, newValue: String): String {
    val lastIndex = lastIndexOf(oldValue)
    if (lastIndex == -1) {
        return this
    }
    val prefix = substring(0, lastIndex)
    val suffix = substring(lastIndex + oldValue.length)
    return "$prefix$newValue$suffix"
}