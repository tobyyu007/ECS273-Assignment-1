<script lang="ts">
import Notes from './components/Notes.vue'
import Example from './components/Example.vue'
import ExampleWithLegend from './components/ExampleWithLegend.vue';
import wordcloud from './components/WordCloud.vue'
import ExampleWithInteractions from './components/ExampleWithInteractions.vue';
import { createStore } from './stores/index';

export default {
  name: 'app',
  setup() { // Composition API syntax
        const store = createStore()
        return {
            store
        }
    },
  created() {
        this.store.fetchExample("GET");
        //console.log(this.store.wordCount);
    },
  components: {
    wordcloud,
    ExampleWithLegend,
    Notes
  },
  methods: {
    wordClickHandler(name, value, vm) {
      console.log('wordClickHandler', name, value, vm);
    }
  },
  data() {
    var wordCount = this.store.wordCount;
    // console.log("1234");
    var words = Object.keys(wordCount);
    var wordCountIndex = 0;
    var resultArray = Object.keys(wordCount).map(function(word){
        let person = {
          "name": words[wordCountIndex],
          "value": wordCount[word]
        }
        wordCountIndex++;
        return person;
    });
    console.log(resultArray);
    return {
      myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
      defaultWords: resultArray,
    }
  }
}

</script>

<template>
  <v-container id="main-container" class="d-flex flex-column flex-nowrap" fluid>
    <v-row no-gutters>
      <v-col>
        <wordcloud
          :data="defaultWords"
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
