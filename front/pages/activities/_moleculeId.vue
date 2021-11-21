<template>
  <v-row justify="center" align="center" class="mt-4 mt-md-8">
    <v-col cols="12">
      <v-row>
        <v-col cols="12">
          <h1 class="text-center">
            <v-icon large>mdi-molecule</v-icon>
            Molecule
          </h1>
        </v-col>
        <v-col cols="12" offset-md="3" md="6">
          <molecule-item :item="getMolecule"></molecule-item>
        </v-col>
      </v-row>
      <v-divider class="my-6"></v-divider>
      <v-col cols="12" ref="mainElem">
        <h2 class="text-center">
          <v-icon large>mdi-file-tree</v-icon>
          Activities
        </h2>
      </v-col>
      <v-row justify="center" class="my-4">
        <template v-if="isLoading">
          <v-col cols="12" class="mx-auto text-center">
            <v-progress-circular size="40" indeterminate></v-progress-circular>
          </v-col>
        </template>
        <template v-else>
          <v-col cols="12" md="4" v-for="item in getMoleculeActivities.data" :key="item.id">
            <activity-item :item="item"></activity-item>
          </v-col>
        </template>
        <v-col cols="12" class="mb-4" v-if="!isLoading">
          <client-only>
            <vs-pagination :current-page="page" :total-pages="getMoleculeActivities.totalPages" @change="paginate"></vs-pagination>
          </client-only>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<script>
import { mapGetters } from 'vuex';
import moleculeItem from "@/components/molecule/item";
import activityItem from "@/components/activity/item";
import VsPagination from '@vuesimple/vs-pagination';
export default {
  async fetch({ store, query, params, error }) {
    const param = {
      id: params.moleculeId,
      page: query.page
    }
    await store.dispatch('molecules/getMolecule', params.moleculeId)
      .catch((err) => { error({ statusCode: 400,  message: 'Couldn\'t retrieve molecule activities list from api' }) })
    await store.dispatch('molecules/getMoleculeActivities', param)
      .catch((err) => { error({ statusCode: 400,  message: 'Couldn\'t retrieve molecule activities list from api' }) })
  },
  components: {
    moleculeItem,
    activityItem,
    VsPagination
  },
  data() {
    return {
      isLoading: false,
    }
  },
  watch: {
    '$route.query.page': {
      handler(val, oldVal) {
        if(val && val > 1) {
          this.fetchData()
        }
      }
    }
  },
  computed: {
    ...mapGetters('molecules', [
      'getMoleculeActivities',
      'getMolecule'
    ]),
    page: {
      get() { return parseInt(this.$route.query.page) || 1 ; },
      set(val) { this.$router.push({ query: { page: val } }); },
    }
  },
  methods: {
    paginate(page) {
      this.page = page;
    },
    async fetchData() {
      this.isLoading = true;
      window.scrollTo({
        top: this.$refs.mainElem.clientY,
        left: this.$refs.mainElem.clientX,
        behavior: 'smooth'
      });
      const params = {
        id: this.$route.params.moleculeId,
        page: this.$route.query.page
      };
      await this.$store.dispatch('molecules/getMoleculeActivities', params)
      this.isLoading = false;
    }
  }
}
</script>
