import `2023`.InputParser
import kotlin.math.pow

fun main() {
    println("--- Day 4 ---")
    val input = InputParser.getInputAsStringList("day_04")
    println("Solution part 1: " + solvePart1(input))
    println("Solution part 2: " + solvePart2(input))
}

private fun solvePart1(input: List<String>): String {
    val cards = extractScratchCards(input)
    return cards.sumOf { it.calculatePoints() }.toInt().toString()
}

private fun solvePart2(input: List<String>): String {
    var res = 0
    val cards = extractScratchCards(input).toMutableList()
    val createsCopies : MutableMap<Int, List<Int>> = mutableMapOf()
    cards.forEachIndexed { index, scratchcard ->
        val hitList = mutableListOf<Int>()
        for (i in 1..scratchcard.calculateHits()) {
            hitList.add(cards[index + i].id)
        }
        createsCopies[scratchcard.id] = hitList
    }
    for (card in cards) {
        res += solveRecursively(scratchcard = card, createsCopies, cards)
    }
    res += cards.size
    return "$res"
}

fun solveRecursively(scratchcard: Scratchcard, map: MutableMap<Int, List<Int>>, cards: List<Scratchcard>): Int {
    return if (map[scratchcard.id]!!.isEmpty()) {
        0
    } else {
        var n = scratchcard.calculateHits()
        map[scratchcard.id]!!.forEach {
            n += solveRecursively(cards.find { scratchcard -> scratchcard.id == it }!!, map, cards)
        }
        n
    }
}

fun extractScratchCards(input: List<String>): List<Scratchcard> {
    val cards = mutableListOf<Scratchcard>()
    input.forEach { line ->
        val gameNumbersSplit = line.split(":")
        val id = gameNumbersSplit.first().replace(Regex("[a-zA-Z]+"), "").trim().toInt()
        val numbersSplit = gameNumbersSplit.last().split("|")
        val winningNumbers = numbersSplit.first().trim().replace("  ", " ").trim().replace(" ", ",").split(",").map { it.toInt() }
        val numbers = numbersSplit.last().trim().replace("  ", " ").trim().replace(" ", ",").split(",").map { it.toInt() }
        cards.add(Scratchcard(id, numbers, winningNumbers))
    }
    return cards
}

data class Scratchcard(
    val id: Int,
    val numbers: List<Int>,
    val winningNumbers: List<Int>
) {
    fun calculatePoints(): Double {
        var res = 0.0
        val n = numbers.filter { it in winningNumbers }.size
        if (n > 0) {
            res = 2.0.pow(n.toDouble() - 1)
        }
        return res
    }

    fun calculateHits(): Int {
        return numbers.filter { it in winningNumbers }.size
    }
}