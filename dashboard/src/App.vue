<script lang="ts">
import Notes from './components/Notes.vue'
import Example from './components/Example.vue'
import ExampleWithLegend from './components/ExampleWithLegend.vue';
import wordcloud from './components/WordCloud.vue'
import ExampleWithInteractions from './components/ExampleWithInteractions.vue';
import { createStore } from './stores/index';

export default {
  name: 'app',
  components: {
    wordcloud,
    ExampleWithLegend,
    Notes
  },
  methods: {
    wordClickHandler(name, value, vm) {s
      console.log('wordClickHandler', name, value, vm);
    }
  },
  data() {
    return {
      myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
    }
  }
}

</script>

<template>
  <v-container id="main-container" class="d-flex flex-column flex-nowrap" fluid>
    <v-row no-gutters>
      <v-col>
        <wordcloud
          nameKey="name"
          valueKey="value"
          :color="myColors"
          :showTooltip="true"
          :wordClick="wordClickHandler">
        </wordcloud>
      </v-col>
      <v-col>
        <Notes/>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
#main-container{
  height: 100%;
}
</style>
