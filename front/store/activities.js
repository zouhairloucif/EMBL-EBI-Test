const state = () => ({
  list: null,
})

const getters = {
  getAllActivities: (state) => state.list,
}

const mutations = {
  SET_ACTIVITIES_LIST(state, data) {
    state.list = data;
  },
}

const actions = {
  getAllActivities({commit}, params) {
    return new Promise((resolve, reject) => {
      let link = 'activity/list/';
      if(params.page && params.page > 1) {
        link += `?page=${params.page}`;
      }
      this.$axios.$get(link)
        .then((response) => {
          commit('SET_ACTIVITIES_LIST', response);
          resolve(response);
        })
        .catch((error) => {
          commit('SET_ACTIVITIES_LIST', null);
          reject(error);
        })
    })
  },
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
