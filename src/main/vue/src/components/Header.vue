<template>
  <aside>
    <div class="container">
      <RouterLink to="/"><h1>Phillip Lemons</h1></RouterLink>
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </aside>
</template>

<style scoped>
aside {
  color: rgba(235, 235, 235, 0.64);
  min-width: 20%;
  height: 100vh;
  background: #202020;
  line-height: 1.5;
  display: flex;
  flex-direction: column;
}

.container {
  position: relative;
  margin: 0 15%;
}

h1 {
  color: rgba(235, 235, 235, 0.64);
  font-size: 30px;
  text-align: center;
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
