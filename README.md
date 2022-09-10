The `old` directory has my code and blog posts from before my refactor to Kotlin.

Most of the configuration files are taken from the Ktor example appengine repository:
https://github.com/GoogleCloudPlatform/kotlin-samples/tree/main/appengine/ktor

The following commands are useful:
- `./gradlew appengineRun`
- `./gradlew appengineDeploy`


## Vue App

I use Vue for my main blog pages. To run just do the following:

```
cd src/main/vue
npm install
npm run dev
```

If you want to build the app for deploy, run `npm run build` from the `src/main/vue` directory. This
will add a `distVue` folder to resources which then gets included with the ktor build.
