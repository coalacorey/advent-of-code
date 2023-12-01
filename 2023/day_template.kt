import java.io.File
import java.io.InputStream

fun main() {
    print("--- Day X ---")
    val input = getInput()
    print("Solution part 1: " + solvePart1(input))
    print("Solution part 2: " + solvePart2(input))
}

fun solvePart1(input: List<String>): String {
    return ""
}

fun solvePart2(input: List<String>): String {
    return ""
}

fun getInput(): List<String> {
    val inputStream: InputStream = File("input.txt").inputStream()
    val lineList = mutableListOf<String>()

    inputStream.bufferedReader().forEachLine { lineList.add(it) }
    lineList.forEach { println(">  $it") }
    return lineList
}