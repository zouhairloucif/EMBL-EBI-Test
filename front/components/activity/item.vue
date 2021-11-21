<template>
  <v-card height="100%" :ripple="false" outlined>
    <v-card-text class="text-center">
      <p>Type: {{ item.type }}</p>
      <p>Units: {{ item.units }}</p>
      <p>Value: {{ item.value }}</p>
      <p>Relation: {{ item.relation }}</p>
      <p>Target Name: {{ item.target ? item.target.name : 'N/A' }}</p>
      <p>Target Organism: {{ item.target ? item.target.organism : 'N/A' }}</p>
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
}
</script>
