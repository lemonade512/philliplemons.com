<template>
  <aside>
    <RouterLink to="/"><h1>Phillip <span class="lastName">Lemons</span></h1></RouterLink>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
    </nav>
  </aside>
</template>

<style scoped>
aside {
  color: rgba(235, 235, 235, 0.64);
  padding: 30px;
  height: 100vh;
  background: #202020;
  line-height: 1.5;
  display: flex;
  flex-direction: column;
}

h1 {
  color: rgba(235, 235, 235, 0.64);
  font-size: 30px;
  text-align: center;
  margin: 0;
}

a:hover .lastName {
  transition: color 0.5s;
  color: #edd772;
}

nav {
  display: flex;
  flex-direction: column;
  width: 100%;
  font-size: 18px;
  text-align: center;
  margin-top: 2rem;
}

a {
  text-decoration: none;
}

nav a {
  padding: 10px;
  text-transform: uppercase;
}

nav a:hover {
  background: #343434;
}

nav a:visited {
  color: rgba(150, 150, 150, 0.64);
}
</style>
