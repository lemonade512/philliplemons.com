package com.philliplemons

import io.ktor.application.*
import io.ktor.features.*
import io.ktor.html.*
import io.ktor.routing.*
import kotlinx.html.*


fun Application.main() {
    // This adds Date and Server headers to each response, and allows custom additional headers
    install(DefaultHeaders)
    // This uses the logger to log every call (request/response)
    install(CallLogging)

    routing {
        get("/") {
            call.respondHtml {
                head {
                    title { +"Ktor on Google App Engine Standard" }
                }
                body {
                    p {
                        +"Hello there! This is ktor running on Google Appengine Standard"
                    }
                }
            }
        }

        /*
        static("/test") {
            resources("static")
        }
        */
    }
}
