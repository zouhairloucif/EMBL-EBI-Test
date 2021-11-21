<template>
  <v-app dark>
    <v-navigation-drawer v-model="drawer" fixed app>
      <v-list rounded>
        <v-list-item v-for="(item, i) in items" :key="i" :to="{name: item.to}" router exact>
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <v-container>
        <v-row>
          <v-col cols="12" class="text-right">
            <v-btn plain fab @click="toggleDarkMode">
              <v-icon>mdi-weather-night</v-icon>
            </v-btn>
          </v-col>
        </v-row>
        <Nuxt />
      </v-container>
    </v-main>

  </v-app>
</template>

<script>
export default {
  data () {
    return {
      drawer: true,
      items: [
        {
          icon: 'mdi-molecule',
          title: 'Molecules',
          to: 'index'
        },
        {
          icon: 'mdi-file-tree',
          title: 'Activities',
          to: 'activities'
        }
      ],
    }
  },
  methods: {
    toggleDarkMode() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
    }
  }
}
</script>

<style lang="scss" scoped>
@import "assets/main";
</style>
