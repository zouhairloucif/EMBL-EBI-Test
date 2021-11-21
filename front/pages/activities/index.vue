<template>
  <v-row justify="center" align="center" class="mt-4 mt-md-8">
    <v-col cols="12">
      <h1 class="text-center">Activities</h1>
    </v-col>
    <v-col cols="12" class="mt-4 mt-md-8">
      <v-row justify="center">
        <template v-if="isLoading">
          <v-col cols="12" class="mx-auto text-center">
            <v-progress-circular size="40" indeterminate></v-progress-circular>
          </v-col>
        </template>
        <template v-else>
          <v-col cols="12" md="4" v-for="item in getAllActivities.data" :key="item.id">
            <activity-item :item="item"></activity-item>
          </v-col>
        </template>
      </v-row>
    </v-col>
    <v-col cols="12" class="mb-4" v-if="!isLoading">
      <client-only>
        <vs-pagination :current-page="page" :total-pages="getAllActivities.totalPages" @change="paginate"></vs-pagination>
      </client-only>
    </v-col>
  </v-row>
</template>

<script>
import { mapGetters } from 'vuex';
import activityItem from "@/components/activity/item";
import VsPagination from '@vuesimple/vs-pagination';
export default {
  components: {
    activityItem,
    VsPagination
  },
  data() {
    return {
      isLoading: false,
    }
  },
  created() {
    this.fetchData();
  },
  watch: {
    '$route.query.page': {
      handler(val, oldVal) {
        this.fetchData()
      }
    }
  },
  computed: {
    ...mapGetters('activities', [
      'getAllActivities'
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
      await this.$store.dispatch('activities/getAllActivities', params)
      this.isLoading = false;
    }
  }
}
</script>
