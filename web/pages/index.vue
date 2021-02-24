<template>
  <div class="container">
    <div>
      <Logo />
      <h1 class="title">
        AITA
      </h1>
      <div class="subtitle">Am I the asshole?</div>
      <div class="links">
        <nuxt-link to="/check" rel="noopener noreferrer" class="button--green">
          Check
        </nuxt-link>
        <nuxt-link to="/random" rel="noopener noreferrer" class="button--grey">
          Random
        </nuxt-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.title {
  font-family: "Quicksand", "Source Sans Pro", -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
