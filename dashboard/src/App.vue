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
  }
}

</script>

<template>
  <div id="body" style="text-align: center">
    <v-container id="main-container" class="d-flex flex-column flex-nowrap" fluid>
      <v-row no-gutters>
        <v-col>
          <h1 class="title">Data Visualization for COVID-19 Open Research Dataset</h1>
          <br/><br/>
        </v-col>
      </v-row>
      <v-row no-gutters>
        <v-col>
          <h3 class="description">Most Frequent Words in Paper's Abstract</h3>
          <wordcloud/>
        </v-col>
        <v-col>
          <h3 class="description">Number of Articles by Publication Year</h3>
          <barchart/>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<style>
#body {
  height: 100%;
  display:flex; flex-direction:column; justify-content:center;
  min-height:100vh;
}
.description {
  font-familt: 'Aerial';
  font-size: 18px;
}
.title {
  font-familt: 'Aerial';
  font-size: 35px;
  text-align: center;
}
</style>
