export const state = () => ({
  story: {}
});

export const mutations = {
  SET_STORY(state, data) {
    let storyObject = data;
    storyObject.text = storyObject.text.split("\n\n");
    state.story = storyObject;
  }
};

export const actions = {
  async loadStory({ commit }) {
    await this.$axios
      .get("/posts/?limit=1")
      .then(res => {
        commit("SET_STORY", res.data[0]);
      })
      .catch(error => console.log(error));
  }
};
