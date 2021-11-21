<template>
  <v-card color="primary" height="100%" :to="{name: 'activities-moleculeId', params: { moleculeId: item.id }}" rounded>
    <v-card-title class="justify-center" v-html="item.name"></v-card-title>
    <v-card-text class="text-center">
      <p>Max Phase: {{ item.max_phase }}</p>
      <p>Structure: {{ item.structure }}</p>
      <template v-if="isLoading">
        <v-progress-circular color="white" size="30" indeterminate></v-progress-circular>
      </template>
      <div v-else v-html="molecule"></div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    item: {
      type: Object,
      required: true
    },
  },
  data() {
    return {
      molecule: null,
      isLoading: true,
    }
  },
  mounted() {
    const { structure } = this.item;
    initRDKitModule()
      .then((instance) => {
        let mol = instance.get_mol(structure);
        this.molecule = mol.get_svg();
      })
      .finally(() => {
        this.isLoading = false;
      })
  }
}
</script>
