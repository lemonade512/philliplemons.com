<script>
import anime from 'animejs/lib/anime.es.js';

export default {
  mounted() {
    // Wrap every letter in a span
    var textWrappers = document.querySelectorAll('.hiddenText');
    for (let i = 0; i < textWrappers.length; i++) {
      var textWrapper = textWrappers[i];
      textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");
    }

    setTimeout(() => {
      anime.timeline()
        .add({
          targets: '.a1 .letter',
          opacity: 1,
          delay: (el, i) => 70 * i
        }).add({
          targets: '.a2 .letter',
          opacity: 1,
          delay: (el, i) => 70 * i
        }, '+= 300')
    }, 1500);
  }
}
</script>

<template>
  <main>
    <h1 class="a1 hiddenText">Oh, hello!</h1>
    <h1 class="a2 hiddenText">What is your name?</h1>
  </main>
</template>

<style>
.circle {
  height: 50px;
  width: 50px;
  border-radius: 50%;
  background-color: red;
}

.letter {
  opacity: 0;
}
</style>
