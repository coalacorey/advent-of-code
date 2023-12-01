package `2023`

import java.io.File
import java.io.InputStream

class InputParser {

    companion object {
        fun getInputAsStringList(path: String, print: Boolean = false): List<String> {
            val inputStream: InputStream = File("2023/${path}/input.txt").inputStream()
            val lineList = mutableListOf<String>()

            inputStream.bufferedReader().forEachLine { lineList.add(it) }
            if (print) {
                lineList.forEach { println(">  $it") }
            }
            return lineList
        }
    }
}