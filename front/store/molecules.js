const state = () => ({
  list: null,
  activities: null,
  molecule: null,
})

const getters = {
  getMoleculesList: (state) => state.list,
  getMoleculeActivities: (state) => state.activities,
  getMolecule: (state) => state.molecule,
}

const mutations = {
  SET_MOLECULES_LIST(state, data) {
    state.list = data;
  },
  SET_ACTIVITIES_LIST(state, data) {
    state.activities = data;
  },
  SET_MOLECULE(state, data) {
    state.molecule = data;
  },
}

const actions = {
  getAllMolecules({commit}, params) {
    return new Promise((resolve, reject) => {
      let link = 'molecule/list/';
      if(params.page && params.page > 1) {
        link += `?page=${params.page}`;
      }
      this.$axios.$get(link)
        .then((response) => {
          commit('SET_MOLECULES_LIST', response);
          resolve(response);
        })
        .catch((error) => {
          commit('SET_MOLECULES_LIST', null);
          reject(error);
        })
    })
  },
  getMoleculeActivities({commit}, params) {
    return new Promise((resolve, reject) => {
      let link = `molecule/${params.id}/activities/`;
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
  getMolecule({commit}, id) {
    return new Promise((resolve, reject) => {
      this.$axios.$get(`molecule/${id}/`)
        .then((response) => {
          commit('SET_MOLECULE', response);
          resolve(response);
        })
        .catch((error) => {
          commit('SET_MOLECULE', null);
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
