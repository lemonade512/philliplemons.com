package com.philliplemons

import io.ktor.application.*
import io.ktor.features.*
import io.ktor.html.*
import io.ktor.http.content.defaultResource
import io.ktor.http.content.resources
import io.ktor.http.content.static
import io.ktor.http.content.staticBasePackage
import io.ktor.routing.*
import java.io.File
import kotlinx.html.*


fun Application.main() {
    // This adds Date and Server headers to each response, and allows custom additional headers
    install(DefaultHeaders)
    // This uses the logger to log every call (request/response)
    install(CallLogging)
    log.info("Example log statement")

    routing {
        // Serves the Vue SPA on "/"
        static("/") {
            staticBasePackage = "vueDist"
            defaultResource("index.html")
            resources(".")
        }

        /*
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
        */
    }
}
