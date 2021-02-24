<template>
  <div class="container">
    <div class="story">
      <h1 class="story-title">{{ story.title }}</h1>
      <ul class="story-lines">
        <li class="story-line" v-for="(line, n) in story.text" :key="n">
          {{ line }}
        </li>
      </ul>
      <h1 class="story-classification">{{ story.label }}</h1>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  head() {
    return {
      title: "AITA - Random"
    };
  },
  computed: {
    ...mapState("story", ["story"])
  },
  created() {
    this.$store.dispatch("story/loadStory");
  }
};
</script>

<style>
.story {
  margin: 0 8rem;
}
.story-title {
  margin: 2rem 0;
}
.story-lines {
  text-align: justify;
  list-style-type: none;
}
.story-line {
  margin: 1rem 0;
}
.story-classification {
  margin: 2rem 0;
}
@media screen and (min-width: 1200px) {
  .story {
    margin: 0 16rem;
  }
}
@media screen and (max-width: 768px) {
  .story {
    margin: 0 2rem;
    text-align: center;
  }
}
</style>
