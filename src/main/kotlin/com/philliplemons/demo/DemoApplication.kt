package com.philliplemons.demo

/*

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.boot.web.servlet.support.SpringBootServletInitializer

@SpringBootApplication
class DemoApplication : SpringBootServletInitializer()

fun main(args: Array<String>) {
	runApplication<DemoApplication>(*args)
}
*/

import io.ktor.application.Application
import io.ktor.application.call
import io.ktor.response.respond
import io.ktor.routing.get
import io.ktor.routing.routing

fun DemoApplication.main() {
    routing {                             // 1
        get("/") {                        // 2
            call.respond("Hello World!!") // 3
        }
    }
}
