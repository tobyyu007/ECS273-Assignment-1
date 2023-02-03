<script lang="ts">
// https://github.com/feifang/vue-wordcloud
// https://www.kaggle.com/code/davidmezzetti/cord-19-analysis-with-sentence-embeddings
// https://www.kaggle.com/code/mobassir/mining-covid-19-scientific-papers
// https://www.kaggle.com/code/gpreda/cord-19-solution-toolbox/notebook

import wordcloud from './components/WordCloud.vue'
import barchart from './components/BarChart.vue'


export default {
  name: 'app',
  components: {
    wordcloud,
    barchart
  },
  methods: {
    wordClickHandler(name, value, vm) {
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
        <barchart/>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
#main-container{
  height: 100%;
}
</style>
