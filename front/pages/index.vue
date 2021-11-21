<template>
  <v-row justify="center" align="center">
    <v-col cols="12">
      <h1 class="text-center">Molecules</h1>
    </v-col>
    <v-col cols="12" class="my-4 mt-md-8">
      <v-row justify="center">
        <template v-if="isLoading">
          <v-col cols="12" class="mx-auto text-center">
            <v-progress-circular size="40" indeterminate></v-progress-circular>
          </v-col>
        </template>
        <template v-else>
          <v-col cols="12" md="4" v-for="item in getMoleculesList.data" :key="item.id">
            <client-only>
              <molecule-item :item="item"></molecule-item>
            </client-only>
          </v-col>
        </template>
      </v-row>
    </v-col>
    <v-col cols="12" class="mb-4" v-if="!isLoading">
      <client-only>
        <vs-pagination :current-page="page" :total-pages="getMoleculesList.totalPages" @change="paginate"></vs-pagination>
      </client-only>
    </v-col>
  </v-row>
</template>

<script>
import { mapGetters } from 'vuex';
import moleculeItem from "@/components/molecule/item";
import VsPagination from '@vuesimple/vs-pagination';
export default {
  async fetch({ query, store, error }) {
    const params = { page: query.page }
    await store.dispatch('molecules/getAllMolecules', params)
      .catch((err) => {
        error({
          statusCode: 400,
          message: 'Couldn\'t retrieve molecules list from api'
        })
      })
  },
  components: {
    moleculeItem,
    VsPagination,
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
      'getMoleculesList'
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
        top: 0,
        left: 0,
        behavior: 'smooth'
      });
      const params = { page: this.$route.query.page }
      await this.$store.dispatch('molecules/getAllMolecules', params)
      this.isLoading = false;
    }
  }
}
</script>
